#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>

using namespace std;

typedef long long int64;

#define Fill(a,c) memset(&a, c, sizeof(a))
#define All(v) (v).begin(), (v).end()
#define REP(i,n) for (int i = 0; i < (n); i++)
#define REPD(i,n) for (int i = (n) - 1; i >= 0; i--)
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
	
#define pi acos(-1.)
#define eps 1e-7
//#define inf 1LL<<32
#define inf 1e17
#define maxn 1000

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

int main()
{
	int testN;
	cin>>testN;
	REP(testi,testN) {
	VI Ix, Iy;
	int In;
	cin >> In;
	REP(i,In){int tx; cin>>tx; Ix.push_back(tx);}
	REP(i,In){int ty; cin>>ty; Iy.push_back(ty);}

	sort(All(Ix));
	sort(All(Iy));

	int64 res=0;
	REP(i,In){res+=Ix[i]*Iy[In-1-i];}
	printf("Case #%d: %d\n", testi+1, res);
	}
}
