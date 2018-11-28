#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define i64 __int64
#define inf 1000000000

const double eps = 1e-11;

#define MAX 102
#define MAX1 6405

int cases,caseno,P[MAX1],N;
int gr[MAX][MAX],K[MAX][MAX];
char a[MAX][MAX];

int cnt=0;

vector <int> adj[MAX1];

int move[6][2]={0,-1,0,1,-1,-1,-1,1,1,-1,1,1};
int m,n;

inline int valid(int i,int j)
{
	if(i>=0 && i<m && j>=0 && j<n)
	{
		return gr[i][j];
	}
	return -1;
}

void call(int i,int j,int col)
{
	int k,x,y,res;

	gr[i][j]=col;

	for(k=0;k<6;k++)
	{
		x=i+move[k][0];
		y=j+move[k][1];

		res=valid(x,y);

		if(res==col)
		{
			while(1);
		}
		if(res==0)
		{
			call(x,y,col%2+1);
		}
	}
}

void input()
{
	int i,j;

	CLR(gr);
	N=0;
	cnt=0;
	scanf("%d %d",&m,&n);
	for(i=0;i<m;i++) scanf("%s",a[i]);
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if(a[i][j]=='x')
			{
				cnt++;
				gr[i][j]=-1;
			}
		}
	}
	for(i=m-1;i>=0;i--)
	{
		for(j=0;j<n;j++)
		{
			if(gr[i][j]==0)
			{
				call(i,j,1);
			}
		}
	}
	int k=0;

	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if(gr[i][j]>0)
			{
				K[i][j]=k++;
			}
			else
				K[i][j]=-1;
		}
	}
	for(i=0;i<k;i++) adj[i].clear();

	N=0;
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if(K[i][j]>=0)
			{
				k=K[i][j];
				if(gr[i][j]==1)
				{
					int x,y,l;

					P[N++]=k;
					for(l=0;l<6;l++)
					{
						x=i+move[l][0];
						y=j+move[l][1];

						if(valid(x,y)>0) adj[k].push_back(K[x][y]);
					}
				}
			}
		}
	}
}

void print()
{
	int i,j;

	puts("");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d ",gr[i][j]);
		}
		puts("");
	}
}

int Left[MAX1],Right[MAX1];
bool visited[MAX1];

/* Given a graph m left nodes and n right nodes */

bool bpm(int u)
{
    int v,k;

    for(k=0;k<adj[u].size();k++)
	{
		v=adj[u][k];
		if(visited[v]) continue;
		visited[v]=true;
		if(Right[v]==-1 || bpm(Right[v]))
		{
			Left[u]=v;
			Right[v]=u;
			return true;
		}
    }
    return false;
}

void process()
{
	printf("Case #%d: ",++caseno);
	int Count,i;

    memset(Left,-1,sizeof(Left));
    memset(Right,-1,sizeof(Right));
    Count=0;
    for(i=0;i<N;i++) {
		memset(visited,0,sizeof(visited));
		if(bpm(P[i])) Count++;
    }
	printf("%d\n",m*n-Count-cnt);
}

int main()
{
	freopen("Inputs\\c.in","r",stdin);
	freopen("Inputs\\c2.txt","w",stdout);

	scanf("%d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}
