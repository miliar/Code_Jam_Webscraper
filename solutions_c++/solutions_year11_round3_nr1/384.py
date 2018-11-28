#include <stdio.h>
#include <iostream>
using namespace std;
char ma[64][64];
int r,c,t;
void init()
{
	scanf("%d %d",&r,&c);
	for(int i=0;i<r;i++)scanf("%s",&ma[i]);
	return;
}
bool change1()
{
	for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
			if(ma[i][j]=='#')
			{
				if(i<r-1&&j<c-1&&ma[i+1][j]=='#'&&ma[i][j+1]=='#'&&ma[i+1][j+1]=='#')
				{
					ma[i][j]='/';
					ma[i][j+1]='\\';
					ma[i+1][j]='\\';
					ma[i+1][j+1]='/';
				}else return false;
			}
	return true;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(int tot=1;tot<=t;tot++)
	{
		init();
		printf("Case #%d:\n",tot);
		if(change1())
		{
			for(int i=0;i<r;i++)
			{
				printf("%s\n",ma[i]);
			}
		}else
			printf("Impossible\n");
	}
	return 0;
}
