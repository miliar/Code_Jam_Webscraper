#include<stdio.h>
#include<algorithm>

using namespace std;

bool gN[8][8], gM[8][8];
void read(bool gp[8][8], int N) {
	for(int i=0;i<8;i++)
		for(int j=0;j<8;j++)
			gp[i][j]=false;

	for(int i=0;i<N-1;i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		a--; b--;
		gp[a][b]=gp[b][a]=true;
	}
}

int main() {
	int C;
	scanf("%d", &C);
	for(int cas=1;cas<=C;cas++) {
		int N, M;
		scanf("%d", &N);
		read(gN, N);
		scanf("%d", &M);
		read(gM, M);

		int per[8];
		for(int i=0;i<N;i++) per[i]=i;

		bool ss=false;
		do {
			bool succ=true;
			for(int i=0;i<M;i++)
				for(int j=0;j<M;j++) {
					if(gN[per[i]][per[j]]!=gM[i][j]) {
						succ=false;
						goto next;
					}
				}
next:
			if(succ) {
				ss=true;
				break;
			}
		}while(next_permutation(per, per+N));

		printf("Case #%d: ", cas);
		if(ss) puts("YES");
		else puts("NO");
	}
	return 0;
}