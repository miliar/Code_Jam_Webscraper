#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int T;
int n;
int v1[800];
int v2[800];

int compare(const void *a, const void *b) {
	return (*((int*)a)) - (*((int*)b));
}


int main() {
	fstream in;
	in.open("prob1.in", fstream::in);
	FILE *out = fopen("prob1.out","w");

	in >> T;

	for (int a = 0; a < T; a++) {
		in >> n;
		for (int b = 0; b < n; b++) {
			in >> v1[b];
		}
		for (int c = 0; c < n; c++) {
			in >> v2[c];
		}
		qsort(v1,n,sizeof(int),compare);
		qsort(v2,n,sizeof(int),compare);

		__int64 ans = 0;
		for (int d = 0; d < n; d++) {
			ans += ((__int64)v1[d]) * ((__int64)v2[n-1-d]);
		}
		fprintf(out,"Case #");
		fprintf(out,"%i",a+1);
		fprintf(out,": ");
		fprintf(out,"%I64d\n",ans);
	}
	
	in.close();
	fclose(out);
	return 0;
}