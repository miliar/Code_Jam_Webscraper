#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int T;
int R,C,D;
char w[505][505];

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-1.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		scanf("%d%d%d\n",&R,&C,&D);
		for(int i=0;i<R;i++)
			gets(w[i]);
		int ans=0;
		bool flag=false;
		for(ans=min(R,C);ans>=3&&!flag;ans--)
		{
			for(int x0=0;x0<=R-ans&&!flag;x0++)
				for(int y0=0;y0<=C-ans&&!flag;y0++)
				{
					int sum=0;
					int tmpx=0;
					int tmpy=0;
					for(int i=0;i<ans;i++)
						for(int j=0;j<ans;j++)
						{
							if((i==0||i==ans-1)&&(j==0||j==ans-1))
								continue;
							tmpx+=(i)*w[x0+i][y0+j];
							tmpy+=(j)*w[x0+i][y0+j];
							sum+=w[x0+i][y0+j];
						}
					if(tmpx*2==(ans-1)*sum&&tmpy==tmpx)
					{
						flag=true;
						printf("%d\n",ans);
					}
				}
		}
		if(!flag)
			puts("IMPOSSIBLE");
	}
	return 0;
}
