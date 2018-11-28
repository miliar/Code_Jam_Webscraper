#include <iostream>
#include <string>

using namespace std;

void oneCase();

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << (i + 1) << ": " << endl;
		oneCase();
	}

	return 0;
}

void oneCase()
{
	int t;
	cin >> t;

	bool played[100][100] = { false };
	double wins[100][101] = { 0.0 };
	double games[100][101] = { 0.0 };

	string s;
	for (int i = 0; i < t; i++)
	{
		cin >> s;
		for (int j = 0; j < t; j++)
		{
			if (s[j] == '.') continue;
			
			played[i][j] = true;
			games[i][t]++;
			if (s[j] == '1')
			{
				wins[i][t]++;
			}
			for (int k = 0; k < t; k++)
			{
				if (k != j)
				{
					games[i][k]++;
					if (s[j] == '1')
					{
						wins[i][k]++;
					}
				}
			}
		}
	}

	double OWP[100] = {0.0};
	double OWPP[100] = {0.0};

	for (int i = 0; i < t; i++)
	{
		double total = 0.0;
		double count = 0.0;
		for (int j = 0; j < t; j++)
		{
			if (played[i][j])
			{
				count++;
				total += (wins[j][i] / games[j][i]);
			}
		}
		OWP[i] = total / count;
	}

	for (int i = 0; i < t; i++)
	{
		double total = 0.0;
		double count = 0.0;

		for (int j =0; j < t; j++)
		{
			if (played[i][j])
			{
				count++;
				total += OWP[j];
			}
		}

		OWPP[i] = total / count;
	}

	for (int i = 0; i < t; i++)
	{
		double RPI = 0.0;
		RPI += 0.25 * (wins[i][t] / games[i][t]);
		RPI += 0.50 * OWP[i];
		RPI += 0.25 * OWPP[i];
		cout << RPI << endl;
	}
}