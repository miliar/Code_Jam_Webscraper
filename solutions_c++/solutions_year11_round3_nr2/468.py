#include <cstdio>
using namespace std;

int L,t,N,C;
int A[1002],S[1002];
int main ()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int z=1;z<=T;++z)
    {
    scanf("%d %d %d %d",&L,&t,&N,&C);
    printf("Case #%d: ",z);
    for (int i=0;i<C;++i) scanf("%d",&A[i]);
    S[0]=0;
    for (int i=1;i<=N;++i) S[i]=S[i-1]+A[(i-1)%C];
    if (!L) printf("%d\n",2*S[N]);
    else if (L==1 || N==1)
    {
         int cnt=0;
         int bst=2000000000;
         for (int i=0;i<N;++i)
         {
             cnt=2*S[i];
             if (cnt>=t) cnt+=A[i%C]+2*(S[N]-S[i+1]);
             else cnt+=(t-cnt)/2+A[i%C]+2*(S[N]-S[i+1]);
             if (bst>cnt) bst=cnt;
         }
         printf("%d\n",bst);
    }
    else
    {
         int cnt=0;
         int bst=2000000000;
         for (int i=0;i<N-1;++i)
         {
             cnt=2*S[i];
             if (cnt>=t) cnt+=A[i%C];
             else cnt+=(t-cnt)/2+A[i%C];
             for (int j=i+1;j<N;++j)
             {
                 int tmp=2*(S[j]-S[i+1]);
                 if (cnt+tmp>=t) tmp+=A[j%C]+2*(S[N]-S[j+1]);
                 else tmp+=(t-cnt-tmp)/2+A[j%C]+2*(S[N]-S[j+1]);
                 if (bst>cnt+tmp) bst=cnt+tmp;
             }
         }
         printf("%d\n",bst);
    }
    }
    return 0;
}
