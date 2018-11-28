#include <stdio.h>

#define N 100

int L, H, n, a[N];

int Check(int m)
{
	for (int i = 0; i < n; ++i)
		if (a[i]%m && m%a[i]) return 0;
	return 1;
}

int main()
{
	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d%d%d", &n, &L, &H);
		for (int i = 0; i < n; ++i) scanf("%d", a+i);
		while (L <= H)
			if (!Check(L)) ++L; else break;
		printf("Case #%d: ", T);
		if (L <= H) printf("%d\n", L); else puts("NO");
	}
	return 0;
}

