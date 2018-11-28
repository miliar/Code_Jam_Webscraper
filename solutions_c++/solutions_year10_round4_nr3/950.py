#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
using namespace std;
struct mt
{
	int data[245][245];
	int end()
	{
		int i,j,k;
		for(i=1;i<240;i++)
			for(j=1;j<240;j++)
			{
				if(data[i][j]==1) return 0;
			}
		return 1;
	}
	/*void prt()
	{
		int i,j,k;
		for(i=1;i<20;i++)
		{
			for(j=1;j<20;j++)
				printf("%d",data[i][j]);
			printf("\n");
		}
		printf("\n");
	}*/
}mat;
void set(struct mt &x,int a,int b,int c,int d)
{
	int i,j,k;
	for(i=a;i<=c;i++)
	{
		for(j=b;j<=d;j++)
		{
			x.data[i][j]=1;
		}
	}
}
int okay(struct mt &a,int x,int y)
{
	if(x<=0) return 0;
	if(y<=0) return 0;
	//if(x>=200) return 0;
	//if(y>=200) return 0;
	if(a.data[x][y]==1) return 1;
	return 0;
}
mt next(mt x)
{
	int i,j,k;
	//printf("x-1\n");
	mt res=x;
	//printf("x\n");
	//memset(res.data,0,sizeof(res.data));
	for(i=1;i<240;i++)
		for(j=1;j<240;j++)
		{
			if(okay(x,i-1,j)==0&&okay(x,i,j-1)==0 )
				res.data[i][j]=0;
		}
	//printf("y\n");
	for(i=1;i<240;i++)
		for(j=1;j<240;j++)
		{
			if(okay(x,i-1,j)==1&&okay(x,i,j-1)==1 )
				res.data[i][j]=1;
		}
	//printf("z\n");
	return res;
}

int main()
{

	//memset(mat,0,sizeof(mat));
	freopen("c:\\x1.txt","r",stdin);
	freopen("c:\\x3.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	printf("%d",cas);
	for(int x=1;x<=cas;x++)
	{
	memset(mat.data,0,sizeof(mat.data));
	int i,j,k;
	int n;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		int a,b,c,d;
		scanf("%d%d%d%d",&a,&b,&c,&d);
		set(mat,a,b,c,d);
	}
	for(i=0;;i++)
	{
		//mat.prt();
		if(mat.end()) break;
		//printf("a\n");
		mat=next(mat);
		//printf("b\n");
		//getchar();

	}
	printf("Case #%d: %d\n",x,i);
	}
	return 0;
}