#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>

#define oo 1000000005
#define eps 1e-11

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i < _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i > _b; i--)
#define RESET(c,x) memset (c, x, sizeof (c))

#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

int ntest,n;
string str;
char adj[256][256];
bool clear[256][256];

int main () {
    freopen("B-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    REP(t,ntest){
        printf("Case #%d: ",t+1);        
        memset(adj,0,sizeof adj);
        memset(clear,0,sizeof clear);
        cin>> n;
        REP(i,n){
            cin>> str;
            adj[str[0]][str[1]] = adj[str[1]][str[0]] = str[2];
        }
        cin>> n;
        REP(i,n){
            cin>> str;
            clear[str[0]][str[1]] = clear[str[1]][str[0]] = true;
        }
        vector<char> vt;
        cin>>n;
        cin>> str;
        REP(i,n){
            char temp;
            if(vt.size()) temp= vt[vt.size()-1];
            if( vt.size() && adj[ temp ][str[i]] ){                
                vt.pop_back();
                vt.PB( adj[ temp ][str[i]] );
            }
            else{
                vt.PB( str[i] );
                REP(j,vt.size()-1)
                    if( clear[vt[j]][str[i]] ){
                        vt.clear();
                        break;
                    }
            }            
        }
        printf("[");
        REP(i,vt.size()-1)
            printf("%c, ",vt[i]);
        if(vt.size()) printf("%c",vt[vt.size()-1] );
        printf("]\n");        
    }       
    return 0;
}
