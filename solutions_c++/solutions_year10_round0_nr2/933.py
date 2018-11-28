#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

typedef long long NATURAL;
const unsigned maxN = 1000;

NATURAL num[maxN];
int N;



NATURAL gcd(NATURAL a, NATURAL b)
{
	return (b == 0) ? abs(a) : gcd(b, a%b);
}

NATURAL gcd_all()
{
	NATURAL res = abs(num[0]);
	for (int i = 1; i < N - 1; i++)
	{
		if (res == 1) break;

		res = gcd(res, num[i]);
	}

	return res;
}


NATURAL fair_warning()
{
	for (int i = 0; i < N-1; ++i)
	{
		num[i] -= num[i+1];
	}

	NATURAL a = gcd_all();
	NATURAL b = num[N-1];



	NATURAL res = -b % a;

	//cout << a << " " << b << res << endl;
	while (res < 0) res += a;

	return res;
}

int main(void)
{
	int C;

	cin >> C;
	for (int i = 1; i <= C; i++)
	{
		cin >> N;

		for (int j = 0; j < N; j++)
		{
			cin >> num[j];
		}

		NATURAL res = fair_warning();

		cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}

