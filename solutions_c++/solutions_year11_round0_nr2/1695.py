#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
using namespace std;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

int C,D,N;
map< pair<char, char> , char > c;
vector<string> d;
map< char, int> l;
string q,s,n;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int TS;
	cin >> TS;
	rep(T,TS)
	{
		c.clear();
		d.clear();
		l.clear();
		q = "";
		s = "";
		n = "";
		cin >> C;
		rep(i,C)
		{
			cin >> s;
			c[mp(s[0], s[1])] = s[2];
			c[mp(s[1], s[0])] = s[2];
		}
		cin >> D;
		rep(i,D)
		{
			cin >> s;
			//d[mp(s[0], s[1])] = s[2];
			d.pb(s);
		}
		cin >> N;
		cin >> n;
		rep(i,N)
		{
			q += n[i];
			l[n[i]]++;
			while (q.size() >= 2)
			{
				int qs = q.size();
				char ch = c[mp(q[qs - 1], q[qs - 2])];
				if (ch != 0)
				{
					l[q[qs - 1]]--;
					l[q[qs - 2]]--;
					l[ch]++;
					q.resize(q.size() - 2);
					q += ch;
				} else
					break;
			}
			rep(i,D)
				if (l[d[i][0]]>0 && l[d[i][1]]>0)
				{
					q = "";
					l.clear();
				}
		}

		printf("Case #%d: [", T+1);
		if (q.size() > 0)
		{
			rep(i,int(q.size())-1)
			printf("%c, ",q[i]);
			printf("%c]\n",q[q.size()-1]);
		} else
			printf("]\n");
	}

	return 0;
}

