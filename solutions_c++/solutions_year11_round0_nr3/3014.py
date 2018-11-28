#include <cstdio>
#define VETSI(a, b) ((a)>(b) ? (a) : (b))

void hledej(int uroven, int xorovy1, int xorovy2, int normalni1, int normalni2);
int N;
int Hodnoty[100];
int Max;

int main()
{
	int T; scanf("%d", &T);
	for(int test=1; test<=T; test++) {
		Max=-1;
		scanf("%d", &N); for(int i=0; i<N; i++) scanf("%d", &Hodnoty[i]);
		hledej(0, 0, 0, 0, 0);
		if(Max==-1) printf("Case #%d: NO\n", test);
		else printf("Case #%d: %d\n", test, Max);
	}

	return 0;
}

void hledej(int uroven, int xorovy1, int xorovy2, int normalni1, int normalni2)
{
	if(uroven==N) {if(xorovy1==xorovy2 && normalni1!=0 && normalni2!=0 && Max<VETSI(normalni1, normalni2)) {Max=VETSI(normalni1, normalni2);}}
	else {
		hledej(uroven+1, xorovy1^Hodnoty[uroven], xorovy2, normalni1+Hodnoty[uroven], normalni2);
		hledej(uroven+1, xorovy1, xorovy2^Hodnoty[uroven], normalni1, normalni2+Hodnoty[uroven]);
	}
}
