#include <stdio.h>

int main () {
	int tn, t;
	int nn, i, j, c;
	int a[1000], b[1000];
	FILE *input, *output;
	input = fopen("input.in","r");
	output = fopen("output.txt","w");
	fscanf(input,"%d",&tn);
	for (t=1;t<=tn;t++) {
		fscanf(input, "%d", &nn);
		for (i=0;i<nn;i++) {
			fscanf(input, "%d %d", &a[i], &b[i]);
		}
		c = 0;
		for (i=0;i<nn;i++) {
			for (j=i+1;j<nn;j++) {
				if ((a[i]>a[j]) && (b[i]<b[j])) c++;
				if ((a[i]<a[j]) && (b[i]>b[j])) c++;
			}
		}
		fprintf(output, "Case #%d: %d\n",t,c);
	}
	return 0;
}