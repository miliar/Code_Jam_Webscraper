#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
int mat[2000][2000];
int pow2(int n)
{
	return 1<<n;
}
void allp(int x,int y)// x y的根加1
{
	int s;int i,j,k;
	s=y*pow2(x);
	for(i=s;i<s+pow2(x);i++)
	{
		mat[0][i]--;
	}

}
int allok(int x,int y)// x y的根加1
{
	int s;int i,j,k;
	s=y*pow2(x);
	for(i=s;i<s+pow2(x);i++)
	{
		if(mat[0][i]>=0) return 0;
	}
	return 1;
}
int cnt=0;
void deep(int x,int y,int n)
{
	//printf("<%d,%d,%d>",x,y,n);
	int i,j,k;
	if(x==0 ) return ;

	if(allok(x,y)) return ;
	allp(x,y);
	cnt++;

	for(i=y;i<y+n;i++)
	{
		deep(x-1,y*2+i,n*2);
	}
	//deep(x-1,y*2);
}
int main()
{
	int n;
	int m;
	int i,j,k;
	int cas;
	freopen("c:\\x6.txt","r",stdin);
	freopen("c:\\x7.txt","w",stdout);
	scanf("%d",&cas);
	for(int  x=1;x<=cas;x++)
	{
	scanf("%d",&n);
	m=1<<n;
	for(i=0;i<n+1;i++)
	{
		for(j=0;j<  pow2(n-i);j++)
		{
			scanf("%d",&mat[i][j]);
		}
	}
	for(i=0;i<1<<n;i++)
	{
		mat[0][i]=n-mat[0][i];
	}
	cnt=0;
	deep(n,0,1);
	printf("Case #%d: %d\n",x,cnt);
	}
	/*for(i=0;i<n+1;i++)
	{
		for(j=0;j< (  1<<(n-i) );j++)
		{
			printf("<%d>",mat[i][j]);
		}
		printf("\n");
	}*/

	return 0;
}