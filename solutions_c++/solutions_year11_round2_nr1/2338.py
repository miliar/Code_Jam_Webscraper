#include <fstream>

using namespace::std;

int main()
{
	int T, K;
	int i, j, m;
	char data[102][102];
	double RIP[102];
	double WP[102], OWP[102], OOWP[102];
	int Times[102];
	ifstream input("D:\\a.txt", ifstream::in);
	ofstream output("D:\\b.txt", ofstream::out);

	input >> T;
	
	for (i = 0; i < T; i++)
	{
		output << "Case #" << i + 1 << ":" << endl;
		input >> K;
		memset(data, 0, sizeof data);
		memset(RIP, 0, sizeof RIP);
		memset(WP, 0, sizeof WP);
		memset(OWP, 0, sizeof OWP);
		memset(OOWP, 0, sizeof OOWP);
		memset(Times, 0, sizeof Times);
		for (j = 0; j < K; j++)
		{
			for (m = 0; m < K; m++)
			{
				input >> data[j][m];
				if (data[j][m] != '.')
				{
					Times[j]++;
				}

				if (data[j][m] == '1')
				{
					WP[j] += 1;
				}
			}
			WP[j] = WP[j] / Times[j];
		}

		for (j = 0; j < K; j++)
		{
			for (m = 0; m < K; m++)
			{
				if (data[j][m] == '0')
				{
					OWP[j] += (WP[m] * Times[m] - 1) / (Times[m] - 1);
				}
				else if (data[j][m] == '1')
				{
					OWP[j] += WP[m] * Times[m] / (Times[m] - 1);
				}
			}

			OWP[j] = OWP[j] / Times[j];
		}

		for (j = 0; j < K; j++)
		{
			for (m = 0; m < K; m++)
			{
				if (data[j][m] != '.')
				{
					OOWP[j] += OWP[m];
				}
			}

			OOWP[j] = OOWP[j] / Times[j];

			output << 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j] << endl;
		}

		
	}

	return 0;
}