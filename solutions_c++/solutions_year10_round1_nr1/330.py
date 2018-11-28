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

string s[64], t[64];
int N, K;

void rotate()	{
	FOR (i, 0, N)	{
		t[i] = s[i];
	}
	
	FOR (i, 0, N)	{
		FOR (j, 0, N)	{
			t[j][N-1-i] = s[i][j];
		}
	}
}

void drop()	{
	FOR (j, 0, N)	{
		int k = N - 1;
		for (int i = N-1; i >= 0; i--)	if (t[i][j] != '.')	{
			s[k--][j] = t[i][j];
		}
		for (; k >= 0; k--)	{
			s[k][j] = '.';
		}
	}
}

int dx[] = {1, 1, 0, 1}, dy[] = {-1, 1, 1, 0};

bool find(char p)	{
	FOR (i, 0, N)	{
		FOR (j, 0, N)	{
			FOR (idx, 0, 4)	{
				bool ok = true;
				int ci = i, cj = j;
				for (int k = 0; k < K && ok; k++)	{
					ok = ok && 0 <= ci && ci < N && 0 <= cj && cj < N;
					ok = ok && (s[ci][cj] == p);
					ci += dy[idx];
					cj += dx[idx];
				}
				if (ok)	return true;
			}
		}
	}
	return false;
}

int main(void)	{
	int C;
	cin >> C;
	FOR (nc, 1, C+1)	{
		cin >> N >> K;
		FOR (i, 0, N)	{
			cin >> s[i];
		}
		rotate();
		drop();

		bool r = find('R'), b = find('B');

		cout << "Case #" << nc << ": ";
		if (r && b)	{
			cout << "Both";
		}
		else if (r)	{
			cout << "Red";
		}
		else if (b)	{
			cout << "Blue";
		}
		else	{
			cout << "Neither";
		}
		cout << endl;
	}
	
	
}
