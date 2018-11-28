#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

int ht[128][128], lab[128][128], out[128][128][2] ;

bool IN(int x, int a, int b)	{
	return a <= x && x < b;
}

int main(void)	{
	int C, H, W;
	cin >> C;
	FOR (nc, 1, C+1)	{
		cin >> H >> W;
		FOR (i, 0, H)	FOR (j, 0, W)	cin >> ht[i][j];
		
		memset(out, 255, sizeof out);
		memset(lab, 255, sizeof lab);
		
		FOR (i, 0, H)	FOR (j, 0, W)	{
			int bi = -1, bj = -1;
			FOR (di, -1, 2)	FOR (dj, -1, 2)	if (di*dj == 0 && di+dj != 0 && IN(i+di,0,H) && IN(j+dj,0,W))	if (ht[i+di][j+dj] < ht[i][j])	{
				if (bi == -1 || ht[i + di][j + dj] < ht[bi][bj])	{
					bi = i + di;
					bj = j + dj;
				}
			}
			out[i][j][0] = bi; 	out[i][j][1] = bj;
		}
		
		int nlab = 0;
		FOR (y, 0, H)	FOR (x, 0, W)	{
			int i = y, j = x;
			while (out[i][j][0] != -1 && lab[i][j] == -1)	{
				int ni = out[i][j][0], nj = out[i][j][1];
				i = ni, j = nj;
			}
			int setlab = -1;
			if (lab[i][j] == -1)	setlab = nlab++;
			else	setlab = lab[i][j];

			assert(setlab != -1);
			i = y, j = x;
			while (i != -1 && j != -1 && lab[i][j] == -1)	{
				lab[i][j] = setlab;
				int ni = out[i][j][0], nj = out[i][j][1];
				i = ni, j = nj;
			}
			//if (i != -1 && j != -1)	assert(lab[i][j] == setlab);
		}

		cout << "Case #" << nc << ":" << endl;
		FOR (i, 0, H)	{
			FOR (j, 0, W)	{
				cout << (char)(lab[i][j]+'a');
				if (j < W - 1)	cout << " ";
			}
			cout << endl;
		}
	}
	
	
}
