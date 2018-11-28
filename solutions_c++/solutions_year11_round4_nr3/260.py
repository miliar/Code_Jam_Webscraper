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
long long n;

bool p[1000005];
int main () {
    freopen("C-large.in","r",stdin);
    freopen("test.out","w",stdout);
    memset(p,true,sizeof p); p[0]=p[1]=false;
    for(int i=2; i<1000005; i++) if(p[i]) for(long long j=1LL*i*i; j<1000005; j+=i) p[j]=false;
    scanf("%d",&ntest);
    REP(test,ntest){        
        printf("Case #%d: ",test+1);   
        cin>>n;
        if(n==1){ printf("0\n"); continue;}
        
        int res=0;
        for(int i=2; i<1000005; i++){
            if(p[i]){
                long long temp=1LL*i*i;
                while( n>= temp) res++, temp*=i;
            }
        }
        res++;
        printf("%d\n",res);            
    }
    return 0;
}
