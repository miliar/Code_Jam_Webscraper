#include <iostream>
using namespace std;

char table[128][128];
double WP[128], OWP[128], OOWP[128];

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> table[i];
		for (int i = 0; i < n; i++)
		{
			int total = 0, won = 0;
			for (int j = 0; j < n; j++)
				if (table[i][j] != '.')
				{
					total++;
					if (table[i][j] == '1')
						won++;
				}
			WP[i] = (double)won / total;
		}
		for (int i = 0; i < n; i++)
		{
			int summands = 0;
			double sum = 0.0;
			for (int j = 0; j < n; j++)
				if (table[i][j] != '.')
				{
					int total = 0, won = 0;
					for (int k = 0; k < n; k++)
						if (k != i && table[j][k] != '.')
						{
							total++;
							if (table[j][k] == '1')
								won++;
						}
					summands++;
					sum += (double)won / total;
				}
			OWP[i] = sum / summands;
		}
		for (int i = 0; i < n; i++)
		{
			int summands = 0;
			double sum = 0.0;
			for (int j = 0; j < n; j++)
				if (table[i][j] != '.')
				{
					summands++;
					sum += OWP[j];
				}
			OOWP[i] = sum / summands;
		}

		printf("Case #%d:\n", kase);
		for (int i = 0; i < n; i++)
			printf("%.12lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	}
	return 0;
}
