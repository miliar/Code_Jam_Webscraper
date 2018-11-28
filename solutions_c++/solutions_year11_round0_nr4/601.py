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
int n,a[1005];
bool c[1005];
int main () {
    freopen("D-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    REP(t,ntest){
        printf("Case #%d: ",t+1);  
        scanf("%d",&n);
        REP(i,n) scanf("%d",&a[i+1]);
        memset(c,false,sizeof c);
        double r=0;
        FOR(i,1,n){
            if(!c[i]){
                c[i]=true;
                int l=0;                
                for(int k=a[i]; !c[k]; k = a[k], l++) c[k]=true; 
                if(l) r+= (l+1);
            }
        }
        printf("%.6lf\n",r);
    }
    return 0;
}
