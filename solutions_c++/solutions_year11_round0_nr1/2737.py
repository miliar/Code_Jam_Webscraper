#include <cstdio>

int abs(int n) {
	if(n<0) return -n;
	return n;
}

int seqO[300];
int seqB[300];
char seq[300];

int main() {
	int T,N;
	scanf("%d",&T);
	for(int t=1;t<=T;++t) {
		int qO = 0,qB = 0;
		int pO = 1,pB = 1;
		printf("Case #%d: ",t);
		scanf("%d",&N);
		char rob;
		int but;
		for(int a=0;a<N;++a) {
			scanf(" %c%d",&rob,&but);
			seq[a] = rob;
			if(rob == 'O') {
				seqO[qO++] = but;
			}
			else seqB[qB++] = but;
		}
		int iO = 0,iB = 0,i = 0;
		int ans = 0;
		while(iO<qO && iB < qB) {
			if(seq[i++] == 'O') {
				int d = abs(seqO[iO] - pO) + 1;
				ans += d;
				pO = seqO[iO++];
				if(d >= abs(seqB[iB] - pB)) {
					pB = seqB[iB];
				}
				else seqB[iB] < pB ? pB -= d : pB += d;
			}
			else {
				int d = abs(seqB[iB] - pB) + 1;
				ans += d;
				pB = seqB[iB++];
				if(d >= abs(seqO[iO] - pO)) {
					pO = seqO[iO];
				}
				else seqO[iO] < pO ? pO -= d : pO += d;
			}
		}
		while(iO < qO) {
			ans += abs(seqO[iO] - pO)+1;
			pO = seqO[iO++];
		}
		while(iB < qB) {
			ans += abs(seqB[iB] - pB)+1;
			pB = seqB[iB++];
		}
		printf("%d\n",ans);
	}
	return 0;
}
