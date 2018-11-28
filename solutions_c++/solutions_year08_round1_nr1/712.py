#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>

#include <stdio.h>
#include <string.h>

using namespace std;

typedef vector <int>    vi;
typedef vector <vi>     vvi;
typedef long long       ll;
typedef vector <ll>     vll;
typedef vector <double> vd;
typedef vector <string> vs;
typedef pair<int,int>   pii;
typedef vector <pii>    vpii;
typedef istringstream   iss;

#define INF 1e10
#define eps 1e-9

#define DIST(a, b)      sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]))
#define MAX(a, b)       ((a) > (b) ? (a) : (b))
#define SQR(a)          ((a) * (a))
#define ABS(a)          ((a>0) ? (a) : (-a))

#define FOR(i,from,to)  for (int i(from),_b(to); i <= _b; ++i)
#define FORD(i,from,to) for (int i(from),_b(to); i >= _b; --i)
#define REP(i,n)        for (int i(0),_n(n); i<_n; ++i)
#define FILL(var,c)     memset(&var, c, sizeof(var))
#define ALL(x)          (x).begin(), (x).end()
#define FOREACH(it, x)  for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define SORT(x) 	sort(ALL(x))
#define REVERSE(x) 	reverse(ALL(x))
#define UNIQUE(x) 	SORT(x), (x).resize(unique(ALL(x))-(x).begin())

#define PB 		push_back
#define PF 		push_front
#define MP(a,b) 	make_pair(a,b)
#define ST 		first
#define ND 		second
#define SIZE(x) 	(int)x.size()

template <typename T> std::string to_s( const T& t ) { ostringstream oss; oss << t; return oss.str(); }

void trim(string& str)
{
	string::size_type pos1 = str.find_first_not_of(' ');
	string::size_type pos2 = str.find_last_not_of(' ');
	str = str.substr(pos1 == string::npos ? 0 : pos1, pos2 == string::npos ? str.length() - 1 : pos2 - pos1 + 1);
}

int main()
{
	int num, i;
	ifstream in("in");
	string line;

	in >> num;
	getline(in, line);

	for (int n=0; n<num; n++)
	{
		printf("Case #%d: ", n+1);
		int len;

		in >> len;
		getline(in, line);

		vi x;
		vi y;
		int val;

		for (i=0; i<len; i++)
		{
			in >> val;
			x.PB(val);
		}

		for (i=0; i<len; i++)
		{
			in >> val;
			y.PB(val);
		}
		
		SORT(x);
		SORT(y);
		REVERSE(y);
		int dot=0;
		for (i=0; i<len; i++)
		{
			dot += x[i]*y[i];
		}
		printf("%d\n", dot);
	}

	in.close();

	return 0;
}

