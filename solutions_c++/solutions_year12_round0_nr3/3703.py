//  Recycled Numbers.cpp
//  12/04/14.

#if 1

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <cctype>
#include <sstream>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <bitset>
#include <complex>
#include <fstream>
using namespace std;
typedef long long ll;
const double EPS = 1e-9;
typedef vector<int> vint;
typedef pair<int, int> pint;
#define rep(i, n) REP(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define MSG(a) cout << #a << " " << a << endl;
#define REP(i, x, n) for(int i = x; i < n; i++)
template<class T> T RoundOff(T a){ return int(a+.5-(a<0)); }
template<class T, class C> void chmax(T& a, C b){ if(a < b) a = b; }
template<class T, class C> void chmin(T& a, C b){ if(b < a) a = b; }
template<class T, class C> pair<T, C> mp(T a, C b){ return make_pair(a, b); }

string toString(int x)
{
	stringstream ss;
	
	ss << x;
	
	return ss.str();
}
bool isCycle(int n, int m)
{
	string a(toString(n)), b(toString(m));
	
	if(a.size() != b.size()) return false;
	
	rep(i, a.size())
	{
		if(a == b) return true;
		rotate(a.begin(), a.begin() + 1, a.end());
	}
	
	return false;
}

int main()
{
    int T;
	
	cin >> T;
	
	for(int caseNumber = 1; caseNumber <= T; caseNumber++)
	{
		int res = 0, A, B;
		cin >> A >> B;
		
		map<pint, bool> table;
		
		for(int n = A; n <= B; n++)
		{
			string tmp = toString(n);
			int size = tmp.size();
			
			rep(i, size)
			{
				int m = atoi(tmp.c_str());

				res += n < m && A <= m && m <= B && table[mp(n, m)] != (table[mp(n, m)] = 1);
				
				rotate(tmp.begin(), tmp.begin() + 1, tmp.end());
			}
		}
		
		cout << "Case #" << caseNumber << ": " << res << endl;
	}
}

#endif