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
typedef long long ll;
using namespace std;

int ntest;
ll n,d,g;
int main () {
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    REP(t,ntest){
        printf("Case #%d: ",t+1);
        cin>> n >> d >> g;
        if(g==100 && d<100) printf("Broken\n");
        else if(g==0 && d> 0) printf("Broken\n");
        else if(n<100){
            bool flag=false;
            for(int num=1; num<n+1 && !flag; num++){
                REP(w,num+1){
                    if(w*100 == num*d) { printf("Possible\n"); flag= true; break;}
                }
            }
            if(!flag)
                printf("Broken\n");
        }
        else printf("Possible\n");
    }
    return 0;
}
