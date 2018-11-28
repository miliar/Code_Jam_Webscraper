#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cctype>
#include <queue>
#include <deque>
#include <list>

using namespace std;

void Solve()
{
	int n;
	cin >> n;

	deque< int > aim[2];
	deque< pair< bool, int > > all;

	for (int i = 0; i < n; ++ i)
	{
		char c;
		int pos;
		cin >> c >> pos;
		all.push_back(make_pair(c == 'O', pos));
		aim[c == 'O'].push_back(pos);
	}

	if (aim[0].empty()) aim[0].push_back(1);
	else aim[0].push_back(aim[0].back());
	if (aim[1].empty()) aim[1].push_back(1);
	else aim[1].push_back(aim[1].back());

	int pos[2];
	pos[0] = pos[1] = 1;

	int t = 0;

	while (!all.empty())
	{
		bool A, B;
		A = all.front().first;
		B = !A;

		int add = abs(all.front().second - pos[A]) + 1;
		t += add;

		pos[A] = all.front().second;
		if (pos[B] < aim[B].front())
		{
			pos[B] = min(aim[B].front(), pos[B] + add);
		}
		else if (pos[B] > aim[B].front())
		{
			pos[B] = max(aim[B].front(), pos[B] - add);
		}

		aim[A].pop_front();
		all.pop_front();
	}	

	cout << t << endl;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int testCnt;
	cin >> testCnt;

	for (int test = 1; test <= testCnt; ++ test)
	{
		cout << "Case #" << test << ": ";
		Solve();
	}

	return 0;
}