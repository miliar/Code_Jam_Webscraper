#include<iostream>
#include<string>
#include<map>
char grid[55][55];
int N,K;
void rotate()
{
	char tmp[55][55];
	memset(tmp,'.',sizeof(tmp));
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			tmp[j][N-i-1]=grid[i][j];
		}
	}
	
	for(int k=0;k<N;k++)
	{
		for(int j=0;j<N;j++)
			for(int i=N-1;i>=1;i--)
			{
				if(tmp[i][j]=='.')
				{
					tmp[i][j]=tmp[i-1][j];
					tmp[i-1][j]='.';
				}
			}
	}
	memcpy(grid,tmp,sizeof(tmp));
}
bool calcR()
{
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)if(grid[i][j]=='R')
		{
			for(int dx=-1;dx<=1;dx++)for(int dy=-1;dy<=1;dy++)if(dx!=0||dy!=0)
			{
				int cnt=0;
				for(int k=0;k<K;k++)
				{
					if(i+dx*k<0||i+dx*k>=N||j+dy*k<0||j+dy*k>=N)break;
					if(grid[i+dx*k][j+dy*k]!='R')break;
					cnt++;
				}
				if(cnt==K)return true;
			}
		}
	return false;
}
bool calcB()
{
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)if(grid[i][j]=='B')
		{
			for(int dx=-1;dx<=1;dx++)for(int dy=-1;dy<=1;dy++)if(dx!=0||dy!=0)
			{
				int cnt=0;
				for(int k=0;k<K;k++)
				{
					if(i+dx*k<0||i+dx*k>=N||j+dy*k<0||j+dy*k>=N)break;
					if(grid[i+dx*k][j+dy*k]!='B')break;
					cnt++;
				}
				if(cnt==K)return true;
			}
		}
	return false;
}
int main ()
{
	int cases;
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		scanf("%d%d",&N,&K);
		bool R=false,B=false;
		for(int i=0;i<N;i++)
			scanf("%s",grid[i]);
		rotate();
		if(calcR())R=true;
		if(calcB())B=true;
		printf("Case #%d: ",cas);
		if(R&&B)printf("Both\n");
		else if(R)printf("Red\n");
		else if(B)printf("Blue\n");
		else printf("Neither\n");
	}
	return 0;
}