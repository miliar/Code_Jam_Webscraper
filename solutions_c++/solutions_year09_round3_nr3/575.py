#include <stdio.h>
#include <algorithm>

using namespace std;

int P, Q;
int A[110]={0};
int process(void)
{
	sort(A,A+Q);
	int i, j;
	int or[110]={0};
	int chk[110]={0};
	int ret=P*Q;
	int tmp;
	for (i=0;i<Q;++i) or[i] = i;
	do{
		tmp = 0;
		for (i=0;i<Q;++i) chk[i] = 0;
		for (i=0;i<Q;++i){
			chk[or[i]] = 1;
			for (j = or[i]-1; j>=0; --j){
				if (chk[j] == 1){
					tmp = tmp + (A[or[i]]-A[j]-1);
					break;
				}
			}
			if (j<0){
				tmp = tmp + (A[or[i]]-1);
			}

			for (j=or[i]+1; j<Q; ++j){
				if (chk[j] == 1){
					tmp = tmp + (A[j]-A[or[i]]-1);
					break;
				}
			}
			if (j>=Q){
				tmp = tmp + (P-A[or[i]]);
			}
		}
		if (tmp < ret) ret = tmp;
	}while(next_permutation(or,or+Q));
	return ret;
}
int main(void)
{
	int N;
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &N);
	int test_case;
	int i;
	for (test_case = 1; test_case<=N; ++test_case){
		fscanf(fin, "%d %d", &P, &Q);
		for (i=0;i<Q;++i){
			fscanf(fin, "%d", &A[i]);
		}
		fprintf(fout, "Case #%d: %d\n", test_case, process());
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

/*
#include <stdio.h>
#include <set>

using namespace std;

int P, Q;
int A[110]={0};
int process(void)
{
	int chk[110]={0};
	set<int> used;
	int i, j;
	int MAX = P;
	int x;
	int ret=0;
	used.insert(0); used.insert(P+1);
	for (i=0;i<Q;++i){
		MAX = -1;
		x = -1;
		for (j=0;j<Q;++j){
			if (chk[j]==0){
				if (MAX < (*(used.upper_bound(A[j]))-A[j])){
					MAX = (*(used.upper_bound(A[j]))-A[j]);
					x = j;
				}
				if (MAX < (A[j]-(*(used.lower_bound(A[j]))))){
					MAX = (A[j]-(*(used.lower_bound(A[j]))));
					x = j;
				}
				printf("%d %d\n", (*(used.upper_bound(A[j]))), (*(used.lower_bound(A[j]))));
			}
		}
		printf("%d %d\n", (*(used.upper_bound(A[x]))), (*(used.lower_bound(A[x]))));
		ret = ret + (*(used.upper_bound(A[x]))) - (*(used.lower_bound(A[x]))) - 2;
		chk[x] = 1;
		used.insert(A[x]);
	}
	return ret;
}
int main(void)
{
	int N;
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &N);
	int test_case;
	int i;
	for (test_case = 1; test_case<=N; ++test_case){
		fscanf(fin, "%d %d", &P, &Q);
		for (i=0;i<Q;++i){
			fscanf(fin, "%d", &A[i]);
		}
		fprintf(fout, "Case #%d: %d\n", test_case, process());
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
*/