# include <cstdio>
# include <iostream>
# include <fstream>
# include <algorithm>
# include <vector>
# include <string>
# include <set>
# include <utility>
# include <map>
# include <queue>
# include <stack>
# include <list>
# include <bitset>
# include <deque>
# include <cassert>
# include <iomanip>
# include <cmath>
# define pb push_back
# define forn(i,n) for (int i=0; i<(int)n; ++i)
# define ford(i,n) for (int i=n-1; i>=0; --i)
# define get(a,b); a b; cin >> b;
# define ull unsigned long long
# define ll long long
# define ld long double
# define mp make_pair
# define matrix vector < vector <int> > 
# define all(a) a.begin(), a.end()
# define INF 1e9
# define eps 1e-9
using namespace std;

int main(){
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	int t;
	cin >> t;
	forn(iter,t){
		int c;
		double d;
		cin >> c >> d;
		vector <double> ven;
		forn(i,c){
			int v;
			double p;
			cin >> p >> v;
			forn(j,v)
				ven.pb(p);
		}
		int n = ven.size();
		double l = 0, r = 1000000;
		forn(it,50){
			double x = (l+r)/2;
			vector <double> tven = ven;
			bool ok = true;
			tven[0]-=x;
			for (int i=1; i<n; i++)
				tven[i] = max(tven[i-1]+d, tven[i]-x);
			for (int i=0; i<n-1; i++)
				ok = ok && (tven[i+1]-tven[i]>=d);
			forn(i,n)
				ok = ok && abs(ven[i]-tven[i])<=x;
			if (ok)
				r = x;
			else
				l = x;
		}
		cout << "Case #" << iter+1 << ": " << l << endl;
	}
    return 0;
}
