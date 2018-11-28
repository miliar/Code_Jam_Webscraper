#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<math.h>
#include<cmath>
#define eps 1e-11
#define INF (2<<31)-1
#define siz 500000

using namespace std;

int max(int a, int b) {
	if(a>b) return a;
	return b;
}
int min(int a, int b){
	if(a<b) return a;
	return b;
}

int gcd(int a, int b)
{
	int c;
	if(a==b)
		return b;
	while(a>0)
	{
		c=b%a;
		b=a;
		a=c;
	}
	return b;
}

vector<int> adj[siz];
int t, n, m, a, b,  ct=1;
int r, c;
char row[100][100];
int col[100][100];
int done[100][100];
char yy;

int main()
{
	freopen("al.in","r",stdin);
	freopen("out4.txt","w",stdout);
	int i, j, res;
	scanf("%d", &t);
	while(t--)
	{
		memset(col, 0, sizeof(col) );
		memset(done, -1, sizeof(done) );
		scanf("%d %d", &r, &c);
		for(i=0;i<r;i++)
		{
			scanf("%s", &row[i]);
			for(j=0;j<c;j++)
			{
				if(row[i][j]=='.')
					col[i][j]=1;
				else
					col[i][j]=2;
			}
		}
		yy=92;
		res=0;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(j==c-1 && col[i][j]==2)
				{
					res=-1;
					break;
				}
				if(i==r-1 && col[i][j]==2)
				{	
					res=-1;
					break;
				}
				if(col[i][j]==2 && col[i][j+1]==2 && col[i+1][j]==2 && col[i+1][j+1]==2)
				{
					if(done[i][j]!=ct && done[i][j+1]!=ct && done[i+1][j]!=ct && done[i+1][j+1]!=ct)
					{
						col[i][j]=3;
						col[i][j+1]=3;
						col[i+1][j]=3;
						col[i+1][j+1]=3;
						done[i][j]=ct;
						done[i][j+1]=ct;
						done[i+1][j]=ct;
						done[i+1][j+1]=ct;
						
						row[i][j]='/';
						
						row[i][j+1]=yy;
						
						row[i+1][j]=yy;
						
						row[i+1][j+1]='/';
					}
				}
				else if(col[i][j]==1 || done[i][j]==ct)
				{
					done[i][j]=ct;
				}
				else
				{
					res=-1;
				}
				
			}
		}
		printf("Case #%d:\n", ct++);
		if(res==-1)
		{
			printf("Impossible\n");
		}
		else
		{
			for(i=0;i<r;i++)
			{
				printf("%s\n", row[i]);
			}
		}
		
		
	}
	
	return 0;
	
}
