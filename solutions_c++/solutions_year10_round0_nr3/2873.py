#include <iostream>
using namespace std;
const int maxn=1001;
unsigned int g[maxn];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	int T,N,R,K;
	scanf("%d",&T);
	for (int num=1;num<=T;num++)
	{
		printf("Case #%d: ",num);
		scanf("%d%d%d",&R,&K,&N);
		for(int i=1;i<=N;i++)
            scanf("%d",&g[i]);
        int p=1;
        int sum=0;
        for(int i=0;i<R;i++)
        {
            unsigned int w=K;
            int tag=0;
            while(w>=g[p]&&tag<N)
            {
                sum+=g[p];
                w-=g[p];
                if(p==N)
                    p=1;
                else
                    p++;
                tag++;
            }
        }
        printf("%d\n",sum);
		fflush(stdout);
	}
	return 0;
}
