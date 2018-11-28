#include<iostream>
#include<string>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#include<vector>
#include<set>
#include<algorithm>
#include<utility>
#include<bitset>
#include<sstream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cctype>

#define FOR(a,b) for(int a=0;a<b;a++)
#define FORR(a,b) for(int a=b-1;a>=0;a--)
#define INR(a,b) (0<=a && a<b)
#define CLEAR(a,b) memset(a,b,sizeof a)

#define PB push_back
#define LLI long long
#define PII pair<int,int>
#define MKP make_pair
#define VI vector<int>
#define VS vector<string>
#define VVI vector< vector<int> >
#define VVS vector< vector< string > >
#define IT iterator

#define MAX 101

using namespace std;

int main(){
    int t;

    cin >> t;

    FOR(t_n,t){
        int n, tot=0, oo=0, ob=0, xo=1, xb=1;
        cin >> n;

        FOR(i,n){
            char c;
            int but,mov;
            cin >> c >> but;

            if(c=='O'){
                mov = abs(xo-but)-oo;
                if(mov<0){
                    mov = 0;
                }
                oo = 0;
                mov++;
                ob += mov;
                xo = but;
            }
            else{
                mov = abs(xb-but)-ob;
                if(mov<0){
                    mov = 0;
                }
                ob = 0;
                mov++;
                oo += mov;
                xb = but;
            }
            tot +=mov;
        }
        cout << "Case #"<<t_n+1<<": "<<tot<<endl;

    }
    return 0;
}
