#include <cstdio>
#include <cstdlib>
#include <cstring>

int T;
int N;
int a[500];

int suma(int h);
void vypis(int h);

int main()
{
	scanf("%d", &T);

	for(int test=1; test<=T; test++) {
		scanf("%d", &N);
		for(int i=0; i<N; i++) scanf("%d", &a[i]);
		for(int f=1; f<(1<<N); f++) for(int g=1; g<(1<<N); g++) if(!(f&g)) {
			int sf=suma(f), sg=suma(g);
			if(sf==sg) {
				printf("Case #%d:\n", test);
				vypis(f);
				vypis(g);
				goto next;
			}
		}
		printf("Case #%d:\nImpossible\n", test);
next:;
	}

	return 0;
}

int suma(int h)
{
	int i=0;
	int s=0;
	while(h) {
		if(h&1) s+=a[i];
		i++;
		h>>=1;
	}
	return s;
}

void vypis(int h)
{
	bool prvni=true;
	int i=0;
	while(h) {
		if(h&1) {
			if(prvni) {printf("%d", a[i]); prvni=false;}
			else printf(" %d", a[i]);
		}
		i++;
		h>>=1;
	}
	printf("\n");
}
