#include <cstdlib>      
#include <cstring>      
#include <memory>      
#include <cstdio>      
#include <fstream>      
#include <iostream>      
#include <cmath>      
#include <string>      
#include <sstream>      
#include <stack>      
#include <queue>      
#include <vector>      
#include <set>      
#include <map>      
#include <algorithm>      
#include <deque>      
#include <list>      
#include <complex> 
using namespace std;  
const int dir[4][2]={
{1,0},{0,1},{-1,1},{1,1}};
const char *S[]={"Red",
	"Neither","Blue","Both"};
char a[55][55],u[55][55];
int n, k;
bool ok(int x,int y)
{
	return (x>=0&&x<n&&y>=0&&y<n);
}
bool dfs(int x,int y,int k,int di)
{
	if(k==1) return 1;
	int xx = x + dir[di][0];
	int yy = y + dir[di][1];
	if(ok(xx,yy)&&a[xx][yy]==a[x][y])
		if(dfs(xx,yy,k-1,di)) return 1;
		else return 0;
	return 0;

}
int main ( )
{
	int tCase;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d", &tCase);
	for(int t = 1; t <= tCase; t++)
	{
		printf("Case #%d: ", t);
		int  rflag = 0, bflag = 0;
		scanf("%d%d", &n, &k);
		for(int i = 0; i < n; i++)
			scanf("%s", a[i]);
		for(int i = 0; i < n; i++)
			for(int j = n - 1; j >= 0; j--)
				if(a[i][j]=='.') 
					for(int k = j - 1; k >= 0; k--)
						if(a[i][k]!='.')
						{
							a[i][j] = a[i][k];
							a[i][k] = '.';
							break;
						}
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				if(a[i][j]=='R'&&!rflag)
				{
					for(int kl = 0; kl < 4; kl++)
						if(dfs(i,j,k,kl)) 
						{
							rflag = 1;
							break;
						}
				}
				else if(a[i][j]=='B'&&!bflag)
				{
					for(int kl = 0; kl < 4; kl++)
						if(dfs(i,j,k,kl)) 
						{
							bflag = 1;
							break;
						}
				}
				else if(rflag && bflag)
					break;
		if(rflag && bflag) printf("%s\n",S[3]);
		else if(rflag) printf("%s\n",S[0]);
		else if(bflag) printf("%s\n",S[2]);
		else printf("%s\n", S[1]);

	}
	return 0;
}
