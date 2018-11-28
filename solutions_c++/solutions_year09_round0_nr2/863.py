#include<stdio.h>

int h[201][201];
int p[201][201];
int father[20001];
char u[20001];
int ntest,n,m;

int ff(int x)
{
	if(father[x]==x) return x;
	else return father[x] = ff(father[x]);
}

const int dx[] = {-1,0,0,1};
const int dy[] = {0,-1,1,0};

int main()
{
	scanf("%d",&ntest);
	for(int test = 1; test <= ntest; test++)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				scanf("%d",&h[i][j]);
				p[i][j] = i*m+j;
				u[i*m+j] = 0;
				father[i*m+j] = i*m+j;
			}
		for(int x=0;x<n;x++)
			for(int y=0;y<m;y++)
			{
				int best = -1;
				int c = 0;
				for(int u=0;u<4;u++)
				{
					int xx = x + dx[u];
					int yy = y + dy[u];
					if(xx>=0 && xx<n && yy>=0 && yy<m)
						if(best==-1 || best > h[xx][yy])
						{
							best = h[xx][yy];
							c = u;
						}
				}
				if(best!=-1 && best < h[x][y]) father[ff(p[x][y])] = ff(p[x+dx[c]][y+dy[c]]);
			}
		char temp = 'a';
		for(int x=0;x<n;x++)
			for(int y=0;y<m;y++)
				if(u[ff(p[x][y])]==0)
				{
					u[ff(p[x][y])] = temp;
					temp++;
				}
		if(temp>'z'+1) while(1) puts("!");
		printf("Case #%d:\n",test);
		for(int x=0;x<n;x++)
			for(int y=0;y<m;y++)
			{
				printf("%c",u[ff(p[x][y])]);
				if(y==m-1) printf("\n");
				else printf(" ");
			}
	}
	return 0;
}

