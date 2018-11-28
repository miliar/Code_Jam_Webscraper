#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define CLEAR(t) memset((t), 0, sizeof(t))

#define sz size()
#define pb push_back
#define pf push_front

#define VI vector<int>
#define VS vector<string>
#define LL long long

#define INF (1<<30)

int main() {
    int n;
    
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    
    cin >> n;
    REP( ncase, n ) {
        string s;
        VI o;
        int k;
        
        cin >> k >> s;
        REP(i,k) o.pb( i );
        
        //cout << s << endl;
        
        int soln = INF;
        do {
            string en;
            int start = 0;
            while( start != s.sz ) {
                REP(i, o.sz) {
                    en += s[ start + o[i] ];
                } 
                start += k;
            }
            
            //cout << en << endl;
            //system("pause");
            // after encryption
            char last = en[0];
            int ans = 1;
            REP(i, en.sz) {
                if( en[i] != last ) {
                    ans ++;
                    last = en[i];
                }
            } 
            soln <?= ans;
        }while( next_permutation( o.begin(), o.end() ) );
        
        printf("Case #%d: %d\n",ncase+1,soln);
    }

    //system("pause");
    
    return 0;
}
