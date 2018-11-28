#include <iostream>
#include <algorithm>

using namespace std;

struct paris
{
	int garums;
	int cik;
} mas[1000000];

bool les(paris a, paris b)
{
	if (a.garums > b.garums)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int t;
int N,L;
long long T;
int C;

int main()
{
	freopen("B32.in", "rt", stdin);
	freopen("B32.out", "wt", stdout);

	cin >> t;

	long long atbilde = 0;

	for (int i = 1; i <= t; i++)
	{
		cin >> L >> T >> N >> C;
		long long atbilde = 0;

		for (int j = 0; j < C; j++)
		{
			cin >> mas[j].garums;
		}

		long long ciklagarums = 0;

		for (int j = 0; j < C; j++)
		{
			ciklagarums += mas[j].garums;
		}

		ciklagarums *= 2;

		long long pilnicikli = T / ciklagarums;

		for (int j = 0; j < C; j++)
		{
			mas[j].cik = N/C;

			if (N % C > j)
			{
				mas[j].cik++;
			}

			atbilde += 2 * ((long long) mas[j].cik) * mas[j].garums;

			mas[j].cik -= pilnicikli;
		}

		long long paliekpari = T % ciklagarums;

		int j = 0;

		while (2*mas[j].garums <= paliekpari)
		{
			mas[j].cik--;
			paliekpari -= 2*mas[j].garums;
			j++;
		}

		mas[C].cik = 0;

		if ((paliekpari > 0) && (mas[j].cik > 0))
		{
			mas[j].cik--;
			mas[C].garums = mas[j].garums - paliekpari / 2;
			mas[C].cik = 1;
			paliekpari = 0;
		}

		sort(mas, mas + C+1, les);

		for (int j = 0; j < C+1; j++)
		{
			if (mas[j].cik > 0)
			{
				int sk = min(L, mas[j].cik);

				atbilde -= ((long long) sk) * (mas[j].garums);

				L -= sk;
			}
		}

		printf("Case #%d: %lld\n", i,atbilde);
	}

	return 0;
}