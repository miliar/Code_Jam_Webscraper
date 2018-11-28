#include <stdio.h>

int main(void)
{
	int T, t;
	__int64 R, k;
	int N, i;
	int End[1010]={0};
	__int64 a[2010]={0};
	__int64 Sum[1010]={0};
	__int64 acc[1010]={0};
	__int64 sum = 0;
	__int64 dab = 0;
	__int64 chk[1010]={0};
	int ed = 0;
	int x;
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &T);
	for (t=1;t<=T;++t){
		fscanf(fin, "%I64d %I64d %d", &R, &k, &N);
		for (i=0;i<N;++i){
			fscanf(fin, "%I64d", &a[i]);
			a[i+N] = a[i];
			chk[i] = 0;
			Sum[i] = 0;
			End[i] = i;
			acc[i] = 0;
		}
		sum = 0;
		ed = 0;
		for (i=0;i<N;++i){
			if (ed>i) sum = sum - a[i-1];
			else{
				sum = 0;
				ed = i;
			}
			while (sum+a[ed] <= k && (ed-i)<N){
				sum = sum + a[ed];
				++ed;
				if (ed == i) break;
			}
			Sum[i] = sum;
			End[i] = ed;
			if (End[i] >= N) End[i] = End[i] - N;
		}
		x = 0;
		chk[x] = 1;
		sum = Sum[x];
		acc[x] = Sum[x];
		--R;
		while (R > 0){
			if (chk[End[x]] != 0){
				sum = sum + (acc[x]+Sum[End[x]]-acc[End[x]])*(R/(chk[x]+1-chk[End[x]]));
				R = R % (chk[x]+1-chk[End[x]]);
				break;
			}else{
				chk[End[x]] = chk[x] + 1;
				acc[End[x]] = acc[x] + Sum[End[x]];
				x = End[x];
				sum = sum + Sum[x];
				--R;
			}
		}
		while (R > 0){
			x = End[x];
			sum = sum + Sum[x];
			--R;
		}
		fprintf(fout, "Case #%d: %I64d\n", t, sum);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}