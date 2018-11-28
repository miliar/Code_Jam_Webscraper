#include<stdio.h>
#include<memory.h>

int ans[101][101];
bool can[101][101];

int N;
int H,W,R;
int r,c;

bool valid(int x,int y)
{
	return x>=0&&x<=H&&y>=0&&y<=W;
}

void init()
{
	memset(can,0,sizeof(can));
	scanf("%d%d",&H,&W);
	scanf("%d",&R);
	memset(can,true,sizeof(can));
	while(R--)
	{
		scanf("%d%d",&r,&c);
		can[r][c]=false;
	}
}

void dp()
{
	int i,j;
	memset(ans,0,sizeof(ans));
	ans[1][1]=1;
	for(i=1;i<=H;i++)
		for(j=1;j<=W;j++)
		{
			if(ans[i][j])
			{
				if(valid(i+2,j+1)&&can[i+2][j+1])
					ans[i+2][j+1]=(ans[i+2][j+1]+ans[i][j])%10007;
				if(valid(i+1,j+2)&&can[i+1][j+2])
					ans[i+1][j+2]=(ans[i+1][j+2]+ans[i][j])%10007;
			}
		}
	printf("%d\n",ans[H][W]);
}

int main()
{
	//freopen("D.in","r",stdin);
	//freopen("D.txt","w",stdout);
	scanf("%d",&N);
	int i;
	for(i=1;i<=N;i++)
	{
		init();
		printf("Case #%d: ",i);
		dp();
	}
	return 0;
}
		
