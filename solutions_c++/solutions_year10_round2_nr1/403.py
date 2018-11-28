#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <string>
#include <cctype>
#include <cstdlib>
#include <iostream>

#define X real()
#define Y imag()
#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define EPS 1e-9
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )

using namespace std;

typedef long long ll;
typedef long double ld;


set<string> ard;

int main() {
    int T;
    scanf("%d",&T);
//cout << T << endl;
    FR(i,T) {
        int N,M;
        scanf("%d %d",&N,&M);
        ard.clear();
        string l;
        FR(i,N) {
            cin >> l;
            FR(i,l.size()) {
                if(l[i]=='/'&&i>0) {
                    ard.insert(l.substr(0,i));
                }                
            }            
            ard.insert(l);
        }        
        
        
        int res=0;
        FR(i,M) {
            cin >> l;
            FR(i,l.size()) {
                if(l[i]=='/'&&i>0) {
                    if(ard.find(l.substr(0,i))==ard.end()) res++;
                    ard.insert(l.substr(0,i));
                }
            }
            if(ard.find(l)==ard.end()) res++;
            ard.insert(l);
        }
        
        printf("Case #%d: ",i+1);
        cout << res << endl;
    }
}