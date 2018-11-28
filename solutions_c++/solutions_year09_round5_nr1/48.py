#include <cstdio>
#include <queue>
#include <set>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int dxy[4][2] = { {0, 1}, {0, -1}, {-1, 0}, {1, 0} };

class boxes
{
public:
	set <pair<int, int> > B;
	int con;

	boxes(){
		con = -1;
	}

	bool connected()
	{
		set <pair<int, int> > bio;
		queue <pair <int,int> > Q;

		pair <int,int> s = *(B.begin());

		bio.insert(s);
		Q.push(s);

		while(Q.size())
		{
			s = Q.front(); Q.pop();

			for (int i = 0; i < 4; ++i)
			{
				pair <int,int> t(s.first+dxy[i][0], s.second+dxy[i][1]);
				if (bio.count(t) == 0 && B.count(t) != 0)
				{
					bio.insert(t);
					Q.push(t);
				}
			}
		}

		return bio.size() == B.size();
	}
};

bool operator == (const boxes &a, const boxes &b)
{
	set <pair<int, int> >::iterator itr1, itr2;

	for (itr1 = a.B.begin(), itr2 = b.B.begin(); itr1 != a.B.end(); ++itr1, ++itr2)
	{
		if (*itr1 != *itr2) return false;
	}

	return true;
}

bool operator < (const boxes &a, const boxes &b)
{
	set <pair<int, int> >::iterator itr1, itr2;

	for (itr1 = a.B.begin(), itr2 = b.B.begin(); itr1 != a.B.end(); ++itr1, ++itr2)
	{
		if (*itr1 != *itr2) return (*itr1) < (*itr2);
	}

	return false;
}

int R, C;
map <boxes, int> minDistance;
char polje[16][16];
boxes start, end;

bool valid(boxes& s)
{
	for (set<pair<int,int> >::iterator itr = s.B.begin(); itr != s.B.end(); ++itr)
	{
		if (itr->first < 0 || itr->first >= R || itr->second < 0 || itr->second >= C) return false;
		if (polje[itr->first][itr->second] == '#') return false;
	}

	return true;
}

bool valid(pair <int,int> t)
{
	if (t.first < 0 || t.first >= R || t.second < 0 || t.second >= C) return false;
	if (polje[t.first][t.second] == '#') return false;

	return true;
}

void load()
{
	scanf("%d%d", &R, &C);

	end.B.clear();
	start.B.clear();

	for (int i = 0; i < R; ++i)
	{
		scanf("%s", polje[i]);
		for (int k = 0; k < C; ++k)
		{
			if (polje[i][k] == 'x' || polje[i][k] == 'w') end.B.insert(make_pair(i, k));
			if (polje[i][k] == 'o' || polje[i][k] == 'w') start.B.insert(make_pair(i, k));
		}
	}

	end.con = 1;
	start.con = 1;
}

int solve()
{
	if (start == end) return 0;

	queue <boxes> Q;
	minDistance.clear();
	boxes s, t;
	Q.push(start);
	minDistance[start] = 0;

	do{
		s = Q.front(); Q.pop();

		int sd = minDistance[s];

		for (set <pair <int,int> >::iterator itr = s.B.begin(); itr != s.B.end(); ++itr)
		{
			for (int p = 0; p < 4; ++p)
			{
				pair <int, int> tp(itr->first + dxy[p][0], itr->second + dxy[p][1]);
				pair <int, int> tc(itr->first - dxy[p][0], itr->second - dxy[p][1]);
				if (s.B.count(tp) || s.B.count(tc)) continue;
				if (valid(tc) == 0) continue;

				t = s;
				t.B.erase(*itr);
				t.B.insert(tp);

				t.con = t.connected();

				if (t.con == 0 && s.con == 0) continue;
				if (valid(t) == 0) continue;
				if (minDistance.count(t) != 0) continue;

				if (t == end) return sd+1;

				minDistance[t] = sd+1;
				Q.push(t);
			}
		}

	}while(Q.size());

	return -1;
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; ++tt)
	{
		load();

		printf("Case #%d: %d\n", tt, solve());
	}


	return 0;
}
