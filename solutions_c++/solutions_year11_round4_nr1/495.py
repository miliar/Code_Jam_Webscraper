#include <iostream>
#include <algorithm>

using namespace std;

int t;

struct nogr
{
	int gar;
	int w;
} mas[1000000];

bool les(nogr a, nogr b)
{
	if (a.w < b.w)
	{
		return true;
	}
	else
	{
		return false;
	}
}

long double T;
int X,S,R,N;
long double atbilde;

int x,y,w;

int main()
{
	freopen("A2.in", "rt", stdin);
	freopen("A2.out", "wt", stdout);

	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		double atbilde = 0;
		cin >> X >> S >> R >> T >> N;

		int Z = X;

		for (int j = 0; j < N; j++)
		{
			cin >> x >> y >> w;
			mas[j].gar = y-x;
			mas[j].w = w + S;

			atbilde += ((double) mas[j].gar) / mas[j].w;

			Z -= mas[j].gar;
		}

		mas[N].gar = Z;
		mas[N].w = S;

		atbilde += ((double) mas[N].gar) / mas[N].w;


		sort(mas, mas+N+1, les);

		int ind = 0;

		if (R > S)
		{
			while (T > 0 && ind < N+1)
			{
				//vai var visu noskriet?

				if (mas[ind].gar <= T * (mas[ind].w + R - S))
				{
					atbilde -= ((double) mas[ind].gar) / mas[ind].w;
					double laiks = ((double) mas[ind].gar) / (mas[ind].w + R - S);
					T -= laiks;
					atbilde += laiks;
				}
				else
				{
					double dist = T * (mas[ind].w + R - S);

					atbilde -= ((double) dist) / mas[ind].w;
					double laiks = ((double) dist) / (mas[ind].w + R - S);
					T = 0;
					atbilde += laiks;

				}

				ind++;
			}
		}

		cout << "Case #" << i << ": ";
		printf("%.9f\n", atbilde);
	}

	return 0;
}