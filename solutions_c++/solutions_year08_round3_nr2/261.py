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

int x[40];
int oper[40];
int size;

void inc_oper(void)
{
	int i;
	for (i=1; i<size; i++)
	{
		oper[i]++;
		if (oper[i]<=2) break;
		oper[i]=0;
	}
}

long calc_oper(void)
{
	long val=0;
	long part=0;
	long mul=1;
	int i;
	for (i=size-1; i>=0; i--)
	{
		part += x[i]*mul;
		switch (oper[i])
		{
			case 0: val += part; part = 0; mul = 1; break; // +
			case 1: val -= part; part = 0; mul = 1; break; // -
			case 2: mul *= 10; break;
		}
	}
	return val;
}

long is_ugly(long val)
{
	return ( ((val%2)==0) || ((val%3)==0) || ((val%5)==0) || ((val%7)==0) );
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

		string str;
		in >> str;

		size = str.length();
		for (i=0; i<size; i++)
			x[i] = str.at(i)-'0';
		str += " ";

		FILL(oper, 0);
		int n = (int)pow(3.0, size-1);
		long val;
		int ugly_count=0;
		for (i=0; i<n; i++)
		{
			val = calc_oper();
#if 0
			char temp[4] = "+- ";
			for (int j=0; j<size; j++) printf("%c%d", temp[oper[j]], x[j]); 
			printf(" = %d\n", val);
#endif
			ugly_count += is_ugly(val);
			inc_oper();
		}
		printf("%d\n", ugly_count);
	}

	in.close();

	return 0;
}

