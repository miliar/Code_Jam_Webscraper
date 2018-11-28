#include<cstdio>
#include<vector>
#include<algorithm>
#define MAXN 128
using namespace std;
int T,P,Q;
int A[MAXN];
bool F[MAXN];
int main()
{
    int i,j,k;
    scanf("%d",&T);
    for(k=0;k<T;++k)
    {
        scanf("%d %d",&P,&Q);
        for(i=0;i<Q;++i)
        {
            scanf("%d",&A[i]);
            --A[i];
        }
        sort(A,A+Q);
        int ans=INT_MAX,crnt;
        do
        {
            for(j=0;j<P;++j)F[j]=true;
            crnt=0;
            for(i=0;i<Q;++i)
            {
                F[A[i]]=false;
                for(j=A[i]-1;j>=0;--j)
                {
                    if(!F[j])break;
                    ++crnt;
                }
                for(j=A[i]+1;j<P;++j)
                {
                    if(!F[j])break;
                    ++crnt;
                }
            }
            ans=min(ans,crnt);
        }while(next_permutation(A,A+Q));
        printf("Case #%d: %d\n",k+1,ans);
    }
    return 0;
}
