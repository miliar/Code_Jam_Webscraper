#include <stdio.h>
#include <memory.h>
#define SIZE 110

int mp[SIZE][SIZE];
int h,w;
int tid(int i,int j)
{
	return i*w+j;
}
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int f[SIZE*SIZE];
int getroot(int k)
{
	if(f[k] != k)
		f[k] = getroot(f[k]);
	return f[k];
}
int vis[SIZE*SIZE];
int main()
{
	int a,b,ra,rb,i,j,ti,tj,k,T,no = 0;
	freopen("D:\\B-large.in","r",stdin);
	freopen("D:\\B-large.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		no++;
		scanf("%d%d",&h,&w);
		for(i = 0; i < h; i++)
		{
			for(j = 0; j < w; j++)
			{
				scanf("%d",&mp[i][j]);
				a = tid(i,j);
				f[a] = a;
			}
		}
		for(i = 0; i < h; i++)
		{
			for(j = 0; j < w; j++)
			{
				a = tid(i,j);
				b = -1;
				int minv = 10000000;
				for(k = 0; k < 4; k++)
				{
					ti = i + dir[k][0];
					tj = j + dir[k][1];
					if(ti >= 0 && ti < h && tj >= 0 && tj < w && mp[ti][tj] < mp[i][j])
					{
						if(mp[ti][tj] < minv)
						{
							minv = mp[ti][tj];
							b = tid(ti,tj);
						}
					}
				}
				if(b != -1)
				{
					ra = getroot(a);
					rb = getroot(b);
					f[ra] = rb;
				}
			}
		}
		memset(vis,0,sizeof(vis));
		char out = 'a';
		printf("Case #%d:\n",no);
		for(i = 0; i < h; i++)
		{
			for(j = 0; j < w; j++)
			{
				if(j != 0)
					printf(" ");
				a = tid(i,j);
				ra = getroot(a);
				if(!vis[ra])
					vis[ra] = out++;
				printf("%c",(char)vis[ra]);
			}
			printf("\n");
		}
	}
	return 0;
}