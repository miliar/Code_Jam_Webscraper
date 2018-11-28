#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
using namespace std;
#define sz(a) (int)((a).size())
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(), (a).end()
typedef pair<int, int> pii;
typedef vector<int> vint;
typedef long long lint;

int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

int R, C;

inline bool Valid(int r, int c)
{
	return r >= 0 && r < R && c >= 0 && c < C;
}

char Letter[111][111];
pii Par[111][111];
int H[111][111];

void MakeSet(pii p)
{
	Par[p.first][p.second] = p;
}
pii FindSet(pii p)
{
	if(Par[p.first][p.second] == p)
		return p;
	return Par[p.first][p.second] = FindSet(Par[p.first][p.second]);
}
void Link(pii p, pii t)
{
	Par[p.first][p.second] = t;
}
void Union(pii p, pii t)
{
	if(FindSet(p) == FindSet(t))
		return;
	Link(FindSet(p), FindSet(t));
}

bool Solve(int test)
{
	scanf("%d %d", &R, &C);
	for(int r = 0; r < R; ++r)
		for(int c = 0; c < C; ++c)
		{
			MakeSet(mp(r, c));
			Letter[r][c] = 0;
			scanf("%d", &H[r][c]);
		}
	for(int r = 0; r < R; ++r)
		for(int c = 0; c < C; ++c)
		{
			int minh = 1 << 20;
			for(int i = 0; i < 4; ++i)
			{
				int rr = r + dr[i];
				int cc = c + dc[i];
				if(Valid(rr, cc))
					minh = min(minh, H[rr][cc]);
			}
			if(minh >= H[r][c])
				continue;
			for(int i = 0; i < 4; ++i)
			{
				int rr = r + dr[i];
				int cc = c + dc[i];
				if(Valid(rr, cc) && H[rr][cc] == minh)
				{
					Union(mp(r, c), mp(rr, cc));
					break;
				}
			}
		}
	char letter = 'a';
	printf("Case #%d:\n", test);
	for(int r = 0; r < R; ++r)
	{
		for(int c = 0; c < C; ++c)
		{
			if(c)
				printf(" ");
			pii p = FindSet(mp(r, c));
			if(!Letter[p.first][p.second])
				Letter[p.first][p.second] = letter++;
			printf("%c", Letter[p.first][p.second]);
		}
		printf("\n");
	}
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//*/while(Solve(++t));
	return 0;
}