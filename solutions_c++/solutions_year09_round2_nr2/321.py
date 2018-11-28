#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cfloat>
#include <cmath>
#include <complex>
#include <cstdio>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define all(x) (x).begin(),(x).end()
typedef long long ll;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;

typedef pair<int, int> PII;
typedef vector<PII> VPII;
#define X first
#define Y second
#define mp make_pair

#define two(x) (1<<(x))
#define twoll(x) ((long long)1<<(x))
#define contain(s,x) (((s)&two(x))!=0)
#define containll(s,x) (((s)&twoll(x))!=0)

#define db(a) cout << #a << "=" << a << " "
#define dbn cout << endl
template<class T> void print(vector<T> v) { cout << "["; if (v.size()) cout << v[0]; for (unsigned i = 1; i < v.size(); ++i) cout << ", " << v[i];cout << "]\n"; }
template<class T> void print(vector<vector<T> > v) { cout << "[ ---\n"; if (v.size()) cout << " ", print(v[0]); for (unsigned i = 1; i < v.size(); ++i) cout << " ", print(v[i]); cout << "--- ]\n"; }
template<class T1, class T2> void print(pair<T1, T2> p) { cout << "{" << p.first << ", " << p.second << "}"; }
template<class T1, class T2> void print(vector<pair<T1, T2> > v) { cout << "["; if (v.size()) print(v[0]); for (unsigned i = 1; i < v.size(); ++i) cout << ", ", print(v[i]);cout << "]\n"; }
#define sqr(x) (x)*(x)

template<class T> inline int chkmin(T& a, T b) { if (a>b) {a=b; return 1;} return 0; }
template<class T> inline int chkmax(T& a, T b) { if (a<b) {a=b; return 1;} return 0; }

string STR(int n) { char tmp[20]; sprintf(tmp,"%d",n); return tmp; }
int INT(string s) { return atoi(s.c_str()); }
template <class Ty, class Tx> Ty to(const Tx &x) { Ty y; stringstream ss; ss<<x; ss>>y; return y; }

const int INF = 1000000007;
const double EPS = 1e-10;

char buf[1<<20];

int CUR_CASE;
int TOTAL_CASES;

int main() {
	freopen("DATA.in", "rt", stdin);
	freopen("DATA.ou", "wt", stdout);
	clock_t STARTTIME, ENDTIME;
	STARTTIME = clock();

	gets(buf);
	TOTAL_CASES = atoi(buf);

	for (CUR_CASE = 1; CUR_CASE <= TOTAL_CASES; ++CUR_CASE)
	{
		gets(buf);
		string s = buf;
		string s2 = s;
		next_permutation(all(s2));
		string res;
		if (s2 <= s)
		{
			char c = *max_element(all(s));
			for (int i = 0; i < s.length(); ++i)
				if (s[i] != '0' && s[i] < c)
					c = s[i];
			res += c;
			s.erase(s.begin()+s.find(c));
			s += '0';
			sort(all(s));
			res += s;
		}
		else
			res = s2;
		printf("Case #%d: %s\n",CUR_CASE,res.c_str());
	}

	ENDTIME = clock();
	cerr << "elapsed time : " << ENDTIME-STARTTIME << "ms";
	return 0;
}





