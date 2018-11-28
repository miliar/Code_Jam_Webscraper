#include <stdio.h>
int cnt[105][105];
int rock[105][105];
int main()
{
	int q,w,T,t,W,H,R;
	int y,x;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d %d %d",&H,&W,&R);
		for (q=1;q<=H;q++) for (w=1;w<=W;w++) 
			cnt[q][w]=rock[q][w]=0;
		cnt[1][1]=1;
		for (q=1;q<=R;q++) 
		{
			scanf("%d %d",&y,&x);
			rock[y][x]=1;
		}
		for (q=1;q<=H;q++) for (w=1;w<=W;w++)
		{
			//(dy,dx)=(2,1)
			y=q+2,x=w+1;
			if (y<=H && x<=W && rock[y][x]==0) cnt[y][x]=(cnt[y][x]+cnt[q][w])%10007;
			y=q+1,x=w+2;
			if (y<=H && x<=W && rock[y][x]==0) cnt[y][x]=(cnt[y][x]+cnt[q][w])%10007;
		}
		printf("Case #%d: %d\n",t,cnt[H][W]);
	}
	return 0;
}
