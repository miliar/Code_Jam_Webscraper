#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <queue>
#include <time.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for(int (a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))

#define NMAX 10000000

typedef vector<int> vi;
typedef vector <string> vs;

vs split(const string& s, const string& delim =" ") { vs res;string t; RP(i,s.sz){ if (delim.find(s[i])!=string::npos) {if (!t.empty()) {res.pb(t);t = "";}} else {t+=s[i];}} if (!t.empty()) {res.pb(t);}return res;}

int main()
{
	int test;   
	int x,s,r,t,n;
	vector< pair< int, pair<int, int> > > seg;
	int c;
    cin >> test;
    
    for(int cs=1; cs<=test; cs++)
    {		
		cin >> x >> s >> r >> t >> n;
		seg.clear();	
		int b, e, w;		
		int last = 0;
		RP(i, n) { 
			cin >> b >> e >> w; 
			if (last < b) seg.pb(make_pair(s, make_pair(last, b)));
			
			seg.pb(make_pair(w+s, make_pair(b, e)));
			last = e;
		}
		
		if (seg[seg.sz-1].second.second < x)
		{
			seg.pb(make_pair(s, make_pair(last, x)));
		}
		
		sv(seg);
		
		//RP(i, seg.sz) { cout << seg[i].second.first << " " << seg[i].second.second << endl; }
		
		double tt = t;
		double dif = r - s;
		double res = 0;
		for(int i=0; i<seg.size(); i++)
		{
			double len = seg[i].second.second - seg[i].second.first;
			double sp = seg[i].first;
			
			if (tt < 1e-9)
			{
				res += len/sp;
			}
			else if (len/(sp + dif) <= tt)
			{
				res +=len/(sp + dif);
				tt -= len/(sp + dif);
			}
			else
			{
				res += tt;
				len -= (sp+dif)*tt;
				res += len/sp;
				tt = 0;
			}
		}
		
		printf("Case #%d: %.8lf\n", cs, res);
	}

	return 0;
}
