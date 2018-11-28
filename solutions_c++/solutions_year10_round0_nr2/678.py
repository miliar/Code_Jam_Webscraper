#include <iostream>
#include <fstream>
#include <sstream>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <deque>

#include <cmath>
#include <string>
#include <ctime>
#include <ctime>
#include <cstdlib>
#include <algorithm>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define tr(v,it) for(typeof(v.begin()) it = v.begin(); it != v.end() ; ++it)
#define all(c) c.begin(),c.end()
#define SZ(c) (int)c.size()
#define SQ(x) (x)*(x)
#define OUT(a,b)FOR(i,0,b)cout << a[i] << " ";cout << endl;
#define PI 2.0*acos(0.0)
#define SET(a,b) memset(a,b,sizeof a)
#define r(T) scanf("%d",&T)
using namespace std;

typedef long long LL;

int main()
{
	int T,N;
	r(T);
	REP(c,1,T)
	{
		r(N);
		vector<int> v(N);
		FOR(j,0,N)r(v[j]);
		sort(all(v));
		vector<int> x;
		FOR(j,1,N)x.push_back(v[j]-v[j-1]);
		int t = x[0];
		FOR(j,1,SZ(x))t = __gcd(t,x[j]);
		int Y = v[0]/t;
		if(v[0]%t)++Y;
		Y = Y*t - v[0];
		printf("Case #%d: %d\n",c,Y);
	}	
	return 0;
}
