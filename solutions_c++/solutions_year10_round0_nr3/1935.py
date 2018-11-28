#include <stdio.h>

struct check{
	long long sum;
	int pos;
	int move;
};

check C[1000];
int index;
int search(int value, int move);

int main(void) {
	int test;
	int R, K, N;
	int Gi[1000];
	int move, k;
	long long board;
	int temp;
	long long repeat;
	long long ret;

	scanf("%d",&test);
	for(int i=1 ; i<=test ; i++) {
		scanf("%d %d %d", &R, &K, &N);
		for(int j=0 ; j<N ; j++) {
			scanf("%d", &Gi[j]);
		}

		index = 0;
		k = 0;
		while(1)
		{
			move = 0;
			board = 0;
			while(board+Gi[k] <= K && move < N) {
				board += Gi[k++];
				if(k >= N) {
					k = 0;
				}
				++move;
			}
			temp = search(k, move);
			if(temp == -1) {
				C[index].sum = board;
				C[index].pos = k;
				C[index++].move = move;
			}
			else {
				break;
			}
		}

		ret = 0;
		for(int j=0 ; j<temp && j<R ; j++) {
			ret += C[j].sum;
		}

		repeat = 0;
		for(int j=temp ; j<index ; j++) {
			repeat += C[j].sum;
		}

		for(int j=0 ; j<(R-temp)%(index-temp) ; j++) {
			ret += C[j+temp].sum;
		}

		printf("Case #%d: %lld\n", i, ret+((R-temp)/(index-temp))*repeat);
	}

	return 0;
}

int search(int value, int move) {
	for(int i=0 ; i<index ; i++) {
		if(C[i].pos == value && C[i].move == move) {
			return i;
		}
	}
	return -1;
}
