#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

int main () {
	int tn, t;
	int ln, pn, cn, c, temp, res;
	FILE *input, *output;
	input = fopen("input.in","r");
	output = fopen("output.txt","w");
	fscanf(input,"%d",&tn);
	for (t=1;t<=tn;t++) {
		fscanf(input, "%d %d %d", &ln, &pn, &cn);
		c = 0;
		if ((ln * cn)>=pn) fprintf(output,"Case #%d: 0\n",t);
		else {
			while (ln<pn) {
				temp = pn % cn;
				pn = pn / cn;
				if (temp!=0) pn++;
				ln = ln * cn;
				if (ln==pn) c = c+1;
				else c = c+2;
			}
			res = 0;
			while (true) {
				res++;
				temp = c%2; 
				c = c/2;
				if (temp!=0) c++;
				if (c==1) break;
			}
			fprintf(output,"Case #%d: %d\n",t,res);
		}
	}
	return 0;
}

int to(int a, int b) {
	int i;
	int res=1;
	for (i=0;i<b;i++) {
		res = res * a;
	}
	return res;
}