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
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1 << 29;
typedef long long ll;
/*
class 
{
private:
	
public:
	
};*/

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

ifstream fin("vstup.txt");
ofstream fout("vystup.txt");

//FILE * fin = fopen("vstup.txt", "r");
//FILE * fout = fopen("vystup.txt", "w");

int N, K;
int input[147][47];

int res = 0;
int active[147][147];

void go(int size, int act, int ind)
{
	if (!size)
	{
		res = max(res, act);
		return;
	}
	if (res >= act+size) return;

	//pouzije posledne
	int size2 = 0;
	FOR(i, 0, size-1)
	{
		bool check = false;
		FOR(j, 0, K)
			if ((input[active[ind][i]][j] == input[active[ind][size-1]][j]) ||
				((input[active[ind][i]][j] < input[active[ind][size-1]][j]) != (input[active[ind][i]][0] < input[active[ind][size-1]][0])))
			{
				check = true;
				break;
			}
		if (check)
			active[ind+1][size2++] = active[ind][i];
	}
	go(size2, act+1, ind+1);

	//nepouzije posledne
	go(size-1, act, ind);
}

void Solve(int tc)
{
	fin >> N >> K;
	FOR(i, 0, N) FOR(j, 0, K) fin >> input[i][j];

	FOR(i, 0, N) active[0][i] = i;

	res = 0;
	go(N, 0, 0);

	fout << "Case #" << tc << ": " << res << endl;
}

int main()
{
	int T;
	fin >> T;
	FOR(step, 0, T)
		Solve(step+1);

	return 0;
}