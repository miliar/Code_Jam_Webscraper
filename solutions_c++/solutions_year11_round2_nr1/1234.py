#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ofstream outf;
	outf.open("1b1.out",ios::out);
	int t;
	int k;
	cin >> t;
	int i,j;
	for (k = 1;k <= t;k++)
	{
		outf << "Case #" << k <<": " << endl;
		int n;
		cin >> n;
		char m[100][100];
		for (i = 0;i < n;i++)
			for (j = 0;j < n;j++)
				cin >> m[i][j];
		double wp1[100] = {0};
		double wp2[100] = {0};
		double owp[100];
		double oowp[100];
		double cnt[100] = {0};
		double win[100] = {0};
		double lose[100] = {0};
		for (i = 0;i < n;i++)
		{
			for (j = 0;j < n;j++)
			{
				if (m[i][j] != '.')
				{
					cnt[i]++;
					if (m[i][j] == '0')
						lose[i]++;
					else
						win[i]++;
				}
			}
			if (cnt[i] != 0)
				wp1[i] = win[i]/cnt[i];
			else
				wp1[i] = 0;
		}

		for (i = 0;i < n;i++)
		{
			double sum = 0;
			for (j = 0;j < n;j++)
			{
				if (m[j][i] == '0')
				{
					wp2[j] = (win[j])/(cnt[j] - 1);
					sum += wp2[j];
				}
				else
				{
					if (m[j][i] == '1')
					{
						wp2[j] = (win[j] - 1)/(cnt[j] - 1);
						sum += wp2[j];
					}
				}
			}
			owp[i] = sum/cnt[i];
		}

		for (i = 0;i < n;i++)
		{
			double sum = 0;
			for (j = 0;j < n;j++)
			{
				if (m[i][j] != '.')
					sum += owp[j];
			}
			oowp[i] = sum/cnt[i];
		}

		for (i = 0;i < n;i++)
			outf << setiosflags(ios::fixed) <<setprecision(6) << 0.25*wp1[i]+0.50*owp[i]+0.25*oowp[i] << endl;
	}
	return 0;
}



			
					


