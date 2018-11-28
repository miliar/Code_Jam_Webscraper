#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main () {
	FILE* In;
	FILE* Out;

	fopen_s(&In, "A-large.in", "r");
	fopen_s(&Out, "A-large.out", "w");

	int nTestCases, iTestCase;
	fscanf_s(In, "%d", &nTestCases);
	for (iTestCase=0; iTestCase < nTestCases; iTestCase++) {
		double x,s,r,t;
		int n,i,j;
		fscanf_s(In, "%lf %lf %lf %lf %d", &x,&s,&r,&t,&n);
		double b[1002],e[1002],w[1002];
		double l[1002];
		for (i=0;i<n;i++) {
			fscanf_s(In, "%lf %lf %lf", b+i,e+i,w+i);
			l[i] = e[i]-b[i];
			x-=l[i];
		}
		l[n] = x;
		w[n] = 0.;
		n++;

		double max = 0;
		int max_i = -1;
		for (i=0;i<n;i++) {
			max = w[i];
			max_i = i;
			for(j=i+1;j<n;j++) {
				if (w[j] < max) {
					max = w[j];
					max_i = j;
				}
			}
			w[max_i] = w[i];
			w[i] = max;
			max = l[max_i];
			l[max_i] = l[i];
			l[i] = max;
		}

		double tek_t, all_t = 0;
		for (i=0;i<n;i++) {
			tek_t = l[i]/(w[i]+r);
			if (all_t+tek_t < t) all_t += tek_t;
			else {
				all_t += (t-all_t)+(l[i] - (t-all_t)*(w[i]+r)) / (w[i]+s);
				break;
			}
		}
		for (j=i+1;j<n;j++) {
			all_t += l[j]/(w[j]+s);
		}

		//Write Out Results
		fprintf_s(Out, "Case #%d: %lf\n", iTestCase+1, all_t);
	}

	if (In) fclose(In);
	if (Out) fclose(Out);

	return 0;
}
