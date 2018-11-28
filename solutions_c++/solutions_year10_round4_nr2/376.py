#include<stdio.h>
#include<algorithm>
using namespace std;
int data[10000];
int group[20][10000];
long long mic[15][10000][15];
int time;
long long dd()
{
	int in,n,m,o;
	scanf("%d",&in);
	int d=1<<in;
	for(n=0;n<d;n++)
	{
		scanf("%d",&data[n]);
		data[n]=in-data[n];
	}
	for(n=1;n<=in;n++)
	{
		int bs=(1<<n);
		int lock=d/bs;
		for(m=0;m<lock;m++)
		{
			scanf("%d",&group[n][m]);
		}
	}
	for(n=0;n<15;n++)
		for(m=0;m<10000;m++)
			for(o=0;o<15;o++)
				mic[n][m][o]=1999999999;
	for(n=0;n<=in;n++)
	{
		int bs=(1<<n);
		int lock=d/bs;
		for(m=0;m<lock;m++)
		{
			if(n==0)
			{
				for(o=data[m];o<15;o++)
				{

					mic[n][m][o]=0;
					//printf("%d %d %d=%lld\n",n,m,o,mic[n][m][o]);
				}
			}
			else
			{
				for(o=0;o<15;o++)
				{
					if(o!=0)
						mic[n][m][o]=min(mic[n][m][o],mic[n][m][o-1]);
					mic[n][m][o]=min(mic[n][m][o],mic[n-1][m*2][o]+mic[n-1][m*2+1][o]);
					mic[n][m][o]=min(mic[n][m][o],mic[n-1][m*2][o+1]+mic[n-1][m*2+1][o+1]+group[n][m]);
					//printf("%d %d %d=%lld (%lld %lld %lld)\n",n,m,o,mic[n][m][o],mic[n][m][o-1],mic[n-1][m*2][o]+mic[n-1][m*2+1][o],mic[n-1][m*2][o+1]+mic[n-1][m*2+1][o+1]+group[n][m]);
				}
			}
		}
	}
	return mic[in][0][0];
}
int main()
{
	int in,n;
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		time=n+200;
		printf("Case #%d: %lld\n",n+1,dd());
	}
}
