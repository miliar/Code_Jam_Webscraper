#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

char mp[55][55];
int R,C;
char res[55][55];
bool vst[55][55];
int move[4][2]={0,0,0,1,1,0,1,1};

bool in(int x,int y)
{
	if(x<0||y<0||x>=R||y>=C)
		return false;
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A_2.out","w",stdout);
	int _,cases=1;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++)
			scanf("%s",mp[i]);
		memset(vst,0,sizeof(vst));
		bool ok=true;
		for(int i=0;i<R&&ok;i++)
		{
			for(int j=0;j<C&&ok;j++)
			{
				if(vst[i][j]) continue;
				if(mp[i][j]=='.') { res[i][j]='.'; continue; }
				int cX=i,cY=j;
				bool f=true;
				for(int d=0;d<4&&f;d++)
				{
					int nX=cX+move[d][0];
					int nY=cY+move[d][1];
					if(!in(nX,nY)) { f=false; break; }
					if(mp[nX][nY]!='#') { f=false; break; }
					if(vst[nX][nY]) { f=false; break; }
					vst[nX][nY]=true;
				}
				if(!f) ok=false;
				else
				{
					res[i][j]='/';
					res[i][j+1]='\\';
					res[i+1][j]='\\';
					res[i+1][j+1]='/';
				}
			}
			res[i][C]=0;
		}
		printf("Case #%d:\n",cases++);
		if(ok)
		{
			for(int i=0;i<R;i++)
				puts(res[i]);
		}
		else puts("Impossible");
	}
	return 0;
}