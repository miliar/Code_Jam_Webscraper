#include <cstdio>
int main()
{
	int n;
	int t;
	int na, nb;
	const int slots = 24*60;
	int t1[slots];
	int t2[slots];
	int maxa;
	int maxb;
	int nad[100];
	int naa[100];
	int nbd[100];
	int nba[100];
	scanf("%d", &n);
	for (int case_ = 0; case_ < n; ++case_)
	{
		scanf("%d", &t);
		scanf("%d", &na);
		scanf("%d", &nb);
		int a;
		int b;
		for (int i = 0; i < na; ++i) {scanf("%d:%d", &a, &b); nad[i] = a*60+b; scanf("%d:%d", &a, &b); naa[i] = a*60+b;}
		for (int i = 0; i < nb; ++i) {scanf("%d:%d", &a, &b); nbd[i] = a*60+b; scanf("%d:%d", &a, &b); nba[i] = a*60+b;} 
		for (int i = 0; i < slots; ++i)	{t1[i] = 0; t2[i] = 0;}
		for (int i = 0; i < na; ++i){ t1[nad[i]] -= 1; t2[naa[i] + t]+=1;}
		for (int i = 0; i < nb; ++i){ t2[nbd[i]] -= 1; t1[nba[i] + t]+=1;}
		int suma = 0;
		int sumb = 0;
		int maxa = 0;
		int maxb = 0;
		for (int i = 0; i < slots; ++i)
		{
			suma -= t1[i];
			sumb -= t2[i];
			if (suma > maxa) maxa = suma;
			if (sumb > maxb) maxb = sumb;
		}
		printf("Case #%d: %d %d\n", (case_+1), maxa, maxb);
	}
	return 0;
}

