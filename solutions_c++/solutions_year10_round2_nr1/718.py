#define DEBUG 1

using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep(i, a, b, x) for(int i(a), _b(b); i <= _b; i += x )
#define rep(i, n) _rep( i, 0, n - 1, 1 )
#define rrep(i, a, b) for(int i(a),_b(b); i >= (_b); --i)
#define xrep( i, a, b ) _rep(i, a, b, 1)
#define foreach(type, v, it) for(type::iterator it = v.begin(); it!=v.end(); ++it)

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

#define dbg(x) if(DEBUG) cerr << __LINE__ << ": " << #x << " -> " << (x) << "\t";
#define dbge(x) if(DEBUG) cerr << __LINE__ << ": "<<#x << " -> " << (x) << endl;




// She
// May be the reason I survive
// The why and wherefore I'm alive
// The one I'll care for through the rough in ready years

//...

map< string, set<string> > dir;

char line[10000];

int main()
{
	int t, n, m;
	freopen("f:/data/A-large.in.txt","r",stdin);
	freopen("f:/data/ala.txt","w",stdout);



	scanf("%d", &t);
	
	xrep(tc,1,t)
	{
		dir.clear();
		vector<string> ori, mkd;
		scanf("%d %d", &n, &m);
		rep(i,n)
		{
			scanf("%s",line);
			string input = line;
			rep(j,sz(input)) if (input[j] == '/') input[j] = ' ';
			ori.pb(input);

		}		
		
		sort(all(ori));
		
		rep(i,n)
		{
			istringstream iss(ori[i]);
			string dname, dtname, last = "";
			
			
			while (iss>>dname)
			{
				dtname = last + "/" + dname;
				dir[last].insert(dtname);
				last = dtname;
			}
		}

		rep(i,m)
		{
			scanf("%s",line);
			string input = line;
			rep(j,sz(input)) if (input[j] == '/') input[j] = ' ';
			mkd.pb(input);

		}
		
		sort(all(mkd));
		
		int ans = 0;
		
		rep(i,m)
		{
			
			istringstream iss(mkd[i]);
			string dname, dtname, last="";
			while (iss>>dname)
			{
				dtname = last + "/" + dname;
				if (dir[last].find(dtname) == dir[last].end())
				{
					dir[last].insert(dtname);
					ans++;
				}
				last = dtname;
			}
		}
		
		printf("Case #%d: %d\n", tc, ans);
		
	}
	
	
	
	
	return 0;
}
