#include <cstdio>
#include <cstdlib>
#include <cstring>

int T;
int A, B;
long double pro[100000];
long double best;
long double pi;

int main()
{
	scanf("%d\n", &T);
	for(int tes=1; tes<=T; tes++) {
		scanf("%d %d\n", &A, &B);
		for(int i=0; i<A; i++) scanf("%Lf", &pro[i]);
		best=B+2;
		pi=1;
		for(int k=0; k<A; k++) {
			pi*=pro[k];
			long double akt=2*(A-k-1)+2*B-A+2-pi*(B+1);
			if(akt<best) best=akt;
		}
		printf("Case #%d: %Lf\n", tes, best);
	}

	return 0;
}
