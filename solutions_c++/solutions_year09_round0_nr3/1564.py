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

/*class 
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

ifstream fin("C-small-attempt0.in");
ofstream fout("vystup.txt");

string str = "welcome to code jam";

void output(int step, int n)
{
	if (!step) return;
	output(step-1, n/10);
	fout << n%10;
}

int dp[547][47];

int main()
{
	int T;

	fin >> T;

	string line;
	getline(fin, line);
	FOR(step, 0, T)
	{
		getline(fin, line);

		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;

		FOR(i, 1, line.size()+1)
		{
			dp[i][0] = dp[i-1][0];
			FOR(j, 1, str.size()+1)
			{
				dp[i][j] = dp[i-1][j];
				if (line[i-1] == str[j-1])
					dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % 1000;
			}
		}

		fout << "Case #" << step+1 << ": ";
		output(4, dp[line.size()][str.size()]);
		fout << endl;
	}

	return 0;
}
