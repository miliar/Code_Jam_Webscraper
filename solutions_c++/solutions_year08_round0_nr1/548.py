#pragma warning (disable : 4018)

#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

const string filename = "A-large";

int main ()
{
	ifstream fin ((filename + ".in" ).c_str());
	ofstream fout((filename + ".out").c_str());

	int T, N, i;

	fin >> N;
	for (T = 0; T < N; T++)
	{
		int S, Q;
		vector<string> s, q;
		map<string, int> se_map;

		string str;
		fin >> S;
		getline (fin, str);
		for (i = 0; i < S; i++)
		{
			getline (fin, str);
			s.push_back (str);
			se_map[str] = i;
		}
		fin >> Q;
		getline (fin, str);
		for (i = 0; i < Q; i++)
		{
			getline (fin, str);
			q.push_back (str);
		}

		int ans = 0, cur_se = -1;
		int se_index = 0, q_index = 0;
		while (0 == 0)
		{
			vector<bool> selected (s.size(), false);
			if (cur_se >= 0)
				selected[cur_se] = true;
			for (; q_index < Q; q_index++)
			{
				for (se_index = 0; se_index < s.size(); se_index++)
					if (s[se_index] == q[q_index])
						break;
				if (se_index < s.size())
					selected[se_index] = true;
				for (i = 0; i < s.size(); i++)
					if (selected[i] == false)
						break;
				if (i >= s.size())
				{
					cur_se = se_index;
					break;
				}
			}

			if (q_index >= Q)
				break;

			ans++;
		}

		fout << "Case #" << T + 1 << ": " << ans << endl;
	}

	return 0;
}