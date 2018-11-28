#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

char c[1000];
int a[1000];
char s[1000];
char bit[50][50];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Al.out","w",stdout);
	int i,j,l,t;
	int line,col;
	char tmp;
	scanf("%d",&t);
	bool possibility;
	for (l=0;l<t;l++)
	{
		possibility=true;
		scanf("%d",&line);
		scanf("%d\n",&col);
		for (i=0;i<line;i++)
		{
			for(j=0;j<col;j++)
			{
				scanf("%c",&bit[i][j]);
			}
			scanf("\n");
		}

//==============process============
		for(i=0;i<line;i++)
		{
			for(j=0;j<col;j++)
			{
				if(bit[i][j]=='#')
				{
					if(i==line-1||j==col-1)
					{
						possibility=false;
						break;
					}
					if(bit[i][j+1]=='#' && bit[i+1][j]=='#' && bit[i+1][j+1]=='#')
					{
						bit[i][j]=bit[i+1][j+1]='/';
						bit[i+1][j]=bit[i][j+1]='\\';
					}
					else
					{
						possibility=false;
						break;
					}
				}
				if(!possibility) break;
			}
		}
		
			printf("Case #%d:\n",l+1);
			if(!possibility)
				printf("Impossible\n");
			else
			{
				for(i=0;i<line;i++)
				{
					for(j=0;j<col;j++)
						printf("%c",bit[i][j]);
					printf("\n");
				}
			}
	}
	return 0;
}