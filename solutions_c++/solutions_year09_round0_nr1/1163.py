#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<char> VI;
typedef vector<string> VIs;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int L,D,N;
	cin >> L >> D >> N;
	VIs words(D);
	REP (t, D)
	{
		cin >> words[t];
	}
	REP (t,N)
	{
		cout << "Case #"<< (t+1) << ": ";
		VVI alpha(L, VI(30, 0));
		char c;
		int i=0;
		while(i<L)
		{
			cin >> c;
			if (c=='(')
			{
				cin >>c ;
				while(c!=')')
				{
					alpha[i][c-'a']=1;
					cin >> c;
				}
			} else
			{
				alpha[i][c-'a']=1;
			}
			i++;
		}
		int res=0;
		REP(tt, D)
		{
			i=0;
			while(i<L && alpha[i][words[tt][i]-'a']==1) i++;
			if (i == L) res++;
		}
		cout << res << endl;
	}
		
	return 0;
}
