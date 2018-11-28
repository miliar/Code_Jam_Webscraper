#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;

int csK, csN;
int A1, A2, B1, B2;

inline int calc(int a, int b)
{
	int q = a / b, r = a % b;
//	fprintf(stderr, "a = %d, b = %d, q = %d, r = %d\n", a, b, q, r);
	if(q > 1) return 1;
	else if(r == 0) return 0;
	else return calc(b, r) ^ 1;
}

int main()
{
	int i, j, k, m, t;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d %d %d", &A1, &A2, &B1, &B2);
		m = 0;
		for(i = A1; i <= A2; ++i)
			for(j = B1; j <= B2; ++j)
				if(i < j) m += calc(j, i);
				else m += calc(i, j);
		printf("Case #%d: %d\n", csK, m);
	}
}





