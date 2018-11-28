#include <stdio.h>

int t,n;
int s[220];
int sum;

bool eliminate(int idx, double frac) {
	double pts = s[idx]+sum*frac;
	double rest=1-frac;

	for (int i=0; i<n; i++) if (i!=idx) {
		double beg=0.0;
		double end=1.;

		for (int bs=0; bs<50; bs++) {
			double mid=(beg+end)/2;

			if (pts<(s[i]+mid*sum)) end=mid;
			else beg=mid;
		}

		if (end>rest) return false;
		else rest-=beg;
	}

	return true;
}

int main() {
	scanf("%d", &t);
	
	for (int it=1; it<=t; it++) {
		scanf("%d", &n);

		for (int i=0; i<n; i++)
			scanf("%d", &s[i]);

		sum=0;
		for (int i=0; i<n; i++)
			sum+=s[i];

		printf("Case #%d:", it); 

		for (int i=0; i<n; i++) {
			double beg=0., end=1.;

			for (int bs=0; bs<50; bs++) {
				double mid=(beg+end)/2;

				if (eliminate(i,mid)) beg=mid;
				else end=mid;	
			}

			printf(" %lf", beg*100);
		}
		printf("\n");
	}
 
	return 0;
}
