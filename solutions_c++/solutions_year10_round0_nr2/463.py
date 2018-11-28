#include <stdio.h>
#include <stdlib.h>
#include<utility>
#include<algorithm>
using namespace std;

int C,N,line,t[1002];

int gcd(int a,int b)
{
    if(a>b) swap(a,b);
    while(a) {
        int temp=a;
        a=b%a;
        b=temp;
    }
    return b;
}

void solve()
{
    int T=t[N-1]-t[N-2]; if(T<0) T=-T;
    for(int i=N-1;i>=1;--i) {
        t[i]-=t[i-1];
        if(t[i]<0) t[i]=-t[i];
        T=gcd(T,t[i]);
    }
    //printf("%d ",T);
    //for(int i=0;i<N;++i) printf("%d ",t[i]);
    int ret=T*((t[0]/T)+1)-t[0];
    if(ret==T) ret=0;
    printf("Case #%d: %d\n",line,ret);
}
int main()
{
      freopen("C:\\³Ì±ó\\code jam\\Fair Warning\\B-small-attempt0.in","r",stdin);
      freopen("C:\\³Ì±ó\\code jam\\Fair Warning\\B-small-attempt0.out","w",stdout);
      scanf("%d",&C);
      for(line=1;line<=C;++line) {
         scanf("%d",&N);
         for(int i=0;i<N;++i) scanf("%d",&t[i]);
         solve();
      }
     // system("PAUSE");
      return 0;
}


