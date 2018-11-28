//#pragma comment(linker, "/stack:1000000")

#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 5e-7
#define Pi 3.14159265358979
#define FILL(a,v) memset(a,v,sizeof(a))

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PII;

vector<PII> a;
int n;
double d;

bool eq(double x, double y)
{
	if(abs(x-y)<EPS)
		return true;
	if(abs(x-y)/x<EPS)
		return true;
	return false;
}

bool chk(double x)
{
	double ml = -1e100;
	REP(i,n)
	{
		ml = max(ml+d, a[i].first-x);
		ml += (a[i].second-1)*d;
		if(ml-a[i].first>x)
			return false;
	}
	return true;
}

double sol()
{
	int c,p,v;
	cin>>c>>d;
	a.clear();
	REP(i,c)
	{
		cin>>p>>v;
		a.pb(mp(p,v));
	}
	n = a.size();
	double l = 0;
	double r = 1e15;
	double m;
	while(!eq(r,l))
	{
		m = (l+r)/2;
		if(chk(m))
			r = m;
		else
			l = m;
	}
	return l;
}

int main(int argc, char** argv)
{
	int T;
	cin>>T;
	cout.precision(9);
	REP(i,T)
		cout<<"Case #"<<i+1<<": "<<sol()<<endl;
	return 0;
}