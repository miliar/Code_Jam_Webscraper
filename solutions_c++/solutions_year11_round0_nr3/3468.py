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

int a[2000];

void sol()
{
	int n;
	cin>>n;
	int s = 0;
	int k = 0;
	REP(i,n)
	{
		cin>>a[i];
		s += a[i];
		k ^= a[i];
	}
	if(k != 0)
		cout<<"NO";
	else
		cout<<s - *min_element(a, a+n);
}

int main(int argc, char** argv)
{
	int T;
	cin>>T;
	REP(i,T)
	{
		cout<<"Case #"<<i+1<<": ";
		sol();
		cout<<endl;
	}
	return 0;
}