#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

int N, cards[1000], vals[100000];

void solve(int t) {
	int i;
	scanf("%d",&N);
	for(i=0;i<N;i++) scanf("%d",&cards[i]);
	if(N<=1) {
		printf("Case #%d: %d\n",t,N);
		return;
	}
	sort(cards,cards+N);
	int mx = 0;
	do {
		int len=1, mn=N, last=cards[0];
		for(i=1;i<N;i++) {
			//printf("%d,", cards[i]);
			if(last+1 != cards[i]) {
				if(i>0 && len < mn) mn = len;
				len = 1;
			} else len++;
			last = cards[i];
		}
		//printf("\n");
		if(len < mn) mn = len;
		if(mn > mx) mx = mn;
	} while(next_permutation(cards+1,cards+N-1));
	printf("Case #%d: %d\n",t,mx);
}

int main() {
	int t,T;
	double sec, tot;
	scanf("%d",&T);
	for(t=1;t<=T;t++) solve(t);
	return 0;
}
