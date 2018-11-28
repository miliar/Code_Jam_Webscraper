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

const int MAX = 2000;

int wall1[MAX], wall2[MAX];
int color[MAX];
vector<int> polygs[MAX];
int C, sz = 0;

bool contains(const vector<int> & v, int x)
{
	FOR(i, 0, v.size())
		if (v[i] == x) return true;
	return false;
}

void divide(const vector<int> & v, int a, int b, vector<int> & v1, vector<int> & v2)
{
	v1.clear();
	v2.clear();
	FOR(i, 0, v.size())
	{
		if (v[i] == a || v[i] == b)
		{
			v1.push_back(v[i]);
			v2.push_back(v[i]);
		}
		else if (v[i] < a || v[i] > b)
			v1.push_back(v[i]);
		else
			v2.push_back(v[i]);
	}
}

bool check_poly(const vector<int> & v)
{
	set<int> c;
	FOR(i, 0, v.size()) c.insert(color[v[i]]);
	return c.size() == C;
}

void random_fill(const vector<int> & v)
{
	vector<int> temp;
	FOR(i, 0, C) temp.push_back(i);
	FOR(i, C, v.size()) temp.push_back(rand() % C);
	random_shuffle(temp.begin(), temp.end());
	FOR(i, 0, v.size())
		color[v[i]] = temp[i];
}

void Solve(int tc)
{
	int N, M;
	cin >> N >> M;
	FOR(i, 0, M) { cin >> wall1[i]; --wall1[i]; }
	FOR(i, 0, M) { cin >> wall2[i]; --wall2[i]; }

	polygs[0].clear();
	sz = 0;
	FOR(i, 0, N) polygs[0].push_back(i); ++sz;
	FOR(i, 0, M)
	{
		int index = 0;
		while (!contains(polygs[index], wall1[i]) || !contains(polygs[index], wall2[i])) ++index;
		divide(polygs[index], wall1[i], wall2[i], polygs[sz], polygs[sz+1]);
		++sz;
		polygs[index].swap(polygs[sz]);
	}

	C = INF;
	FOR(i, 0, sz)
		chmin(C, (int)polygs[i].size());
	printf("Case #%d: %d\n", tc, C);

	FOR(i, 0, N) color[i] = i%C;
	while (true)
	{
		bool ok = true;
		FOR(i, 0, sz)
			if (!check_poly(polygs[i]))
			{
				random_fill(polygs[i]);
				ok = false;
				break;
			}
		if (ok) break;
	}
	FOR(i, 0, N)
	{
		if (i) cout << " ";
		cout << color[i] + 1;
	}
	cout << endl;
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T)
		Solve(step+1);

	return 0;
}