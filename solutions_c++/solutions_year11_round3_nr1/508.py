#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


int main(int argc,char* argv[])
{
	//freopen("A-small.in","r",stdin);
	//freopen("A-small.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	int cas=1;
	scanf("%d",&T);
	int R,C;
	char str[100][100];
	while(T--)
	{
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++)
			scanf("%s",str[i]);

		bool flag=true;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if(str[i][j]=='#')
				{
					if((j+1<C&&str[i][j+1]=='#')&&(i+1<R&&str[i+1][j]=='#'&&str[i+1][j+1]=='#'))
					{
						str[i][j]='/';
						str[i][j+1]='\\';
						str[i+1][j]='\\';
						str[i+1][j+1]='/';
					}
					else
						flag=false;
				}
				if(!flag)
					break;
			}
			if(!flag)
				break;
		}
		printf("Case #%d:\n",cas++);
		if(flag)
		{
			for(int i=0;i<R;i++)
				printf("%s\n",str[i]);
		}
		else
			printf("Impossible\n");

	}

	return 0;
}
