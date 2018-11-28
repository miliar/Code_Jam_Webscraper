#include <cstdio>

char inv[100][3];
char opp[100][3];
char wort[1000];
int len;

bool oppM[30][30];

int main() {
	
	int T;
	scanf("%d ", &T);
	for(int t=0; t<T; ++t) {


		for(int i=0; i<30; ++i)
			for(int j=0; j<30; ++j)
				oppM[i][j] = false;

		int C;
		scanf("%d ", &C);
		for(int c=0; c<C; ++c) {
			scanf("%c%c%c ", &inv[c][0], &inv[c][1], &inv[c][2]);
			if(inv[c][0]>inv[c][1]) {
				char tmp = inv[c][1];
				inv[c][1] = inv[c][0];
				inv[c][0] = tmp;
			}
		}

		
		int D;
		scanf("%d ", &D);
		for(int d=0; d<D; ++d) {
			scanf("%c%c ", &opp[d][0], &opp[d][1]);
			if(opp[d][0]>opp[d][1]) {
				char tmp = opp[d][1];
				opp[d][1] = opp[d][0];
				opp[d][0] = tmp;
			}
			oppM[opp[d][1]-'A'][opp[d][0]-'A'] = true;
			oppM[opp[d][0]-'A'][opp[d][1]-'A'] = true;
		}

		int len=0;
		int N;
		scanf("%d ", &N);
		for(int n=0; n<N; ++n) {
			char buch;
			scanf(" %c ", &buch);
			wort[len++] = buch;
			if(len>1) {
				// try to invoke
				bool combined = false;
				{
					char b1 = wort[len-1];
					char b2 = wort[len-2];
					if(b1>b2) {
						char tmp = b1;
						b1 = b2;
						b2 = tmp;
					}
					for(int c =0; c<C && !combined; ++c) {
						if(b1==inv[c][0] && b2==inv[c][1]) {
							wort[len-2] = inv[c][2];
							len--;
							combined = true;
						}
					}
				}
				// try to oppose
				if(!combined){
					char b1 = wort[len-1];
					for(int x=0; x<len-1; ++x) {
						if(oppM[b1-'A'][wort[x]-'A']) {
							len=0;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: [", t+1);
		for(int i=0; i<len; ++i) {
			printf("%c", wort[i]);
			if(i<len-1)
				printf(", ");
		}
		printf("]\n");

	}


	return 0;
}
