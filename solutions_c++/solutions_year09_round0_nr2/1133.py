#include <iostream>
#include<fstream>
#include <string>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include<math.h>
#include<sstream>
#include <algorithm>
using namespace std;
//ofstream fo("G:\\ASmallAns.txt",ios_base::out);
int t,h,w;
int area[102][102],temp[102][102];
char ans[102][102];
void find(int x,int y,char ch)
{
	if (ans[x][y]!='*')
		return;
	ans[x][y]=ch;
	if (temp[x][y]==1)
	{
		find(x-1,y,ch);
	}
	if (temp[x][y]==2)
	{
		find(x,y-1,ch);
	}
	if (temp[x][y]==3)
	{
		find(x,y+1,ch);
	}
	if (temp[x][y]==4)
	{
		find(x+1,y,ch);
	}

	if ((x+1<h)&&temp[x+1][y]==1)
		find(x+1,y,ch);

	if ((y+1<w)&&temp[x][y+1]==2)
		find(x,y+1,ch);

	if ((y-1>=0)&&temp[x][y-1]==3)
		find(x,y-1,ch);

	if ((x-1>=0)&&temp[x-1][y]==4)
		find(x-1,y,ch);
	return;
}
int main()
{
	int i,j,k,s,n;
	char ch;
	//ofstream fo("G:\\BSmallAns.txt",ios_base::out);


	scanf("%d",&t);
	for (n=1;n<=t;n++)
	{
		scanf("%d%d",&h,&w);
		k=0;
		for (i=0;i<h;i++)
			for (j=0;j<w;j++)
			{
				scanf("%d",&area[i][j]);
				temp[i][j]=0;
			}
		for (i=0;i<h;i++)
			for (j=0;j<w;j++)
			{
				s=0;k=area[i][j];
				if ((i-1>=0)&&area[i-1][j]<k)
				{
					s=1;k=area[i-1][j];
				}

				if ((j-1>=0)&&area[i][j-1]<k)
				{
					s=2;k=area[i][j-1];
				}

				if ((j+1<w)&&area[i][j+1]<k)
				{
					s=3;k=area[i][j+1];
				}

				if ((i+1<h)&&area[i+1][j]<k)
				{
					s=4;k=area[i+1][j];
				}
				
				temp[i][j]=s;
				ans[i][j]='*';
			}
		ch = 'a';
		for (i=0;i<h;i++)
			for (j=0;j<w;j++)
				if (ans[i][j]=='*')
				{
					find(i,j,ch);
					ch=char(ch+1);
				}
		//fo<<"Case #"<<n<<":"<<endl;
		printf("Case #%d:\n",n);
		for (i=0;i<h;i++)
		{
			for (j=0;j<w-1;j++)
				//fo<<ans[i][j]<<' ';
				printf("%c ",ans[i][j]);
			//fo<<ans[i][w-1]<<endl;
			printf("%c\n",ans[i][w-1]);
		}
		
	}

	return 0;
}