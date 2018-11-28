#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int main(int paramc, char ** params)
{
	if (paramc > 1)
		freopen(params[1], "r", stdin);
	int t;
	scanf("%d", &t);
	for (int T = 0; T < t; ++T)
	{
		int n, blue = 1, orange = 1, moves = 0;
		string seq;
		vector <int> orangeMoves, blueMoves;
		scanf("%d", &n); char c; int x;
		for (int i = 0; i < n; ++i)
		{
			scanf(" %c %d", &c, &x);
			seq += c;
			if (c == 'B')
				blueMoves.push_back(x);
			else
				orangeMoves.push_back(x);
		}
		blueMoves.push_back(1);
		orangeMoves.push_back(1);
		reverse(blueMoves.begin(), blueMoves.end());
		reverse(orangeMoves.begin(), orangeMoves.end());
		int i = 0;
		while (i < n)
		{
			if (seq[i] == 'B' && blueMoves.back() == blue)
			{
				++i;
				blueMoves.pop_back();
				if (orange < orangeMoves.back())
					++orange;
				else if (orange > orangeMoves.back())
					--orange;
				++moves;
			}
			else if (seq[i] == 'O' && orangeMoves.back() == orange)
			{
				++i;
				orangeMoves.pop_back();
				if (blue < blueMoves.back())
					++blue;
				else if (blue > blueMoves.back())
					--blue;
				++moves;
			}
			else
			{
				if (orange < orangeMoves.back())
					++orange;
				else if (orange > orangeMoves.back())
					--orange;
				if (blue < blueMoves.back())
					++blue;
				else if (blue > blueMoves.back())
					--blue;
				++moves;
			}
		}
		printf("Case #%d: %d\n", T + 1, moves);
	}
	return 0;
}
