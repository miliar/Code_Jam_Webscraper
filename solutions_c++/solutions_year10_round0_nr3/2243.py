#include <stdio.h>

#define MAXT 51
#define MAXN 1002
//#define MAXR 100000001

long long original[MAXN];
long long ride[MAXN];
long long income;
int firstg[MAXN];

int main() {
	int T,N;
	long long R, k;
	bool loop;

	FILE *infile, *outfile;
	infile = freopen("C-large.in", "r", stdin);
	outfile = fopen("b2.out","w");

	scanf("%d", &T);
	firstg[0] = 0;
	for(int cs = 0; cs < T; cs++) {
		scanf("%lld %lld %d", &R, &k, &N);
		int i;
		for(i = 0; i < N; i++) {
			scanf("%lld", &original[i]);
			ride[i] = 0;
		}

		loop = false;
		int j,s,t, first = 0;
		int start, loop_cnt= 0;
		int first_cnt = 1, group_cnt;
		long long per_ride, per_loop;
		income = 0;
		int loop_size = 0;

		while( R > 0 && loop_cnt < MAXN) {
			per_ride = 0; start = 0; group_cnt = 0;
			while( k - per_ride >= original[first]
			&& group_cnt < N ) {
				per_ride += original[first];
				first++;
				if(first == N) first = 0;
				group_cnt++;
			}
			// check if loop found
			ride[first_cnt-1] = per_ride;
			firstg[first_cnt] = first;
			income += per_ride; R--;
			for(s= 0 ; s < first_cnt; s++)
				if( first == firstg[s] ) {
					loop = true;
					start = s;
					loop_size = first_cnt - s;
					per_loop = 0;
					for(t = start; t < first_cnt; t++)
						per_loop += ride[t];
					break;
				};
			if(loop) break;
			first_cnt++; loop_cnt++;
		}
		if(R != 0) {
			// R is not zero
			int quo, mod;
			quo = R / loop_size;
			mod = R % loop_size;
			income += per_loop*quo;
			for(i = 0; i < mod; i++)
				income += ride[start+i];
		}

		printf("Case #%d: %lld\n", cs+1, income);
		fprintf(outfile, "Case #%d: %lld\n", cs+1, income);
	}
}