#include <stdio.h>
#include <algorithm>
using namespace std;

int p;
int a[1024];
int b[1024];
int mi[1024], mi2[1024];

long long calc(int i, int minus) {
	
	int pa = i/2;
	int ch1 = i*2+1;
	int ch2 = i*2+2;
			
	int toc = i+1;
	int level = 0;
	while (toc) {
		level++;
		toc >>= 1;
	}

//	for (int ii=0; ii<level; ii++) putchar(' ');	printf("calc: %d %d\n", i, minus);
//	for (int ii=0; ii<level; ii++) putchar(' ');	printf("b[i] = %d\n", b[i]);


	int isleaf = level == p;
	long long res;
	
	if (isleaf) {
		if (mi[i] - minus > 1)
			res = 1000000000;
		else if (mi[i] - minus == 1)
			res = b[i];
		else
			res  = 0;
	}
	else {
		res = min(calc(ch1, minus) + calc(ch2, minus),
				calc(ch1, minus+1) + calc(ch2, minus+1) + b[i]);
		
	}
//	for (int ii=0; ii<level; ii++) putchar(' ');	printf("calc: %d %d = %d\n", i, minus, res);
	return res;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int ca=1; ca<=t; ca++) {
		scanf("%d", &p);
		for (int i=0; i<(1<<p); i++)
			scanf("%d", &a[i]);
			
		for (int i=0; i<p; i++) {
//			printf("lineno = %d\n", (1<<(p-i-1)));
			
			for (int j=0; j<(1<<(p-i-1)); j++) {
//				printf("to %d\n", ((1<<(p-i-1))-1 + j));
				scanf("%d", &b[((1<<(p-i-1)))-1 + j]);
				
				if (i == 0)
					mi[((1<<(p-i-1)))-1 + j] = p-min(a[j*2], a[j*2+1]);
			}
			
		}
		
//		for (int i=0; i<(1<<p); i++)printf("bb: %d\n", b[i]);


		printf("Case #%d: %d\n", ca, (int)calc(0, 0));

		continue;
		
		
	}
}

			
