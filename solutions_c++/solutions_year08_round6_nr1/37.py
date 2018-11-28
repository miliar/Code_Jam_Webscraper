#include<stdio.h>
#include<string.h>

int data[1000][2];

void test(int H, int W, int minH, int minW, int maxH, int maxW, int dp) {
	if(H<=maxH && H>=minH && W<=maxW && W>=minW) {
		puts("BIRD");
		return;
	}

	if(H>maxH) maxH=H;
	if(H<minH) minH=H;
	if(W>maxW) maxW=W;
	if(W<minW) minW=W;

	bool succ=true;
	for(int i=0;i<dp;i++) {
		if(data[i][0]<=maxH && data[i][0]>=minH && data[i][1]<=maxW && data[i][1]>=minW) {
			succ=false;
		}
	}

	if(succ) {
		puts("UNKNOWN");
	} else {
		puts("NOT BIRD");
	}
}

int main() {
	int cas;
	scanf("%d", &cas);
	for(int c=1;c<=cas;c++) {
		printf("Case #%d:\n", c);
		int N, M, dp=0;
		scanf("%d", &N);

		int minH=10000000, minW=10000000, maxH=-1, maxW=-1;

		for(int i=0;i<N;i++) {
			int H, W;
			char str[16];
			scanf("%d%d", &H, &W);
			gets(str);

			if(strcmp(str, " BIRD")==0) {
				if(H>maxH) maxH=H;
				if(H<minH) minH=H;
				if(W>maxW) maxW=W;
				if(W<minW) minW=W;
			} else {
				data[dp][0]=H;
				data[dp][1]=W;
				dp++;
			}
		}

		scanf("%d", &M);
		for(int i=0;i<M;i++) {
			int H, W;
			scanf("%d%d", &H, &W);
			test(H, W, minH, minW, maxH, maxW, dp);
		}
	}
	return 0;
}