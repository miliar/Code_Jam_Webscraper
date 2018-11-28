#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int t,r,c,d;

int mas[500][500];
string s;


int main()
{
	freopen("B1.in", "rt", stdin);
	freopen("B1.out", "wt", stdout);

	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		cin >> r >> c >> d;

		for (int j = 0; j < r; j++)
		{
			cin >> s;

			for (int k = 0; k < c; k++)
			{
				mas[j][k] = s[k] - '0';
			}
		}

		int bestg = 1;

		for (int j = 0; j < r; j++)
		{
			for (int k = 0; k < c; k++)
			{
				long long kopsum = 0;
				long long kopsumx = 0;
				long long kopsumy = 0;


				for (int g = 2; j + g < r && k + g < c; g++)
				{
					if (g == 2)
					{
						for (int aa = 0; aa <= 2; aa++)
						{
							for (int bb = 0; bb <= 2; bb++)
							{
								kopsum += mas[j + aa][k + bb];
								kopsumx += 2*(bb-1)*mas[j+aa][k+bb];
								kopsumy += 2*(aa-1)*mas[j+aa][k+bb];
							}
						}
					}
					else
					{
						kopsumx -= kopsum;
						kopsumy -= kopsum;

						for (int aa = 0; aa <= g; aa++)
						{
							kopsum += mas[j+g][k+aa];
							kopsum += mas[j+aa][k+g];

							kopsumx += mas[j+aa][k+g] * g;
							kopsumy += mas[j+aa][k+g] * (2*aa - g);

							kopsumy += mas[j+g][k+aa] * g;
							kopsumx += mas[j+g][k+aa] * (2*aa - g);
						}

						kopsum -= mas[j+g][k+g];
						kopsumx -= mas[j+g][k+g] * g;
						kopsumy -= mas[j+g][k+g] * g;
					}

					if ((kopsumx + g*(mas[j][k] + mas[j+g][k] - mas[j][k+g] - mas[j+g][k+g]) == 0) &&
						(kopsumy + g*(mas[j][k] + mas[j][k+g] - mas[j+g][k] - mas[j+g][k+g]) == 0))
					{
						if (g > bestg)
						{
							bestg = g;

//							cout << j << " " << k << endl;
						}
					}
				}
			}
		}

		cout << "Case #" << i << ": ";

		if (bestg > 1)
		{
			cout << bestg+ 1 << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}