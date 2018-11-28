#include <stdio.h>
#include <algorithm>

using namespace std;

class Tdata{
public:
	int A, B;
};

bool cmp(Tdata t1, Tdata t2){
	return (t1.A < t2.A);
}
int main(void)
{
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	int T, N;
	fscanf(fin, "%d", &T);
	int test_case;
	int i, j;
	int dab;
	Tdata D[1010];
	for (test_case=1;test_case<=T;++test_case){
		fscanf(fin, "%d", &N);
		for (i=0;i<N;++i){
			fscanf(fin, "%d %d", &D[i].A, &D[i].B);
		}
		sort(D,D+N,cmp);
		dab = 0;
		for (i=0;i<N;++i){
			for (j=0;j<i;++j){
				if (D[i].B < D[j].B) ++dab;
			}
		}
		fprintf(fout, "Case #%d: %d\n", test_case, dab);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}