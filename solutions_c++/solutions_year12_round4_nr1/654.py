#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<fstream>
#include<string>
using namespace std;
const int MAXN=20000;
int T;
int D,N;
int Di[MAXN],Li[MAXN];
void solve(int num)
{
	scanf("%d",&N);
	for(int i=1;i<=N;i++)
	scanf("%d%d",&Di[i],&Li[i]);
	scanf("%d",&D);
	int nowLen=Di[1];
	int far=0;
	int gofar=-1;
	for(int i=1;i<N;)
	{
		far=-1;
		gofar=-1;
		for(int j=i+1;j<=N;j++)
		{
			if(Di[i]+nowLen<Di[j])
			break;
			if(Di[j]+min(Di[j]-Di[i],Li[j])>gofar)
			{
				gofar=Di[j]+min(Di[j]-Di[i],Li[j]);
				far=j;
			}
		}
		if(far==-1)
		{
			printf("Case #%d: NO\n",num);
			return ;
		}
		nowLen=min(Di[far]-Di[i],Li[far]);
		i=far;
		if(Di[i]+nowLen>=D)
		{
			printf("Case #%d: YES\n",num);
			return ;			
		}
	}
	if(Di[N]+nowLen>=D)
	printf("Case #%d: YES\n",num);
	else
	printf("Case #%d: NO\n",num);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	solve(i);
	return 0;
}