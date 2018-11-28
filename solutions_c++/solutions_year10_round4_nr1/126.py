#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
using namespace std;
#define MAX 400
char c[MAX*2][MAX*2];
bool used[MAX*2][MAX*2];
char cc[MAX*2];
struct data{
	int x,y,val;
};
bool check(int x,int y,int n)
{
	int i,j;
	for(i=MAX-n;i<=MAX+n;i++)
		for(j=MAX-n;j<=MAX+n;j++)
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
	int cs,i,j,n,dd;
	queue<data> q;
	data now,t;
	scanf("%d",&cs);
	for(dd=1;dd<=cs;dd++)
	{
		memset(c,' ',sizeof(c));
		memset(used,0,sizeof(used));
		scanf("%d",&n);
		gets(cc);
		for(i=n-1;i>=0;i--)
		{
			gets(cc);
			for(j=0;cc[j];j++)
				c[MAX-i][MAX+j-n+1]=cc[j];
		}
		for(i=1;i<n;i++)
		{
			gets(cc);
			for(j=0;cc[j];j++)
				c[MAX+i][MAX+j-n+1]=cc[j];
		}
		while(!q.empty())
			q.pop();
		used[now.x=MAX][now.y=MAX]=true;
		now.val=0;
		q.push(now);
		while(!q.empty())
		{
			now=q.front();
			q.pop();
			if(check(now.x,now.y,n))
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
