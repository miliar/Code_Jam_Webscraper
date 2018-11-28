#include <iostream>
#include <string.h>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
int n,m;
int map[65][65];
char ch[65];
struct node
{
	int x,y;

};
vector<node>a[15];
node temp;
int ok;
int xx,yy;
int f[65][65];
int index;
vector<node>tt;
int test[66][66];
bool OK()
{
	int i;
	int x,y;
	for (i=0;i<a[index].size();i++)
	{
		x=a[index][i].x;
		y=a[index][i].y;
		if (x!=xx||y!=yy)
			return false;
	}
	return true;
}
bool update()
{

	int i;
	int x,y;
	int k=0;
	for (i=0;i<a[index].size();i++)
	{
		x=a[index][i].x;
		y=a[index][i].y;
		if (x+1<n&&map[x+1][y]==-1)
			continue;
		k++;
		if (x+1<n&&test[x+1][y]!=1)
			return false;
		a[index][i].x++;
	}
	if (k==0)
		return false;
}
void update1(int s1,int s2)
{
	int i,j;
	int x,y;
	for (i=0;i<a[index].size();i++)
	{
		x=a[index][i].x;
		y=a[index][i].y;
		for (j=0;j<s1;j++)
			if (y-1>0&&map[x][y-1]!=-1)
				y--;
			else
				break;
		for (j=0;j<s2;j++)
			if (y+1<m&&map[x][y+1]!=-1)
				y++;
			else
				break;
		a[index][i].y=y;
	}
}
void update2(int s1,int s2)
{
	int i,j;
	int x,y;
	for (i=0;i<a[index].size();i++)
	{
		x=a[index][i].x;
		y=a[index][i].y;

		for (j=0;j<s1;j++)
			if (y+1<m&&map[x][y+1]!=-1)
				y++;
			else
				break;
		for (j=0;j<s2;j++)
			if (y-1>0&&map[x][y-1]!=-1)
				y--;
			else
				break;
		a[index][i].y=y;
	}
}
void check()
{
	if (ok==1)
		return;
	if (OK())
	{
		ok=1;
		return;
	}
	int x,y;
	int maxl=0,maxr=0;
	int i,j,k;
	for (i=0;i<a[index].size();i++)
	{
		k=0;
		x=a[index][i].x;
		y=a[index][i].y;
		while (y-1>0&&map[x][y-1]!=-1)
		{
			k++;
			y--;
		}
		maxl=max(maxl,k);
		k=0;
		x=a[index][i].x;
		y=a[index][i].y;
		while (y+1<m&&map[x][y+1]!=-1)
		{
			k++;
			y++;
		}
		maxr=max(maxr,k);
	}
	tt=a[index];
	for (i=0;i<=maxl;i++)
		for (j=0;j<=maxr;j++)
		{
			a[index]=tt;
			update1(i,j);
			if (OK())
			{
				ok=1;
				return;
			}
			if (update())
				check();
			a[index]=tt;
			update2(j,i);
			if (OK())
			{
				ok=1;
				return;
			}
			if (update())
				check();
		}
}
void dfs(int x,int y)
{
	f[x][y]=1;
	if (map[x][y]>=0)
		a[map[x][y]].push_back(temp);
	if (x+1<n&&f[x+1][y]==0&&map[x+1][y]!=-1)
		dfs(x+1,y);
	if (y+1<m&&f[x][y+1]==0&&map[x][y+1]!=-1)
		dfs(x,y+1);
	if (y-1>=0&&f[x][y-1]==0&&map[x][y-1]!=-1)
		dfs(x,y-1);
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,co=1,t;
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
		{
			scanf("%s",ch);
			for (j=0;j<m;j++)
			{
				if (ch[j]=='#')
					map[i][j]=-1;
				if (ch[j]=='.')
					map[i][j]=-2;
				if (ch[j]>='0'&&ch[j]<='9')
					map[i][j]=ch[j]-'0';
			}
		}
		for (i=0;i<10;i++)
			a[i].clear();
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				if (map[i][j]!=-1)
			{
				memset(f,0,sizeof(f));
				temp.x=i;
				temp.y=j;
				dfs(i,j);
			}
		printf("Case #%d:\n",co++);
		for (i=0;i<=9;i++)
		{
			xx=-1;
			yy=-1;
			for (j=0;j<n;j++)
				for (k=0;k<m;k++)
					if (map[j][k]==i)
					{
						xx=j;
						yy=k;
					}
			if (xx!=-1)
			{
				ok=0;
				printf("%d: %d ",i,a[i].size());
				memset(test,0,sizeof(test));
				for (j=0;j<a[i].size();j++)
					test[a[i][j].x][a[i][j].y]=1;
				index=i;
				check();
				if (ok==1)
					printf("Lucky\n");
				else
					printf("Unlucky\n");
			}
		}
	}
	return 0;
}
