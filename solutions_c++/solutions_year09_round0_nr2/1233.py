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
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

VI a;
vector <char> c;

int p (int x)
{
	int xx = x;
	while (a[x]!=x)
		x = a[x];

	while (a[xx]!=xx)
	{
		int next = a[xx];
		a[xx] = x;
		xx = next;
	}

	return x;
}

void join (int x, int y)
{
	x = p(x);
	y = p(y);

	if (x!=y)
		a[x] = y;
}


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);

    int tt;
    cin >> tt;

    REP (t, tt)
    {
    	cout << "Case #" << t+1 << ":" << endl;

    	int w,h;
    	cin >> h >> w;

    	a.resize (w*h);

    	REP (i, a.size ())
			a[i] = i;

    	c = vector <char>(a.size (), '0');

    	VI b(w*h);

    	REP (i, w*h)
			cin >> b[i];

    	REP (i, w*h) {
    		int hh = b[i];
    		int j = i;

    		if (i>=w)
    			if (hh>b[i-w])
    			{
    				hh = b[i-w];
    				j = i-w;
    			}
    		if (i%w)
    			if (hh>b[i-1])
    			{
    				hh = b[i-1];
    				j = i-1;
    			}
    		if ((i+1)%w)
    			if (hh>b[i+1])
    			{
    				hh = b[i+1];
    				j = i+1;
    			}
    		if (i+w<w*h)
    			if (hh>b[i+w])
    			{
    			    hh = b[i+w];
    			    j = i+w;
    			}

    		if (j != i)
    			join (j, i);
    	}

    	char cc = 'a';
    	REP (i, w*h)
    	{
    		if (c[p(i)]=='0')
    		{
    			c[p(i)] = cc++;
    		}
    		cout << c[p(i)];
    		if ((i+1) %w)
    			cout << " ";
    		else
    			cout << endl;
    	}
    }

    return 0;
}
