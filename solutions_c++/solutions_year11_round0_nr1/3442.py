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

int f(int x, int y)
{
	if(x<y)
		return 1;
	if(x>y)
		return -1;
	return 0;
}

int solTest()
{
	vector<PII> O,B;
	int n;
	cin>>n;
	char t;
	int x;
	REP(i,n)
	{
		cin>>t>>x;
		if(t == 'O')
			O.pb(mp(i,x));
		else
			B.pb(mp(i,x));
	}
	if(O.size() != 0)
		O.pb(mp(2000, O.back().second));
	else
		O.pb(mp(2000, 1));
	if(B.size() != 0)
		B.pb(mp(2001, B.back().second));
	else
		B.pb(mp(2001, 1));
	int co = 1;
	int cb = 1;
	int po = 0;
	int pb = 0;
	int res = 0;

	while(po != O.size()-1 || pb != B.size()-1)
	{
		++res;
		if(O[po].first<B[pb].first)
		{
			if(co == O[po].second)
				++po;
			else
				co += f(co, O[po].second); 
			cb += f(cb, B[pb].second);
		}
		else
		{
			co += f(co, O[po].second);
			if(cb == B[pb].second)
				++pb;
			else
				cb += f(cb, B[pb].second);
		}
	}
	return res;
}

int main(int argc, char** argv)
{
	int T;
	cin>>T;
	REP(i,T)
		cout<<"Case #"<<i+1<<": "<<solTest()<<endl;
	return 0;
}