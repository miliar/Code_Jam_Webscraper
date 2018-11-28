#include <iostream>
#include <cstring>
using namespace std;
#define maxn 402
int cc[2][maxn][maxn];
int t,r;
int judge;
int dir;
void turn()
{
	int kl,tmp;
	int i,j;
	for(i=1;i<maxn;i++)
	{
		for(j=1;j<maxn;j++)
		{
			kl = 0;
			tmp = 0;
			if(i!=1&&cc[dir][i-1][j]==1)
				tmp++;
			if(j!=1&&cc[dir][i][j-1]==1)
				tmp++ ;
			if(cc[dir][i][j]==0){
				if(tmp==2){
				cc[1-dir][i][j] = 1;
					kl = 1;
				}
				else
				cc[1-dir][i][j] = 0;
				}
			if(cc[dir][i][j]==1)
			{
				if(tmp == 0)
					cc[1-dir][i][j] = 0;
				else{
				kl = 1;
					cc[1-dir][i][j] = 1;
					}
			}
			if(kl == 1)
			{
				judge = 1;
			}
		}
	}
	//printf("%d\n",judge);
	return;
}
void print()
{
	printf("--------------\n");
	int i,j;
	for(i=1;i<=20;i++)
	{
		for(j=1;j<=20;j++)
		{
			printf("%d",cc[dir][i][j]);
		}
		printf("\n");
	}
	printf("---------------\n");
	system("pause");
	return;
}
int main()
{
	int x1,y1,x2,y2,cnt;
	int i,j,cs;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	while(scanf("%d",&t)!=EOF)
	{
		cs = 1;
		while(t--)
		{
			memset(cc,0,sizeof(cc));
			scanf("%d",&r);
			while(r--)
			{
				scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
				for(i=x1;i<=x2;i++)
				{
					for(j=y1;j<=y2;j++)
					{
						cc[0][i][j] = 1;
					}
				}
			}
			dir = 0;
			cnt = 0;
			//print();
			do
			{
				cnt++;
				judge = 0;
				turn();
				dir = 1-dir;
				//print();
				//printf("%d\n",judge);
			}while(judge);

			printf("Case #%d: %d\n",cs++,cnt);
		}
	}
	return 0;
}
