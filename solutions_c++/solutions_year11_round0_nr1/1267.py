#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long i64;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T sqr(const T &a) {
	return a * a;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testnum;
	cin >> testnum;
	for (int tc = 0; tc < testnum; tc++)
	{
		int n;
		cin >> n;
		vector<pair<int, string> > m(n);
		for (int i = 0; i < n; i++)
			cin >> m[i].second >> m[i].first;
		int time = 0;
		int onxt, bnxt, ocur = 1, bcur = 1;
		for (int i = 0; i < n; i++)
		{
			onxt = ocur, bnxt = bcur;
			for (int j = i; j < n; j++)
				if (m[j].second == "O")
				{
					onxt = m[j].first;
					break;
				}
			for (int j = i; j < n; j++)
				if (m[j].second == "B")
				{
					bnxt = m[j].first;
					break;
				}
			if (m[i].second == "O")
			{
				int cur = abs(onxt - ocur) + 1;
				ocur = onxt;
				if (abs(bnxt - bcur) < cur)
					bcur = bnxt;
				else if (bcur < bnxt)
					bcur += cur;
				else
					bcur -= cur;
				time += cur;
			}
			else
			{
				int cur = abs(bnxt - bcur) + 1;
				bcur = bnxt;
				if (abs(onxt - ocur) < cur)
					ocur = onxt;
				else if (ocur < onxt)
					ocur += cur;
				else
					ocur -= cur;
				time += cur;
			}
		}
		cout << "Case #" << tc + 1 << ": " << time << endl;
	}
	return 0;
}
