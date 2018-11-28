#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
using namespace std;

int T;
int r[1005];
int x[1005];
int y[1005];
int N;
int W;
int L;

bool in(int i,int j)
{
	long long t=(r[i]+r[j]);
	t*=t;
	long long X=x[i]-x[j];
	X*=X;
	long long Y=y[i]-y[j];
	Y*=Y;
	return (X+Y<t);
}

int main()
{
	srand(time(0));
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		scanf("%d%d%d",&N,&W,&L);
		for(int i=0;i<N;i++)
		{
			scanf("%d",&r[i]);
		}
		for(int i=0;i<N;i++)
		{
			while(1)
			{
				x[i]=rand()%(W+1);
				y[i]=rand()%(L+1);
				bool flag=false;
				for(int j=0;j<i;j++)
					if(in(i,j))
					{
						flag=true;
						break;
					}
				if(!flag)
					break;
			}
		}
		printf("Case #%d:",test);
		for(int i=0;i<N;i++)
			printf(" %d %d",x[i],y[i]);
		puts("");
	}
	return 0;
}

