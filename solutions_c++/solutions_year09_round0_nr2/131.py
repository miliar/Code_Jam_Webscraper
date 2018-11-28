#include<stdio.h>

#define MIN(A,B) ((A) < (B) ? (A) : (B))

int mark[200][200];
int num[200][200];
int H,W;
int dirr[]={-1,0,0,1};
int dirc[]={0,-1,1,0};
int cnt=0;

int DFS(int r,int c)
{
	if(mark[r][c])
		return mark[r][c];

	int h = 10000000;

	int i,nr,nc;

	for(i=0;i<4;i++)
	{
		nr=r+dirr[i];
		nc = c+dirc[i];

		if(nr<0 || nr>=H || nc<0 || nc>=W) continue;

		h = MIN(h,num[nr][nc]);
	}

	if(h>=num[r][c]) 
	{
		mark[r][c]=++cnt;
		return cnt;
	}
	
	for(i=0;i<4;i++)
	{
		nr=r+dirr[i];
		nc = c+dirc[i];

		if(nr<0 || nr>=H || nc<0 || nc>=W) continue;
		if(num[nr][nc]==h)
		{
			mark[r][c]=DFS(nr,nc);
			return mark[r][c];
		}
	}


}

int main()
{
	freopen("Bhard.out","w",stdout);

	int T,ks,i,j;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d%d",&H,&W);
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
			{
				scanf("%d",&num[i][j]);
				mark[i][j]=0;
			}

		cnt=0;
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				if(mark[i][j]==0)
				{
					DFS(i,j);
				}

		printf("Case #%d:\n",ks);
		for(i=0;i<H;i++)
		{
			for(j=0;j<W;j++)
			{
				if(j) printf(" ");
				printf("%c",mark[i][j]+'a'-1);
			}
			printf("\n");
		}
	}

	return 0;
}