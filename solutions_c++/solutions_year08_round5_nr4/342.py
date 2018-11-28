#include <iostream>
using namespace std;
int main()
{
	int a[110][110];
	int r[110][110];
	int H,W,R;
	int T,Ti;
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++)
	{
		scanf("%d%d%d",&H,&W,&R);
		memset(a,0,sizeof(a));
		memset(r,0,sizeof(r));
		for(int i=0;i<R;i++)
		{
			int t1,t2;
			scanf("%d%d",&t1,&t2);
			r[t1][t2]=1;
		}
		a[1][1]=1;
		for(int i=2;i<=H;i++)
			for(int j=2;j<=W;j++) if(!r[i][j]) 
			{
				a[i][j] = a[i-2][j-1] + a[i-1][j-2];
				a[i][j]%=10007;
			}

		printf("Case #%d: %d\n",Ti,a[H][W]);
	}
}