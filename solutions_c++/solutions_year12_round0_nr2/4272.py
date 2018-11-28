#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<iostream>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<bitset>
#include<list>
using namespace std;

int main()
{
	/*	freopen("d:\\A-small-attempt0.in", "r", stdin);
	 freopen("d:\\a.txt", "w", stdout);*/
	int T, N, S, P;
	int sum, score;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{

		sum = 0;
		cin >> N >> S >> P;
		vector<int> triplets;
		for (int j = 0; j < N; ++j)
		{
			cin >> score;
			int temp = score % 3;
			if ((score == 0) && (P == 0))
			{
				sum++;
			}
			if ((temp == 1) && (score / 3 + 1) >= P)
			{
				sum++;
			}
			else if (temp == 2)
			{
				triplets.push_back(score / 3 + 1);
			}
			else if (temp == 0 && score != 0)
			{
				triplets.push_back(score / 3);
			}
		}
		sort(triplets.begin(), triplets.end());
		for (unsigned int k = 0; k < triplets.size(); ++k)
		{

			if (triplets[k] >= P)
				sum++;
			else if (triplets[k] + 1 >= P)
			{
				if (S > 0)
				{
					S--;
					sum++;
				}
			}
		}

		cout << "Case #" << i << ": " << sum << endl;
	}
	return 0;
}
