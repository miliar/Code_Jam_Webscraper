#include <iostream>
#include <string>

using namespace std;

int t;

int mas[100][100];

int P[100];
int W[100];
long double WP[100];
long double WPO[100];
long double WPOO[100];

int n;

string s;

int main()
{
	freopen("A2.in","rt",stdin);
	freopen("A2.out","wt",stdout);

	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &n);

		for (int j = 0; j < n; j++)
		{
			P[j] = 0;
			W[j] = 0;
			WP[j] = 0;
			WPO[j] = 0;
			WPOO[j] = 0;

			cin >> s;

			for (int k = 0; k < n; k++)
			{
				if (s[k] == '.')
				{
					mas[j][k] = -1;
				}
				else if (s[k] == '1')
				{
					mas[j][k] = 1;
					P[j]++;
					W[j]++;
				}
				else
				{
					mas[j][k] = 0;
					P[j]++;
				}
			}
		}

		for (int j = 0; j < n; j++)
		{
			WP[j] = ((long double) W[j]) / P[j];
		}

		for (int j = 0; j < n; j++)
		{
			long double sum = 0;

			for (int k = 0; k < n; k++)
			{
				if (mas[j][k] == 0)
				{
					sum += ((long double) W[k] - 1) / (P[k] - 1);
				}
				else if (mas[j][k] == 1)
				{
					sum += ((long double) W[k]) / (P[k] - 1);
				}
			}

			WPO[j] = sum / P[j];
		}


		for (int j = 0; j < n; j++)
		{
			long double sum = 0;

			for (int k = 0; k < n; k++)
			{
				if (mas[j][k] != -1)
				{
					sum += WPO[k];
				}
			}

			WPOO[j] = sum / P[j];
		}

		printf("Case #%d:\n", i);

		for (int j = 0; j < n; j++)
		{
			printf("%.12lf\n", 0.25 *WP[j] + 0.5*WPO[j] + 0.25*WPOO[j]);
		}

	}

	return 0;
}