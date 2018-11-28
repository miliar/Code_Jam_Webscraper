#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;
fstream inp, out;

/*!
u1ik's Sokoban Solver (breadth-first search over state space).
Copyright (C) 2007  Ulan Degenbaev (udegenbaev@gmail.com)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
*/

#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int N   = 13;
int n, m;
char mp[N][N];
bool wp[N][N];
bool bx[N][N];

long long cellid[N][N]; /// id of a reacheable cell
vector <pair <int, int> > idcell;	/// reachable cell by id
char dc[4] = {'D', 'L', 'U', 'R'};
int  di[4] = {1, 0, -1, 0};
int  dj[4] = {0, -1, 0, 1};
int cells;


/// maps positions to state space
long long encode(const vector <pair <int, int> > & boxes, bool stable)
{
	long long k = 0;
	for (int i = 0; i < boxes.size(); ++i)
	{
		k = k * (cells) + cellid[boxes[i].first][boxes[i].second];
	}
	return k * 2 + (stable);
}

/// maps state space to positions
void decode(long long k, vector <pair <int, int> > & boxes, bool & stable)
{
    stable = k % 2; k /= 2;
	for (int i = ((int)boxes.size()) - 1; i >= 0; --i)
	{
		boxes[i] = idcell[k % cells];
		k /= (cells);
	}
	
}

int go(int i, int j)
{
    if (wp[i][j]) return 0;
    wp[i][j] = true;
    int cnt = 1;
    for (int dir = 0; dir < 4; ++dir)
    {
	    int ni = i + di[dir];
	    int nj = j + dj[dir];
	    if (ni < 0 || nj < 0 || ni >= m || nj >= n) continue;
	    if (!bx[ni][nj]) continue;
        cnt += go(ni, nj);
    }
    return cnt;
}

int solve()
{
    /// used for breadth-first search
    vector <pair <int, int > > boxes, new_boxes;
    vector <pair <int, int > > dests, new_dests;
    bool stable, new_stable;

	memset(mp, '.', sizeof(mp));
	memset(wp, 0, sizeof(wp));
	memset(bx, 0, sizeof(bx));
	idcell.clear();
	char s[2*N];	
	inp >> m >> n;
	for (int i = 0; i < m; ++i)
	{
	    inp >> mp[i];
	}
	for (int i = 0; i < m; ++i)
		for (int j = 0; j < n; ++j)
		{
			switch (mp[i][j])
			{
			case 'o':	//box
						mp[i][j] = '.';
						boxes.push_back(make_pair(i, j));
						break;
			case 'x':	//destination
						mp[i][j] = '.';
						dests.push_back(make_pair(i, j)); 
						break;
			case 'w':	//box at destination
						mp[i][j] = '.';
						boxes.push_back(make_pair(i, j)); 
						dests.push_back(make_pair(i, j));
						break;
			}
		}
    for (int i = 0; i < m; ++i)
        cout << mp[i] << endl;
    cells = 0;
	for (int i = 0; i < m; ++i)
	for (int j = 0; j < n; ++j)
	{
	    cellid[i][j] = cells++;
	    idcell.push_back(make_pair(i, j));
	}
    
    queue<long long> qu[2];
    
    std::map<long long, bool> was;
    
	long long k = encode(boxes, true);
	
	qu[0].push(k);
	int T;
	for (T = 0; !qu[T&1].empty() ; ++T)
	{
		if (T % 100 == 0) printf("%d moves checked\n", T);
		while (!qu[T&1].empty())
		{
			k = qu[T&1].front();
			qu[T&1].pop();
			decode(k, boxes, stable);
			for (int i = 0; i < boxes.size(); ++i)
			{
				bx[boxes[i].first][boxes[i].second] = true;
			}
			bool finish = true;
			for (int i = 0; i < dests.size() && finish; ++i)
				if (!bx[dests[i].first][dests[i].second]) finish = false;
		    
			if (finish)
			{
				printf("Best solution uses %d steps\n", T);
				return T;
			}
			for (int i = 0; i < boxes.size(); ++i)
			{
			    int bi = boxes[i].first;
			    int bj = boxes[i].second;
			    for (int dir = 0; dir < 4; ++dir)
			    {
				    new_boxes = boxes;
				    int mi = bi - di[dir];
				    int mj = bj - dj[dir];
				    if (mi < 0 || mj < 0 || mi >= m || mj >= n) continue;
				    if (mp[mi][mj] != '.' || bx[mi][mj]) continue;
				    int ni = bi + di[dir];
				    int nj = bj + dj[dir];
				    if (ni < 0 || nj < 0 || ni >= m || nj >= n) continue;
				    if (mp[ni][nj] != '.' || bx[ni][nj]) continue;
				    new_boxes[i].first = ni;
				    new_boxes[i].second = nj;
				    sort(new_boxes.begin(), new_boxes.end());
				    bx[bi][bj] = false;
				    bx[ni][nj] = true;
			        //cout << "------------ " << endl;
           //         for (int i = 0; i < m; ++i)
           //             {
           //                 for (int j = 0; j < n; ++j)
           //                 if (bx[i][j]) cout << "x";
           //                 else cout << mp[i][j];
           //                 cout << endl;
           //             }
			        //cout << "------------ " << endl;
				    
				    int tot = go(ni, nj);
				    new_stable = (tot == boxes.size());
				    for (int i = 0; i < new_boxes.size(); ++i)
				    {
				        wp[new_boxes[i].first][new_boxes[i].second] = false;
				    }
				    bx[bi][bj] = true;
				    bx[ni][nj] = false;
				    
				    
				    if (!new_stable && !stable) continue;
				    long long nk = encode(new_boxes, new_stable);
				    if (!was[nk])
				    {
					    was[nk] = true;
					    qu[!(T&1)].push(nk);
				    }
			    }
			    
			}
			for (int i = 0; i < boxes.size(); ++i)
			{
				bx[boxes[i].first][boxes[i].second] = false;
			}
		}
	}
	printf("%d moves checked\n", T);
	printf("No solution\n");
	return -1;
}


int main(int argc, char *argv[])
{
    if (argc != 2) { cout << "specify input/output" << endl; return -1;}
    inp.open ((string(argv[1]) + string(".in")).c_str(), fstream::in);
    out.open ((string(argv[1]) + string(".out")).c_str(), fstream::out);
    int T;
    inp >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        cout << "processing case " << cs << endl;
        int result = solve();
        out << "Case #" << cs << ": " << result << endl; 
    }
    return 0;
}