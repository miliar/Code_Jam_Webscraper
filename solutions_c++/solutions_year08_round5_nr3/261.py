#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int TT;
int N,M;
char grid[16][16];
int PD[10][1<<10];
bool pode(int bit,int r) {
	int ult=-2;
	for(int j=0;j<M;j++) {
		if(bit & (1<<j)) {
			if(ult==j-1)
				return false;
			if(grid[r][j]=='x')
				return false;
			ult=j;
		}
	}
	return true;
}
int pode(int bit1,int bit2, int r) {
	if(pode(bit1,r) and pode(bit2,r-1)) {
		for(int j=0;j<M;j++) {
			if(bit1 & (1<<j)) {
				if(j==0) {
					if(bit2 & (1<<(j+1)))
						return false;
				} else if(j==M-1) {
					if(bit2 & (1<<(j-1)))
						return false;
				}
				else {
					if((bit2 & (1<<(j-1))) or (bit2 & (1<<(j+1))))
						return false;
				}
			}
		}
	}
	return true;
}
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		printf("Case #%d: ",T);
		scanf("%d %d",&N,&M);
		for(int i=0;i<N;i++) {
			scanf("%s",grid[N-i-1]);
		}
		memset(PD,0,sizeof(PD));
		int ans=0;
		for(int i=0;i<(1<<M);i++) {
			if(pode(i,0)) {
				PD[0][i]=max(PD[0][i],__builtin_popcount(i));
				ans=max(ans,PD[0][i]);
			}
		}
		for(int j=1;j<N;j++) {
			for(int i=0;i<(1<<M);i++) {
				if(pode(i,j))
					for(int i2=0;i2<(1<<M);i2++) {
						if(pode(i,i2,j)) {
							PD[j][i]=max(PD[j][i],__builtin_popcount(i)+PD[j-1][i2]);
							ans=max(ans,PD[j][i]);
						}
					}
			}
		}
		printf("%d\n",ans);
	}

	return 0;
}
