#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <set>
#include <utility>

using namespace std;

pair<string, int> longest(const vector<string>& engine,
						  const string& skip,
						  vector<string>::const_iterator qb,
						  vector<string>::const_iterator qe);

bool comp(pair<string, int> lhs, pair<string, int> rhs);

void walk(const vector<string>& engine,
		  vector<string>::const_iterator qb,
		  vector<string>::const_iterator qe,
		  vector<string>& step)
{
	if (qb == qe)
		return;

	string skip;
	if (!step.empty())
		skip = step.back();

	pair<string, int> long_pair = longest(engine, skip, qb, qe);

	step.push_back(long_pair.first);

	walk(engine, qb + long_pair.second, qe, step);
}

pair<string, int> longest(const vector<string>& engine,
						  const string& skip,
						  vector<string>::const_iterator qb,
						  vector<string>::const_iterator qe)
{
	map<string, int> far_map;

	for (vector<string>::const_iterator i = engine.begin();
		i != engine.end(); ++i)
	{
		if (*i == skip)
			continue;

		int far = 0;
		vector<string>::const_iterator j = qb;

		while (j != qe && *j != *i)
		{
			++j;
			++far;
		}
		far_map[*i] = far;
	}

	return *max_element(far_map.begin(), far_map.end(), comp);
}

bool comp(pair<string, int> lhs, pair<string, int> rhs)
{
	return lhs.second < rhs.second;
}

int main()
{
	int N;
	cin >> N;

	for (int i = 1; i <= N; ++i)
	{
		vector<string> engine;
		string e;
		int S;
		cin >> S;

		cin.get();
		for (int j = 0; j < S; ++j)
		{
			getline(cin, e);
			engine.push_back(e);
		}

		vector<string> query;
		string q;
		int Q;
		cin >> Q;

		cin.get();
		for (int j = 0; j < Q; ++j)
		{
			getline(cin, q);
			query.push_back(q);
		}

		vector<string> step;
		walk(engine, query.begin(), query.end(), step);

		int s = step.empty() ? 0 : step.size() - 1;

		cout << "Case #" << i << ": " << s << endl;
	}

	return 0;
}