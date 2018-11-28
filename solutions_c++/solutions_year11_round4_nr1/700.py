#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
#define ALL(x)   (x).begin(),(x).end()
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define F first
#define S second
#define CLEAR(A, V) memset(A, V, sizeof(A))

typedef  long long   ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;

template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);

int main(){
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++)
	{
		int X, S, R, N;
		double t;
		cin >> X >> S >> R >> t >> N;
		int walklength = 0;
		double r = 0.;
		vector<II> intervals;
		for(int i = 0; i < N; i++)
		{
			int B,E,w;
			cin >> B >> E >> w;
			intervals.push_back(II(w+S,E-B));
			walklength += E-B;
/*			walklength += E-B;
			if(double(w+R)*double(t)>double(E-B)+EPS)
			{
				// corro todo
				r+=double(E-B)/double(w+R);
				t-=double(E-B)/double(w+R);
			}
			else
			{
				// corro parte
				r+=t;
				double lengthleft = double(E-B)-double(w+R)*double(t);
				t = 0.;
				r+=lengthleft/double(w+S);
			}
			printf("%.9lf\n", r);*/
		}
		if(X>walklength)
		{
			intervals.push_back(II(S,X-walklength));
		}
/*		printf("t = %.9lf\n", t);
		if(X>walklength+EPS)
		{
			double left = X-walklength;
			cout << left << endl;
			if(double(R)*double(t)>left+EPS)
			{
				// corro todo
				r+=left/double(R);
				t-=left/double(R);
				cout << "corro" << endl;
			}
			else
			{
				// corro parte
				r+=t;
				double lengthleft = left-double(R)*double(t);
				t = 0.;
				r+=lengthleft/double(S);
				cout << "corro y camino" << endl;
			}
		}*/
		sort(intervals.begin(),intervals.end());
		for(int i = 0; i < intervals.size(); i++)
		{
			int w = intervals[i].F;
			double ilength = intervals[i].S;
			if(double(w+R-S)*double(t)>double(ilength)+EPS)
			{
				// corro todo
				r+=ilength/double(w+R-S);
				t-=ilength/double(w+R-S);
			}
			else
			{
				// corro parte
				r+=t;
				double lengthleft = ilength-double(w+R-S)*double(t);
				t = 0.;
				r+=lengthleft/double(w);
			}
		}
		printf("Case #%d: %.9lf\n", caso, r);
	}
	return 0;
}

