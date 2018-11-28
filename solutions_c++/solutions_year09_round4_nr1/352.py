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

string input[47];
int pos[47];

void Solve(int tc)
{
	int N;
	fin >> N;
	FOR(i, 0, N) fin >> input[i];

	//najde najpravejsiu 1
	FOR(i, 0, N)
	{
		pos[i] = -1;
		FOR2(j, N-1, -1)
			if (input[i][j] == '1')
			{
				pos[i] = j;
				break;
			}
	}

	int res = 0;
	FOR(i, 0, N)
	{
		int n;
		FOR(j, i, N)
			if (pos[j] <= i)
			{
				n = j;
				break;
			}

		while (n > i)
		{
			++res;
			swap(input[n], input[n-1]);
			swap(pos[n], pos[n-1]);
			--n;
		}
	}

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