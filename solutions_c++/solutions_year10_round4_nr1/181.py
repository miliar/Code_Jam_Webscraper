#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<time.h>
using namespace std;
#define M 300 
char cchar[M*3];
char c[M*3][M*3];
bool used[M*3][M*3];

struct data{
	int x,y,val;
};
bool limit(int x,int y,int n)
{
	int i,j;
	for(i=M-n;i<=M+n;i++)
		for(j=M-n;j<=M+n;j++)
			if(c[i][j]!=' ')
			{
				if(c[i][y*2-j]!=' '&&c[i][y*2-j]!=c[i][j])
					return false;
				if(c[x*2-i][j]!=' '&&c[x*2-i][j]!=c[i][j])
					return false;
			}
	return true;
}
int dx[4]={1,-1,0,0},dy[4]={0,0,1,-1};
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a1.out","w",stdout);
	int cas,i,j,n,dd;
	queue<data> q;
	data now,t;
    cin>>cas;
	for(dd=1;dd<=cas;dd++)
	{
		memset(c,' ',sizeof(c));
		memset(used,0,sizeof(used));
		scanf("%d",&n);
		while(!q.empty())
			q.pop();
		gets(cchar);
		for(i=n-1;i>=0;i--)
		{
			gets(cchar);
			for(j=0;cchar[j];j++)
				c[M-i][M+j-n+1]=cchar[j];
		}
		for(i=1;i<n;i++)
		{
			gets(cchar);
			for(j=0;cchar[j];j++)
				c[M+i][M+j-n+1]=cchar[j];
		}
		used[now.x=M][now.y=M]=true;
		now.val=0;
		q.push(now);
		while(!q.empty())
		{
			now=q.front();
			q.pop();
			if(limit(now.x,now.y,n))
				break;
			for(i=0;i<4;i++)
			{
				t.x=now.x+dx[i];
				t.y=now.y+dy[i];
				t.val=now.val+1;
				if(used[t.x][t.y])
					continue;
				used[t.x][t.y]=true;
				q.push(t);
			}
		}
		printf("Case #%d: %d\n",dd,(n+now.val)*(n+now.val)-n*n);
	}
}

