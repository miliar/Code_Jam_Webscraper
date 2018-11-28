#include <cstdio>

using namespace std;

int T,W,H;

int map[101][101];
int sink[101][101];
char labels[101*101];

int get_sink(int j, int k) {
	if (sink[j][k] >= 0)
		return sink[j][k];
	
	int tj=j, tk=k, talt=map[j][k];
		
	if ((map[j-1][k]<talt)&&(j>0)) {
		tj = j - 1;
		tk = k;
		talt = map[j-1][k];
	}

	if ((map[j][k-1]<talt)&&(k>0)) {
		tj = j;
		tk = k-1;
		talt = map[j][k-1];
	}
	
	if ( (map[j][k+1]<talt) && (k<(W-1)) ) {
		tj = j;
		tk = k+1;
		talt = map[j][k+1];
	}
	
	if ( (map[j+1][k]<talt) && (j<(H-1)) ) {
		tj = j+1;
		tk = k;
		talt = map[j+1][k];
	}
			
	if ((tj==j)&&(tk==k)) {
		sink[j][k]=j*W+k;
	} else	
		sink[j][k] = get_sink(tj, tk);
		
	return sink[j][k];		
}

int main() {
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		scanf("%d %d", &H, &W);
		for(int j=0; j<H; j++)
			for(int k=0; k<W; k++) {
				scanf("%d", &map[j][k]);
				sink[j][k]=-1;
				labels[j*W+k]=0;
			}
		
		for(int j=0; j<H; j++) {
			for(int k=0; k<W; k++) {
				sink[j][k] = get_sink(j,k);				
			}
		}

		
		printf("Case #%d:\n", (i+1));
		char z = 'a';
		for(int j=0; j<H; j++) {
			for(int k=0; k<W; k++) {
				int s = sink[j][k];
				if (labels[s]==0) {
					labels[s]=z;
					z++;
				}
				printf("%c\t", labels[s]);
			}
			printf("\n");
		}
		
	}
	return 0;
}



