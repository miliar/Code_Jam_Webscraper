#include <iostream>
using namespace std;
const int maxn=1000+5;
unsigned int g[maxn];
int main()
{
    //freopen("test.txt","r",stdin);freopen("3.txt","w",stdout);
    freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	int t,n,r,k;
	scanf("%d",&t);
	for (int caseId=1;caseId<=t;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d%d%d",&r,&k,&n);
		//printf("\n%d,%d,%d\n",r,k,n);
		for(int i=1;i<=n;i++)
            scanf("%d",&g[i]);
        int p=1;
        int out=0;
        for(int i=0;i<r;i++)
        {
            unsigned int w=k;
            int tag=0;
            while(w>=g[p]&&tag<n)
            {
                out+=g[p];
                w-=g[p];
                if(p==n)
                    p=1;
                else
                    p++;
                tag++;
            }
        }
        printf("%d\n",out);
		fflush(stdout);
	}
	return 0;
}
