#include <cstdio>
#include <iostream>

using namespace std;

long long N;
int PD, PG;

int Gcd(int A, int B)
{
	return (A == 0) ? B : Gcd(B % A, A);
}

int Work()
{
	cin >> N >> PD >> PG;
	if (PG == 100 || PG == 0)
		return (PD == PG);
	int G = Gcd(PD, 100);
	return (100 / G) <= N;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
		printf("Case #%d: %s\n", Case, Work() ? "Possible" : "Broken");
	return 0;
}