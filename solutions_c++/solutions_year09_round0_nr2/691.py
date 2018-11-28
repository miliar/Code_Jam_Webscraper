#include<iostream>
using namespace std;
struct node
{
	int v,next;
}s[1000000];
int p[10000];
int mp[100][100];
int mat[100][100];
int dx[5]={0,-1,0,0,1};
int dy[5]={0,0,-1,1,0};
int m,n;
inline bool check(int x,int y)
{
	if(x<0||y<0||x>=m||y>=n)return 1;
	return 0;
}
int v[10000];
int cc;
void dfs(int t)
{
	for(int i=p[t];i!=-1;i=s[i].next)
	{
		int u=s[i].v;
		if(v[u]>=0)continue;
		v[u]=cc;
		dfs(u);
	}
}
int dir[10000];
char ch[27];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	for(int ca=1;ca<=zu;ca++)
	{
		printf("Case #%d:\n",ca);
		scanf("%d%d",&m,&n);
		int index=0;
		for(int i=0;i<m;i++)for(int j=0;j<n;j++){scanf("%d",&mat[i][j]);mp[i][j]=index++;}
		int ind=0;
		memset(p,-1,index<<2);
		index=0;
		for(int i=0;i<m;i++)for(int j=0;j<n;j++,index++)
		{
			v[index]=-1;
			int low=mat[i][j];int f=0;
			int y=mp[i][j];
			int x=y;
			for(int k=1;k<=4;k++)
			{
				int tx=i+dx[k];
				int ty=j+dy[k];
				if(check(tx,ty))continue;
				if(mat[tx][ty]<low)
				{
					low=mat[tx][ty];
					f=k;
					x=mp[tx][ty];
				}
			}
			dir[index]=f;
			if(x==y)continue;
			s[ind].v=y;
			s[ind].next=p[x];
			p[x]=ind++;
		}
		cc=0;
		index=0;
		for(int i=0;i<m;i++)for(int j=0;j<n;j++,index++)
		{
			if(dir[index])continue;
			if(v[index]>=0)continue;
			v[index]=cc;
			dfs(index);
			cc++;
		}
		char ccc='a';
		memset(ch,-1,sizeof(ch));
		index=0;
		for(int i=0;i<m;i++)for(int j=0;j<n;j++,index++)
		{
			int zz=v[index];
			if(ch[zz]==-1)ch[zz]=ccc++;
		}
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
				printf("%c ",ch[v[mp[i][j]]]);
			puts("");
		}
	}
}
