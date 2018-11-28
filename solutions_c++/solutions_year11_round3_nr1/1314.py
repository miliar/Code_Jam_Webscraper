
#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;
char p[55][55];
bool cantrans(int x,int y){
	if(p[x][y]=='#'&& p[x+1][y]=='#'&& p[x][y+1]=='#'&& p[x+1][y+1]=='#')
	{
		p[x][y]='/';
		p[x+1][y]='\\';
		p[x][y+1]='\\';
		p[x+1][y+1]='/';
		return true;
	}
	return false;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("tt.out","w",stdout);
	int T,r,c,cases=1;
	cin >>T;
	while (T--)
	{
		cin >>r>>c;
		int ret=1;
		for(int i=0;i<r;i++)
			scanf("%s",&p[i]);
		for(int i=0;i<r-1;i++)
			for(int j=0;j<c-1;j++)
			{
				if(p[i][j]=='#')
				{
					if(!cantrans(i,j))
						ret=0;
				}
			}
			for(int i=0;i<r;i++) if(p[i][c-1]=='#') ret=0;
			for(int j=0;j<c;j++) if(p[r-1][j]=='#') ret=0;
			cout <<"Case #"<<cases++<<":"<<endl;
			if(ret)
				for(int i=0;i<r;i++)
					printf("%s\n",p[i]);
			else
				cout <<"Impossible"<<endl;
	}
	return 0;
}