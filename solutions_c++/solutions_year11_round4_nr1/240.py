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
#define EPS 1e-7
#define Pi 3.14159265358979
#define FILL(a,v) memset(a,v,sizeof(a))

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PII;

vector<pair<int, double>> v;

int n,s,r,x;
double t;
double sol()
{
	v.clear();
	cin>>x>>s>>r>>t>>n;
	{
		int t1,t2,t3;
		REP(i,n)
		{
			cin>>t1>>t2>>t3;
			v.pb(mp(t3, t2-t1));
			x -= (t2-t1);
		}
	}
	v.pb(mp(0,x));
	sort(ALL(v));
	double ct;
	double res = 0;
	double l,vr,vs;
	REP(i,v.size())
	{
		l = v[i].second;
		vr = v[i].first + r;
		vs = v[i].first + s;

		ct = min(t, l/vr);
		res += ct;
		res += (l-vr*ct)/vs;
		t -= ct;
	}
	return res;
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	int T;
	cin>>T;
	cout.precision(9);
	REP(i,T)
		cout<<"Case #"<<i+1<<": "<<sol()<<endl;
	return 0;
}