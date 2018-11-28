#include <stdio.h>
#include <vector>
using namespace std;
int main () {
	FILE *input, *output;
	input = fopen("input2.in","r");
	output = fopen("output.txt","w");
	int count, i, j;
	fscanf(input, "%d", &count);
	vector <int> n, k;
	int a, b;
	for (i=0;i<count;i++) {
		fscanf(input,"%d %d",&a, &b);
		n.push_back(a);
		k.push_back(b);
	}
	int wn;
	for (i=0;i<count;i++) {
		wn = 1;
		for (j=0;j<n[i];j++) {
			wn = wn * 2;	
		}
		if (k[i]%wn==(wn-1)) {
			fprintf(output, "Case #%d: ON\n", i+1);
		}
		else {
			fprintf(output, "Case #%d: OFF\n", i+1);
		}
	}

	return 0;
}