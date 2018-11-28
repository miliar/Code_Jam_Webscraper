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

int ntest;
char c[101];
int r[101];
int orange[101],blue[101];
int n;
int main () {
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    REP(t,ntest){
        printf("Case #%d: ",t+1);
        scanf("%d ",&n);
        REP(i,n)
            scanf("%c %d ",&c[i],&r[i]);
        int dO=1,dB=1;
        int cO=0,cB=0;
        REP(i,n){
            if(c[i]=='O'){
                orange[cO++] = abs(r[i]-dO)+1;
                dO=r[i];
            }
            else if(c[i]=='B'){
                blue[cB++] =  abs(r[i]-dB)+1;
                dB=r[i];
            }                 
        }    
        int s=0;
        cO=0,cB=0;
        REP(i,n){
            if(c[i]=='O'){
                s+= orange[cO];
                blue[cB] =  blue[cB]-orange[cO] > 1 ?  blue[cB]-orange[cO] : 1;
                cO++;                
            }
            if(c[i]=='B'){
                s+= blue[cB];
                orange[cO] =  orange[cO]-blue[cB] > 1 ?  orange[cO]-blue[cB] : 1;
                cB++;                
            }
        }
        printf("%d\n",s);
    }
    return 0;
}
