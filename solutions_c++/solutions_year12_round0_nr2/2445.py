#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

#define max(A, B)	(A) > (B) ? (A) : (B)
#define min(A, B)	(A) < (B) ? (A) : (B)

using namespace std;

bool usable(int col1, int col2, int col3, bool surprise)
{
	vector<int>	v;

	v.push_back(col1);
	v.push_back(col2);
	v.push_back(col3);
	sort(v.begin(), v.end());
	int max_diff = v[2] - v[0];
	if (max_diff > 2)
		return false;
	return surprise ? max_diff == 2 : max_diff < 2;
}

bool is_possible(int S, int p, bool surprise)
{	
	for (int col1 = p; col1 <= 10; col1++)
	{
		int y1 = max(col1 - 2, 0);
		for (int col2 = y1; col2 <= col1; col2++)
		{
			int y = max(col2 - 2, 0);
			for (int col3 = y; col3 <= col1; col3++)
			{
				assert(col1 >= col2 && col1 >= col3);
				if(usable(col1, col2, col3, surprise) && (col1 + col2 + col3 == S))
				{
					//cout << S << " => " << col1 << ", " << col2 << ", " << col3;
					//if (surprise)
					//	cout << "*";
					//cout << endl;
					return true;
				}
			}
		}
	}
	return false;
}

int main()
{
	int		T, N, S, p;

	cin >> T;
	for (int caseno = 1; caseno <= T; caseno++)
	{
		int count = 0;
		cin >> N;
		cin >> S;
		cin >> p;
		vector<int> scores;
		for (int i = 1; i <= N; i++)
		{
			int ti;
			cin >> ti;
			scores.push_back(ti);
		}
		sort(scores.begin(), scores.end());
		for (int i = 0; i < S; i++)
		{
			for (int j = 0; j < scores.size(); j++)
			{
				if (scores[j] == -1)
					continue;
				if (is_possible(scores[j], p, true))
				{
					scores[j] = -1;
					count++;
					break;
				}
			}
		}
		for (int i = 0; i < scores.size(); i++)
		{
			if (scores[i] == -1)
				continue;
			if (is_possible(scores[i], p, false))
			{
				scores[i] = -1;
				count++;
			}
		}
		cout << "Case #" << caseno << ": " << count << endl;
	}
	return 0;
}
