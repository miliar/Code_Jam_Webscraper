#include <cstdio>
#include <cstring>
int TT;
int PD[100][100];
int grid[100][100];
int H,W,R;

int voodoo(int y,int x) {
	if(y<0 or y>=H or x<0 or x>=W)
		return 0;
	if(grid[y][x]==1)
		return 0;
	int &ans=PD[y][x];
	if(ans!=-1)
		return ans;
	ans=0;
	ans=(voodoo(y-2,x-1)+voodoo(y-1,x-2))%10007;
	return ans;
}
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		printf("Case #%d: ",T);
		memset(PD,-1,sizeof(PD));
		memset(grid,0,sizeof(grid));
		scanf("%d %d %d",&H,&W,&R);
		PD[0][0]=1;
		for(int i=0,j,k;i<R;i++) {
			scanf("%d %d",&j,&k);
			grid[j-1][k-1]=1;
		}
		printf("%d\n",voodoo(H-1,W-1));
	}
}
