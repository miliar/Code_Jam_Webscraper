#include <iostream>
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

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

char getComb(vector<string> & rules, char c1, char c2)
{
	FOR(i, 0, rules.size())
		if ((rules[i][0] == c1 && rules[i][1] == c2) || (rules[i][0] == c2 && rules[i][1] == c1))
			return rules[i][2];
	return 0;
}

bool isCleared(vector<string> & oposed, char c1, char c2)
{
	FOR(i, 0, oposed.size())
		if ((oposed[i][0] == c1 && oposed[i][1] == c2) || (oposed[i][0] == c2 && oposed[i][1] == c1))
			return true;
	return false;
}

void Solve(int tc)
{
	int C;
	cin >> C;
	vector<string> rules(C);
	FOR(i, 0, C) cin >> rules[i];

	int D;
	cin >> D;
	vector<string> oposed(D);
	FOR(i, 0, D) cin >> oposed[i];

	int N;
	cin >> N;
	string input;
	cin >> input;

	vector<char> result;
	FOR(i, 0, N)
	{
		result.push_back(input[i]);
		if (result.size() >= 2)
		{
			//comb
			char n = getComb(rules, result[result.size()-2], result[result.size()-1]);
			if (n)
			{
				result.pop_back(); result.pop_back();
				result.push_back(n);
			}
			else
			{
				bool cl = false;
				FOR(j, 0, result.size()-1)
					if (isCleared(oposed, result[j], result[result.size()-1]))
					{
						cl = true;
						break;
					}
				if (cl) result.clear();
			}
		}
	}

	printf("Case #%d: [", tc);
	FOR(i, 0, result.size())
	{
		if (i) cout << ", ";
		cout << result[i];
	}
	cout << "]" << endl;
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T)
		Solve(step+1);

	return 0;
}
