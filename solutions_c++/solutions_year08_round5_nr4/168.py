#include<stdio.h>

int at[200][200];
int H,W;
int R;
int i,j;
int ni,nj;
int diri[]={-2,-1,-2,-1};
int dirj[]={-1,-2,-2,-1};
int x,y,d;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int T,ks;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d%d%d",&H,&W,&R);
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
				at[i][j]=0;

		for(i=1;i<=R;i++)
		{
			scanf("%d%d",&x,&y);
			at[x][y]=-1;
		}

		at[1][1]=1;
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
			{
				for(d=0;d<2;d++)
				{
					ni=i+diri[d];
					nj=j+dirj[d];

					if(!(ni>=1 && nj>=1 && ni<=H && nj<=W)) continue;

					if(at[ni][nj]!=-1 && at[i][j]!=-1)
						at[i][j]=(at[ni][nj]+at[i][j])%10007;
				}
			}

		printf("Case #%d: ",ks);
		if(at[H][W]==-1) printf("0\n");
		else printf("%d\n",at[H][W]);

	}

	return 0;
}