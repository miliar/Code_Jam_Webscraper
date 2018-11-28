#import <cstdio>
#import <string>
#import <algorithm>

using namespace std;
FILE* in, out;

int main() {
	int ncases;
	in = fopen("ain.txt","r");
	fscanf(in,"%d",&ncases);
	for (int casen = 1; casen <= ncases; casen++) {
		int P,K,L,total;
		int vals[1005];
		fscanf(in,"%d %d %d\n",&P,&K,&L);
		for (int i = 0; i < L; i++) {
			fscanf(in,"%d",&vals[i]);
		}
		sort(vals,vals+L);
		printf("Case #%d: ",casen);
		if (P*K < L) {
			printf("Impossible\n");
		} else {
			int i,j,k,total;
			j = k = total = 0;
			j = 1;
			for (i = L-1; i >= 0; i--) {
				total += j*vals[i];
				k++;
				if (k == K) {
					k = 0; j++;
				}
			}
			printf("%d\n",total);
		}
	}
	fclose(in);
}
