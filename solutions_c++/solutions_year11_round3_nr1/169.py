#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int row,cul;
const int size=55,inf=1<<26;
char mat[size][size];

bool check(int x,int y)
{
	return x>=0&&x<row&&y>=0&&y<cul;
}

bool check_ok(int x,int y)
{
	if(!check(x,y)||mat[x][y]!='#')
		return false;
	if(!check(x+1,y)||mat[x+1][y]!='#')
		return false;
	if(!check(x,y+1)||mat[x][y+1]!='#')
		return false;
	if(!check(x+1,y+1)||mat[x+1][y+1]!='#')
		return false;
	return true;
}

int main()
{
	int t,e=1;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d",&t);
	while(t--)
	{
		int i,j;
		bool ans=true;

		scanf("%d%d",&row,&cul);

		for(i=0;i<row;i++)
			scanf("%s",mat[i]);

		for(i=0;i<row&&ans;i++)
			for(j=0;j<cul&&ans;j++)
				if(mat[i][j]=='#')
				{
					if(check_ok(i,j))
					{
						mat[i][j]=mat[i+1][j+1]='/';
						mat[i+1][j]=mat[i][j+1]='\\';
					}
					else ans=false;
				}
		printf("Case #%d:\n",e++);
		if(!ans)
			printf("Impossible\n");
		else for(i=0;i<row;i++)
			puts(mat[i]);
	}
	return 0;
}