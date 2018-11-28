//Seikang

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <stdlib.h>
#include <utility>

#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>

#include <cmath>
#include <complex>
#include <algorithm>

#include <ctime>
#define gtime clock()

using namespace std;

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, lo, hi) for(int i = (lo); i <= (hi); i++)
#define FORD(i, hi, lo) for(int i = (hi); i >= (lo); i--)
#define FE(it, cont) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define ALL(cont) (cont).begin(), (cont).end()
#define SZ(cont) (int)((cont).size())
#define PB  push_back
#define MP  make_pair

template<class T> vector<T> split(const string &s){stringstream ss(s);vector<T> a;T t;while(ss >> t)a.PB(t);return a;}
template<class T> T parse(const string &s){stringstream ss(s);T e;ss >> e;return e;}
template<class T> string toString(const T &e){stringstream ss();ss << e;return ss.str();}

typedef long long int64;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;

const int64 oo = (1ll << 30);
const int MAXN = (int)1e3 + 1;
const int mod = (int)1e9;
const double eps = 1e-9;
const double pi = acos(-1);

int main()
{
//	freopen ("a.in", "rt", stdin);
//	freopen ("a.out", "wt", stdout);
	int c = 1;
	char buff[MAXN];
	cin.getline(buff, MAXN);
	int T;		string s(buff, buff + MAXN);
	T = parse<int>(s);
while(T--)
{
	cin.getline(buff, MAXN);
	s = string(buff, buff + MAXN);
	REP(i, SZ(s))
	{
		switch(s[i])
		{
			case 'a':
				s[i] = 'y';
				break;
			case 'b':
				s[i] = 'h';
				break;
			case 'c':
				s[i] = 'e';
				break;
			case 'd':
				s[i] = 's';
				break;
			case 'e':
				s[i] = 'o';
				break;
			case 'f':
				s[i] = 'c';
				break;
			case 'g':
				s[i] = 'v';
				break;
			case 'h':
				s[i] = 'x';
				break;
			case 'i':
				s[i] = 'd';
				break;
			case 'j':
				s[i] = 'u';
				break;
			case 'k':
				s[i] = 'i';
				break;
			case 'l':
				s[i] = 'g';
				break;
			case 'm':
				s[i] = 'l';
				break;
			case 'n':
				s[i] = 'b';
				break;
			case 'o':
				s[i] = 'k';
				break;
			case 'p':
				s[i] = 'r';
				break;
			case 'q':
				s[i] = 'z';
				break;
			case 'r':
				s[i] = 't';
				break;
			case 's':
				s[i] = 'n';
				break;
			case 't':
				s[i] = 'w';
				break;
			case 'u':
				s[i] = 'j';
				break;
			case 'v':
				s[i] = 'p';
				break;
			case 'w':
				s[i] = 'f';
				break;
			case 'x':
				s[i] = 'm';
				break;
			case 'y':
				s[i] = 'a';
				break;
			case 'z':
				s[i] = 'q';
				break;
		}
	}
	if(c > 1)
		cout << endl;
	printf("Case #%d: %s", c++, s.c_str());
}
//system("pause");
	return 0;
}
