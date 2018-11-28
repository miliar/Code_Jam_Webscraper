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

#define SZ 2000002
bool a[SZ];

vector<Long> p;

void prepare()
{
	FILL(a,true);
	for(int i = 2; i<SZ; ++i)
		if(a[i])
		{
			p.pb(i);
			for(int j = i+i; j<SZ; j += i)
				a[j] = false;
		}
}

Long n;
int cnt(Long x)
{
	int r = 0;
	Long k = x*x;
	while(k<=n)
	{
		k*=x;
		++r;
	}
	return r;
}

int sol()
{
	cin>>n;
	if(n == 1)
		return 0;
	int res = 1;
	REP(i,p.size())
		res += cnt(p[i]);
	return res;
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	prepare();
	int T;
	cin>>T;
	REP(i,T)
		cout<<"Case #"<<i+1<<": "<<sol()<<endl;
	return 0;
}