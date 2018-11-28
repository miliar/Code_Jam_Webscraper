#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long lol;

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

int C, D, N;
string S;
string c[111], d[111];

void solve(int testcase)
{
	cin >> C;
	for (int i = 0; i < C; ++i) cin >> c[i];
	cin >> D;
	for (int i = 0; i < D; ++i) cin >> d[i];
	cin >> N;
	cin >> S;

	string list;
	for (int i = 0; i < N; ++i)
	{
		if (!list.empty())
		{
			int last = sz(list) - 1;
			for (int j = 0; j < C; ++j)
				if ((c[j][0] == list[last] && c[j][1] == S[i]) || (c[j][0] == S[i] && c[j][1] == list[last]))
				{
					list[last] = c[j][2];
					last = -1;
					break;
				}
			if (last == -1) continue;
			for (int j = 0; j < D; ++j)
				if (d[j][0] == S[i] || d[j][1] == S[i])
				{
					char c = d[j][0] == S[i] ? d[j][1] : d[j][0];
					if ((int) list.find(c) != -1) 
					{
						list.clear();
						break;
					}
				}
			if (!list.empty()) list += S[i];
		}
		else
			list += S[i];
	}

	printf("Case #%d: ", testcase);
	printf("[");
	for (int i = 0; i < sz(list); ++i)
	{
		if (i > 0) printf(", ");
		printf("%c", list[i]);
	}
	printf("]");
	puts("");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) solve(i);
	return 0;
}
