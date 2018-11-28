//#pragma comment(linker, "/stack:1000000")

#include <ctime>
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

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	int t,s,n,p,a,r;
	int mf, ms;
	cin>>t;
	REP(i,t)
	{
		cin>>n>>s>>p;
		if(p == 0)
		{
				mf = 0;
				ms = 0;
		}
		else if(p == 1)
		{
			mf = 1;
			ms = 2;
		}
		else
		{
			mf = 3*p-2;
			ms = 3*p-4;
		}
		r = 0;
		REP(j,n)
		{
			cin>>a;
			
			if(a>=mf)
				++r;
			else if(s>0 && a>=ms)
			{
				++r;
				--s;
			}
		}
		printf("Case #%d: %d\n", i+1, r);
	}
	
	return 0;
}