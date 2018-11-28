#include <iostream>
#include <memory.h>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;

typedef string answer_type;

template <typename T>
ostream& operator <<(ostream& out, vector<T> V)
{
	for (int i = 0; i < V.size(); i++)
		out << V[i] << ' ';
	return out;
}

const int N = 100;

bool cont(vector<int> v, int a)
{
	for (int i = 0; i < v.size(); i++)
		if (v[i] == a)
			return true;
	return false;
}

bool bad(vector<int> v, int tr, vector<int>& col)
{
	bool bbb[N];
	memset(bbb, 0, sizeof(bbb));
	for (int i = 0; i < v.size(); i++)
		bbb[col[v[i] - 1]] = 1;
	for (int i = 1; i <= tr; i++)
		if (!bbb[i])
			return true;
	return false;
}

answer_type solve()
{
	int n, m;
	cin >> n >> m;
	set<vector<int> > S;
	vector<int> init(n);
	for (int i = 0; i < n; i++)
		init[i] = i + 1;
	S.insert(init);
	int beg[N], end[N];
	for (int i = 0; i < m; i++)
		cin >> beg[i];
	for (int i = 0; i < m; i++)
		cin >> end[i];
	for (int i = 0; i < m; i++)
	{
		for (auto it = S.begin(); it != S.end(); it++)
		{
			if (cont(*it, beg[i]) && cont(*it, end[i]))
			{
				vector<int> A[2];
				int cur = 0;
				for (int j = 0; j < it->size(); j++)
				{
					if ((*it)[j] == beg[i] || (*it)[j] == end[i])
						A[cur].push_back((*it)[j]), cur ^= 1;
					A[cur].push_back((*it)[j]);
				}
				S.erase(*it);
				S.insert(A[0]);
				S.insert(A[1]);
				goto nexti;
			}
		}
	nexti:;
	}
	
	for (auto it = S.begin(); it != S.end(); it++)
		cerr << *it << endl;
	vector<int> gcol(n);
	int best = 0;
	vector<int> col(n);
	for (int tr = 1; tr <= n; tr++)
	{
		for (int msk = 0, _msk = 0; msk < pow((double)tr, (double)n) + 2; _msk = ++msk)
		{
			for (int i = 0; i < n; i++)
				col[i] = _msk % tr + 1, _msk /= tr;	
			for (auto it = S.begin(); it != S.end(); it++)
			{
				if (bad(*it, tr, col))
					goto nextmsk;
			}
			gcol = col;
			best = tr;
			goto nexttr;
			nextmsk:;
		}
		break;
		nexttr:;
	}
	stringstream ans;
	ans << best << endl << gcol;
	return ans.str();
}

int main()
{
	int T;
	cin >> T;
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
