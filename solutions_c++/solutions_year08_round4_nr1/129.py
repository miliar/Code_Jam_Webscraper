#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std; 

#define DEBUG(x) fout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1 << 29;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
#ifdef WIN32
typedef __int64 ll;
#else
typedef long long ll;
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

ofstream fout("output.out");
ifstream fin("input.in");

const int MAX = 10047;

int gate[MAX], change[MAX], value[MAX];
ll one[MAX], zero[MAX];

ll go(int node, int val)
{
	if (value[node] != -1)
		return value[node] == val ? 0 : INF;
	
	int c1 = 2*node, c2 = 2*node+1;
	if (val == 0)
	{
		if (zero[node] != -1) return zero[node];

		//AND
		int pos1 = go(c1, 0) + min(go(c2, 0), go(c2, 1)), pos2 = go(c2, 0) + min(go(c1, 0), go(c1, 1));
		//OR
		int pos3 = go(c1, 0) + go(c2, 0);

		if (change[node] == 0) //ak sa nemozem menit
		{
			if (gate[node] == 1) return zero[node] = min(pos1, pos2); //som AND
			else return zero[node] = pos3; //som OR
		}
		else
			return zero[node] = min(min(pos1, pos2)+(gate[node]==1?0:1), pos3+(gate[node]==0?0:1));
	}
	else if (val == 1)
	{
		if (one[node] != -1) return one[node];

		//AND
		int pos1 = go(c1, 1) + go(c2, 1);
		//OR
		int pos2 = go(c1, 1) + min(go(c2, 0), go(c2, 1)), pos3 = go(c2, 1) + min(go(c1, 0), go(c1, 1));

		if (change[node] == 0) //ak sa nemozem menit
		{
			if (gate[node] == 1) return one[node] = pos1; //som AND
			else return one[node] = min(pos2, pos3);
		}
		else
			return one[node] = min(pos1+(gate[node]==1?0:1), min(pos2, pos3)+(gate[node]==0?0:1));
	}
}

int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		int M, V;
		fin >> M >> V;

		memset(value, -1, sizeof(value));
		int node = 1;
		FOR(i, 0, (M-1)/2)
		{
			fin >> gate[node] >> change[node];
			++node;
		}

		FOR(i, 0, (M+1)/2)
		{
			fin >> value[node];
			++node;
		}

		memset(one, -1, sizeof(one));
		memset(zero, -1, sizeof(zero));
		
		ll res = go(1, V);
		fout << "Case #" << step+1 << ": ";
		if (res >= INF) fout << "IMPOSSIBLE" << endl;
		else fout << res << endl;
	}

	return 0;
}
