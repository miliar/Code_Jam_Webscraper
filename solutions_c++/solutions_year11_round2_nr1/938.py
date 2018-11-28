#include <string>
#include <vector>
#include <iostream>

using std::string;
using std::vector;

double get_wp(int team, int skip, const vector<string>& games)
{
	int win = 0, total = 0;
	for (int j = 0; j < (int)games.size(); j++)
	{
		if (j == skip) continue;
		if (games[team][j] == '1')
			{win++; total++;}
		else if (games[team][j] == '0')
			total++;
	}
			
	return (double)win / total;
}

int main()
{
	int tests;
	std::cin >> tests;
	for (int currtest = 1; currtest <= tests; currtest++)
	{
		int n;
		std::cin >> n;
		vector<string> games(n);
		for (int i = 0; i < n; i++)
			std::cin >> games[i];
			
		vector<double> wp(n);
		vector<double> owp(n);
		vector<double> oowp(n);
			
		for (int i = 0; i < n; i++)
			wp[i] = get_wp(i, i, games);
		
		for (int i = 0; i < n; i++)
		{
			double sum = 0; int count = 0;
			for (int j = 0; j < n; j++)
				if (games[i][j] != '.')
				{
					sum += get_wp(j, i, games);
					count++;
				}
				
			owp[i] = sum / count;
		}
		
		for (int i = 0; i < n; i++)
		{
			double sum = 0; int count = 0;
			for (int j = 0; j < n; j++)
				if (games[i][j] != '.')
				{
					sum += owp[j];
					count++;
				}
				
			oowp[i] = sum / count;
		}
		
		std::printf("Case #%d:\n", currtest);
		for (int i = 0; i < n; i++)
			std::printf("%.12lf\n", 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]);
	}

	return 0;
}
