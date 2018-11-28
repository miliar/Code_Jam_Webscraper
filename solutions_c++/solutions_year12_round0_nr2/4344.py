#include <cstdlib>
#include <cmath>
#include <map>
#include <utility>
#include <set>
#include <sstream>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <stack>
#include <queue>
#include <numeric>
using namespace std;

#define	mp						make_pair
#define	pb						push_back
#define	bg						begin
#define	ed						end
#define	fs						first
#define	sc						second
#define	sz(x)					((int)((x).size()))
#define	For(i,a,b)				for(int i=(a);i<(b);++i)
#define	rep(i,n)				For(i,0,(n))
#define	rFor(i,a,b)				for(int i=(a);i>=(b);--i)
#define	rrep(i,n)				rFor(i,(n),0)
#define	all(v)					(v).begin(),(v).end()
#define	ITER(type)				type::iterator
#define	EACH(type,cont,it)		for(ITER(type) it=(cont).bg,s___=(cont).ed;it!=s___;++it)

typedef	long long				LL;
typedef	vector<int>				VI;
typedef	vector<LL>				VLL;
typedef	vector<vector<int> >	VVI;
typedef	vector<bool>			VB;
typedef	vector<string>			VS;
typedef	list<int>				LI;
typedef	list<LL>				LLL;
typedef	list<string>			LS;
typedef	pair<int,int>			PII;


int main( void )
{
	int		T;

	cin >> T;
	rep(i, T) {
		int		N, S, p;

		cin >> N >> S >> p;

		VI		t(N);
		rep(j, N)
			cin >> t[j];

		int		res = 0;
		int		possible = 0;
		rep(j, N) {
			if((t[j] + 2) / 3 >= p)
				++res;
			else if(((t[j] != 0 && t[j] % 3 == 0) || t[j] % 3 == 2) && (t[j] + 2) / 3 + 1 == p)
				++possible;
		}
		cout << "Case #" << (i + 1) << ": " << (res + min(possible, S)) << endl;
	}
}
