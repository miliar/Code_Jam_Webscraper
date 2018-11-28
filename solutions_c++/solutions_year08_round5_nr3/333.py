#include<iostream>
using namespace std;
struct node
{
	int v,next;
}s[1000000];
int num[1<<10];
void back(int t,int x,int y)
{
	if(t==10)
	{
		num[x]=y;
	}
	else
	{
		back(t+1,x*2,y);
		back(t+1,x*2+1,y+1);
	}
}
char Mat[101][101];
int dp[15][1<<10];
int main()
{
	freopen("3.txt","r",stdin);
	
int mat[15];
int m,n;
int p[1<<10];
int a[1<<10];
	int index=0;
	for(int i=0;i<(1<<10);i++)
	{
		if(i&(i>>1))continue;
		if(i&(i<<1))continue;
		a[index++]=i;
	//	cout<<i<<endl;
	}
	back(0,0,0);
	int ind=0;
	memset(p,-1,sizeof(p));
	for(int i=0;i<index;i++)
	{
		for(int j=index-1;j>=0;j--)
		{
			if(a[i]&(a[j]<<1))continue;
			if(a[j]&(a[i]<<1))continue;
			s[ind].v=a[j];
			s[ind].next=p[a[i]];
			p[a[i]]=ind++;
		}
	}
	freopen("4.txt","w",stdout);

//	freopen("3.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	int g=1;
	while(zu--)
	{
		memset(mat,0,sizeof(mat));
		scanf("%d%d",&m,&n);
		for(int i=0;i<m;i++)
			scanf("%s",Mat[i]);
		for(int i=0;i<m;i++)
		{
			int x=0;
			for(int j=0;j<n;j++)
				if(Mat[i][j]=='.')
					x*=2;
				else
					x=x*2+1;
			mat[i+1]=x;

		}
		memset(dp,0,sizeof(dp));
		for(int i=0;i<index;i++)
		{
			if(mat[m] & a[i])continue;
			if(a[i]>=(1<<n))break;
			int x=a[i];
			dp[m][x]=num[x];
		}
		if(m==5&&n==3)
			printf("");
		for(int i=m;i>1;i--)
		{
			for(int j=0;j<index;j++)
			{
				int x=a[j];
				if(x>=(1<<n))break;
				for(int k=p[x];k!=-1;k=s[k].next)
				{
					int y=s[k].v;
					if(y>=(1<<n))break;
					if(mat[i-1]&y)continue;
					dp[i-1][y]=max(dp[i-1][y],dp[i][x]+num[y]);
				}
			}
		}
		/*if(m==5&&n==3){
		for(int i=1;i<=m;i++)
		{
			cout<<i<<endl;
			for(int j=0;j<index;j++)
			{
				if(a[j]>=(1<<n))break;
				cout<<a[j]<<":"<<dp[i][a[j]]<<" ";
			}
			cout<<endl;
		
		}
		for(int i=0;i<m;i++)
			cout<<Mat[i]<<endl;
		}*/
		int sum=0;
		for(int i=0;i<index;i++)
		{
			if(a[i]>=(1<<n))break;
			sum=max(sum,dp[1][a[i]]);
		}
		printf("Case #%d: ",g++);
		printf("%d\n",sum);
	}
}