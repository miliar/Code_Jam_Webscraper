#include <cstdio>

int mocn[10];

int T;
int A, B;
int D;
int N;
int found[20];

int digits(int n);
int rotate(int n, int d);

int main()
{
	mocn[0]=1;
	for(int i=1; i<=9; i++) mocn[i]=10*mocn[i-1];
	scanf("%d", &T);

	for(int test=1; test<=T; test++) {
		scanf("%d%d", &A, &B);
		D=digits(A);
		N=0;
		for(int prvni=A; prvni<B; prvni++) {
			for(int i=1; i<D; i++) {
				int druhe=rotate(prvni, i);
				found[i]=druhe;
				if(prvni<druhe && druhe<=B) {
					bool nalezeno=false;
					for(int j=1; j<i; j++) if(found[j]==druhe) {nalezeno=true; break;}
					if(!nalezeno) N++;
				}
			}
		}
		printf("Case #%d: %d\n", test, N);
	}

	return 0;
}

int digits(int n)
{
	int ret=0;
	while(n>0) {ret++; n/=10;}
	return ret;
}

int rotate(int n, int d)
{
	int zacatek=n%mocn[d], konec=n/mocn[d];
	return zacatek*mocn[D-d]+konec;
}
