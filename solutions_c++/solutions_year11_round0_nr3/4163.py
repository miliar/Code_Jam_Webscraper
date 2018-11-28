#include <fstream>

using namespace std;

FILE* fin = fopen("C-large.in","r");
FILE* fout= fopen("C-large.out","w");
// FILE* fin = stdin;
// FILE* fout = stdout;
int a[2000];

void calc(int Case) {
	int N;
	fscanf(fin,"%d",&N);
	int xor = 0;
	int sum = 0;
	int min = 1e9;
	for(int i = 0;i<N;i++) {
		fscanf(fin,"%d",&a[i]);
		xor ^= a[i];
		sum+=a[i];
		if (a[i]<min)
			min = a[i];
	}
	if (xor)
		fprintf(fout,"Case #%d: NO\n",Case+1);
	else {
		fprintf(fout,"Case #%d: %d\n",Case+1,sum-min);

	}


}
int main() {
	int T;
	fscanf(fin,"%d",&T);
	for(int i = 0;i<T;i++)
		calc(i);
}