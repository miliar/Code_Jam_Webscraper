/*
 * 2011-05-21  Martin  <Martin@Martin-desktop>

 * 
 */
#include <iostream>
#include <fstream>

using namespace std;

template <class T> T GCD(T a, T b)
{
	return (a == 0) ? b : GCD(b % a, a);
}

#define ll long long

void Solve()
{
	ll Pd, Pg, N;
	cin >> N >> Pd >> Pg;
	if ((Pd < 100 && Pg == 100) || (Pd > 0 && Pg == 0))
	{
		puts("Broken");
		return;
	}
	ll bb = 100 / GCD(Pd, 100LL);
	ll n = N / bb;
	if (Pd != 0 && n == 0)
	{
		puts("Broken");
		return;
	}
	puts("Possible");
}

int main()
{
	int TestCase;
	scanf("%d", &TestCase);
	for (int i = 1; i <= TestCase; ++ i)
	{
		printf("Case #%d: ", i);
		Solve();
	}
}
