#include <iostream>
using namespace std;
int a[110][20][2];
int k[110];
int main()
{

	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);

	int T,Ti;
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<m;i++)
		{
			scanf("%d",&k[i]);
			for(int j=0;j<k[i];j++)
			{
				scanf("%d%d",&a[i][j][0],&a[i][j][1]);
			}
		}


		printf("Case #%d: ",Ti);
		int result=-1;
		int cresult=1<<30;
		for(int i=0;i<(1<<n);i++)
		{
			int flag=1;
			for(int j=0;j<m;j++)
			{
				int tflag=0;
				for(int t=0;t<k[j];t++)
				{
					if(((i & (1<<(a[j][t][0]-1)))?1:0) == a[j][t][1]) tflag = 1;
				}
				if(!tflag) flag=0;
				if(flag==0) break;					
			}
			if(flag==1)
			{
				int tcount=0;
				for(int j=0;j<n;j++) if(i & (1<<j)) tcount++;
				if(tcount<cresult)
				{
					result = i;
					cresult=tcount;
				}
			}
		}
		if(result>=0) goto scat;

		puts("IMPOSSIBLE");
		continue;
scat:
		for(int i=0;i<n-1;i++)
			printf("%d ",(result & (1<<i))?1:0);
		printf("%d\n",(result & (1<<(n-1)))?1:0);
	}
}