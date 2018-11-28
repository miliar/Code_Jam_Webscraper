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

const string filename = "B-large";

int main ()
{
	ifstream fin ((filename + ".in" ).c_str());
	ofstream fout((filename + ".out").c_str());

	int t, N, i;

	fin >> N;
	for (t = 0; t < N; t++)
	{
		string line;
		int T, NA, NB;
		int h, m, n1, n2;
		vector<int> need_a;
		vector<int> need_b;
		vector<int> present_a;
		vector<int> present_b;

		fin >> T;
		fin >> NA >> NB;
		getline (fin, line);
		for (i = 0; i < NA; i++)
		{
			getline (fin, line);
			h = (line[0]-'0') * 10 + (line[1]-'0');
			m = (line[3]-'0') * 10 + (line[4]-'0');
			n1 = h * 60 + m;
			h = (line[6]-'0') * 10 + (line[7]-'0');
			m = (line[9]-'0') * 10 + (line[10]-'0');
			n2 = h * 60 + m;
			need_a.push_back (n1);
			present_b.push_back (n2 + T);
		}
		for (i = 0; i < NB; i++)
		{
			getline (fin, line);
			h = (line[0]-'0') * 10 + (line[1]-'0');
			m = (line[3]-'0') * 10 + (line[4]-'0');
			n1 = h * 60 + m;
			h = (line[6]-'0') * 10 + (line[7]-'0');
			m = (line[9]-'0') * 10 + (line[10]-'0');
			n2 = h * 60 + m;
			need_b.push_back (n1);
			present_a.push_back (n2 + T);
		}

		sort (need_a.begin(), need_a.end());
		sort (need_b.begin(), need_b.end());
		sort (present_a.begin(), present_a.end());
		sort (present_b.begin(), present_b.end());

		int j, n_a = 0, n_b = 0;
		vector<bool> p_a (present_a.size(), false);
		vector<bool> p_b (present_b.size(), false);
		for (i = 0; i < need_a.size(); i++)
		{
			for (j = 0; j < present_a.size(); j++)
				if (present_a[j] <= need_a[i] && p_a[j] == false)
				{
					p_a[j] = true;
					break;
				}
			if (j >= present_a.size())
				n_a++;
		}
		for (i = 0; i < need_b.size(); i++)
		{
			for (j = 0; j < present_b.size(); j++)
				if (present_b[j] <= need_b[i] && p_b[j] == false)
				{
					p_b[j] = true;
					break;
				}
			if (j >= present_b.size())
				n_b++;
		}

		fout << "Case #" << t + 1 << ": " << n_a << " " << n_b << endl;
	}

	return 0;
}