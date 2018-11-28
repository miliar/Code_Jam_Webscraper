#include<iostream>
#include<string>
using namespace std;

int color[600][600],vis[600][600];
int num[600];

bool cut(int sx,int sy,int len)
{
	for(int i=0;i<len;i++)for(int j=0;j<len;j++)
	{
		int x=sx+i;
		int y=sy+j;
		if(vis[x][y]) return 0;
	}

	for(int i=0;i<len;i++)for(int j=0;j<len;j++)
	{
		int x=sx+i;
		int y=sy+j;
		if(x>sx&&color[x][y]==color[x-1][y]) return 0;
		if(y>sy&&color[x][y]==color[x][y-1]) return 0;
	}

	for(int i=0;i<len;i++)for(int j=0;j<len;j++)
	{
		int x=sx+i;
		int y=sy+j;
		vis[x][y]=1;
	}
	return 1;
}

int get(char c)
{
	if(c>='0'&&c<='9') return c-'0';
	else return c-'A'+10;
}

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t;
	int cas=1;
	cin>>t;
	while(t--)
	{
		int n,m;
		cin>>n>>m;
		string s;
		memset(color,0,sizeof(color));
		memset(vis,0,sizeof(vis));
		for(int i=0;i<n;i++)
		{
			cin>>s;
			for(int j=0;j<m/4;j++)
			{
				int v=get(s[j]);
				for(int k=0;k<4;k++)
				{
					if(v&(1<<k)) color[i][j*4+3-k]=1;
				}
			}
		}


		int size=min(n,m);
		memset(num,0,sizeof(num));
		for(int len=size;len>=2;len--)
		{
			for(int i=0;i+len<=n;i++)for(int j=0;j+len<=m;j++)
			{
				if(cut(i,j,len))
				{
					num[len]++;
				}
			}
		}

		int tot=0;
		for(int i=2;i<=size;i++)
			tot+=i*i*num[i];

		num[1]=n*m-tot;

		int ge=0;
		for(int i=1;i<=size;i++)
		{
			if(num[i]>0) ge++;
		}

		cout<<"Case #"<<cas++<<": "<<ge<<'\n';
		for(int i=size;i>0;i--)
		{
			if(num[i]>0) cout<<i<<' '<<num[i]<<'\n';
		}

	}
	return 0;
}