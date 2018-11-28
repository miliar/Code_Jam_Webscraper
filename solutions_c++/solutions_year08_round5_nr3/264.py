#include<iostream>
using namespace std;

char ar[200][200];
int dp[2][(1<<11)];
int x,tc,h,w,i,j,k,jawab;

bool valid(int x, int y) {
	int i;
	for(i=0;i<w;i++) {
		if((ar[x][i]=='x')&&((1<<i)&y)) return false;
		if((i>0)&&((1<<i)&y)&&((1<<(i-1))&y)) return false;
		if((i<w-1)&&((1<<i)&y)&&((1<<(i+1))&y)) return false;
	}
	return true;
}

bool valid1(int x, int y) { //x depan, y blk
	int i;
	for(i=0;i<w;i++) {
		if((i>0)&&((1<<i)&y)&&((1<<(i-1))&x)) return false;
		if((i<w-1)&&((1<<i)&y)&&((1<<(i+1))&x)) return false;
	}
	return true;
}

int itung(int x) {
	int temp,i;
	temp=0;
	for(i=0;i<w;i++) {
		if((1<<i)&x) temp++;
	}
	return temp;
}

int main() {
	freopen("csmal.in","r",stdin);
	freopen("csmal.out","w",stdout);
	scanf("%d",&tc);
	for(x=1;x<=tc;x++) {
		scanf("%d %d",&h,&w);
		memset(ar,0,sizeof(ar));
		memset(dp,0,sizeof(dp));
		for(i=0;i<h;i++) {
			getchar();
			for(j=0;j<w;j++) {
				ar[i][j]=getchar();
			}
		}
		for(j=0;j<(1<<w);j++) {
			if(!valid(0,j)) {
				dp[0][j]=-1; continue;
			}
			dp[0][j]=itung(j);
		}
		for(i=1;i<h;i++) {
			for(j=0;j<(1<<w);j++) dp[i%2][j]=-1;
			for(j=0;j<(1<<w);j++) {
				if(!valid(i,j)) continue;
				for(k=0;k<(1<<w);k++) {
					if(dp[1-(i%2)][k]==-1) continue;
					if(!valid1(k,j)) continue;
					dp[i%2][j]=max(dp[i%2][j],dp[1-(i%2)][k]+itung(j));
				}
			}
		}
		jawab=0;
		for(i=0;i<(1<<w);i++) jawab=max(jawab,dp[(h-1)%2][i]);
		printf("Case #%d: %d\n",x,jawab);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
