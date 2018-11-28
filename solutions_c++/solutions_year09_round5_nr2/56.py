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
#define A X.X
#define B X.Y
#define C Y.X
#define D Y.Y
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef pair <PII, PII> P;
typedef vector <P> VP;

#define mod 10009

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);

    int tt;
    cin >> tt;
    REP (t, tt)
    {
    	cout << "Case #" << t+1 << ":";
    	string ss;
    	int k;
    	cin >> ss >> k;

    	int n;
    	cin >> n;
    	vector <string> s(n);
    	REP (i, n)
    	{
    		cin >> s[i];
    	}


    	REP (i, ss.size ())
    	{
    		if (ss[i] == '+')
    			ss[i] = ' ';
    	}

    	istringstream iss(ss);

    	string S;

    	VI r(k);

    	while (iss >> S)
    	{
    		int res = 0;

    		P x;
    		vector <pair <P, int> > cur, next;
    		char c[4];
    		REP (i, 4)
    		{
    			if (i<S.size ())
					c[i]=S[i];
    			else
    				c[i]='0';
    		}
    		if (S.size ()<=3)
    			x.D = 1;
    		if (S.size ()<=2)
    			x.C = 1;
    		if (S.size ()<=1)
    			x.B = 1;
    		vector <P> w;

    		REP (i, s.size ())
    		{
    			P y;
    			REP (j, s[i].size ())
    			{
    				if (s[i][j]==c[0])	y.A++;
    				if (s[i][j]==c[1])	y.B++;
    				if (s[i][j]==c[2])	y.C++;
    				if (s[i][j]==c[3])	y.D++;
    			}

    			w.pb (y);
    		}

    		next.pb (pair <P, int> (x, 1));
    		P p;

    		REP (kk, k+1)
    		{
    			swap (cur, next);
    			next.clear();

    			SORT (cur);

    			REP (i, cur.size ())
    			{
    				int v = cur[i].Y;
    				while (i<cur.size ()-1 && cur[i].X == cur[i+1].X)
    				{
    					i++;
    					v+=cur[i].Y;
    				}
					v%=mod;
					if (!v)
						continue;

					p = cur[i].X;

					if (kk && p.A && p.B && p.C && p.D)
					{
						r[kk-1] += (p.A*p.B*p.C*p.D)%mod*v;
						r[kk-1] %= mod;
					}

					if (kk == k)
						continue;

					REP (j, w.size ())
					{
						next.pb (pair <P, int> (P (PII (p.A+w[j].A, p.B+w[j].B), PII (p.C+w[j].C, p.D+w[j].D)), v));
					}
    			}
    		}
    	}

    	REP (i, r.size ())
    	{
    		cout << " " << r[i];
    	}
    	cout << endl;
    }

    return 0;
}
