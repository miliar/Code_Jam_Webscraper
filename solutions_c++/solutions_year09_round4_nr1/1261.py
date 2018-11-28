#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;

struct State
{
	vector<int> st;
	int times;
};

bool IsGood(vector<int>& v)
{
	for (int i = 0; i < (int)v.size(); i++)
	{
		if (v[i] > i)
			return false;
	}
	return true;
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t = 0;
	fin >> t;
	for (int i = 0; i < t; i++)
	{
		int d = 0;
		fin >> d;
		string line;
		vector<int> rows;
		set<vector<int> > visited;
		for (int j = 0; j < d; j++)
		{
			fin >> line;
			int count = 0;
			for (int k = 1; k < (int)line.size(); k++)
				if (line[k] == '1')
					count = k;
			rows.push_back(count);
		}

		int res = 0;

		queue<State> q;
		State st;
		st.st = rows;
		st.times = 0;

		if (IsGood(rows))
			res = 0;
		else
			q.push(st);

		visited.insert(rows);

		while (!q.empty() && res == 0)
		{
			st = q.front();
			q.pop();

			for (int j = 0; j < (int)st.st.size() - 1 && res == 0; j++)
			{
				swap(st.st[j], st.st[j + 1]);
				if (visited.find(st.st) == visited.end())
				{
					if (IsGood(st.st))
					{
						res = st.times + 1;
						break;
					}
					State newState;
					newState.st = st.st;
					newState.times = st.times + 1;
					visited.insert(st.st);
					q.push(newState);
				}
				swap(st.st[j], st.st[j + 1]);
			}
		}

		fout << "Case #" << i + 1 << ": " << res << endl; 
	}
	return 0;
}