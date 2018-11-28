#include <iostream>
using namespace std;
int A[110][110];
int B[110][110];
int DX[4]={-1,0,0,1};
int DY[4]={0,-1,1,0};
int cnt,M,N;
void go(int x,int y)
{
	if (B[x][y]>-1) return;
	int t1,t2,i,xx,yy;
	t1=A[x][y]; t2=-1;
	for(i=0;i<4;i++)
	{
		xx=x+DX[i]; yy=y+DY[i];
		if (0<=xx&&xx<M&&0<=yy&&yy<N&&A[xx][yy]<t1)
		{
			t1=A[xx][yy]; t2=i;
		}
	}
	if (t2==-1) B[x][y]=cnt++; else
	{
		go(x+DX[t2],y+DY[t2]);
		B[x][y]=B[x+DX[t2]][y+DY[t2]];
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int ttt,i,j,tt;
	scanf("%d",&tt);
	for(ttt=0;ttt<tt;ttt++)
	{
		scanf("%d%d",&M,&N);
		for(i=0;i<M;i++) for(j=0;j<N;j++) scanf("%d",&A[i][j]);
		memset(B,-1,sizeof(B));
		cnt=0;
		for(i=0;i<M;i++) for(j=0;j<N;j++)
		if (B[i][j]==-1) go(i,j);
		printf("Case #%d:\n",ttt+1);
		for(i=0;i<M;i++)
		{
			for(j=0;j<N;j++) printf("%c ",'a'+B[i][j]);
			printf("\n");
		}
	}
//	system("pause");
	return 0;
}
