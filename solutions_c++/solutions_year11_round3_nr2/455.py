#include <cstdio>
#include <cstdlib>
#include <cstring>

int main()
{
	int T; scanf("%d", &T);
	for(int test=1; test<=T; test++) {
		int L, t, N, C; scanf("%d%d%d%d", &L, &t, &N, &C);
		int v[1050]; for(int i=0; i<C; i++) scanf("%d", &v[i]);
		int vzd[1050];
		for(int i=0; i<N; i++) vzd[i]=v[i%C];
				//for(int i=0; i<N; i++) printf("%d ", vzd[i]); printf("\n");
		if(L==0) {
			int suma=0;
			for(int i=0; i<N; i++) suma+=vzd[i];
			printf("Case #%d: %d\n", test, 2*suma);
		} else if(L==1) {
			int suma=0;
			for(int i=0; i<N; i++) suma+=vzd[i];
			int psuma=0;
			int best=2*suma;
			for(int i=0; i<N; i++) {
				if(2*psuma>=t) {if(2*suma-vzd[i]<best) best=2*suma-vzd[i];}
				else if(2*psuma+2*vzd[i]>t) {
					if(2*suma-vzd[i]+(t-2*psuma)/2<best) best=2*suma-vzd[i]+(t-2*psuma)/2;
				}
				psuma+=vzd[i];
			}
			printf("Case #%d: %d\n", test, best);
		} else {
			int suma=0;
			for(int i=0; i<N; i++) suma+=vzd[i];
			int best=2*suma;
			int kde;
{
int psuma=0;
for(int i=0; i<N; i++) {
	if(2*psuma>=t) {if(2*suma-vzd[i]<best) {best=2*suma-vzd[i]; kde=i;}}
	else if(2*psuma+2*vzd[i]>t) {
		if(2*suma-vzd[i]+(t-2*psuma)/2<best) {best=2*suma-vzd[i]+(t-2*psuma)/2; kde=i;}
	}
	psuma+=vzd[i];
}
}
{
int psuma=0;
int puvbest=best;
for(int i=0; i<N; i++) {
	if(i==kde) {psuma+=vzd[i]; continue;}
	if(2*psuma>=t) {if(puvbest-vzd[i]<best) {best=puvbest-vzd[i];}}
	else if(2*psuma+2*vzd[i]>t) {
		if(puvbest-vzd[i]+(t-2*psuma)/2<best) {best=puvbest-vzd[i]+(t-2*psuma)/2;}
	}
	psuma+=vzd[i];
}
}
			printf("Case #%d: %d\n", test, best);
		}
	
	}

	return 0;
}
