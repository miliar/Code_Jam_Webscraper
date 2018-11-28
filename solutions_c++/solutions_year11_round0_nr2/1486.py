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



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

    int t;
    cin >> t;
    REP (tt, t)
    {
        cout << "Case #" << (tt+1) << ": [";

		map<string, string> com;
		map<char, set<char> > opp;
		int n,m,k;
        cin >> n;
        REP (i, n)
        {
			string comb;
            cin >> comb;
			//cout <<comb<<endl;
			string pre = comb.substr(0,2);
			string pre2 = pre;
			pre2[0] = pre[1];
			pre2[1] = pre[0];

			string re = comb.substr(2,1);
			//cout <<pre <<" " <<pre2 <<" " <<re<<endl;
			com[pre]=re;
			com[pre2]=re;
		}

		cin >> m;
        REP (i, m)
        {
			string oppo;
            cin >> oppo;
			opp[oppo[0]].insert(oppo[1]);
			opp[oppo[1]].insert(oppo[0]);

			//cout <<oppo<<" " <<oppo2<<" ";
		}

		string a;
		cin >> k;
		cin >>a;
		//cout <<a<<endl;

		for(int i=0; i<k; i++)
		{
			//cout <<a<<" "<<i<<" "<<k<<endl;
			int found = 0;
			if(i>0 && opp.find(a[i]) != opp.end()) {
				for (int j=0;j<i; j++) {
					if (opp[a[i]].find(a[j]) != opp[a[i]].end()) {
						a.erase(0,i+1);
						k=k-i-1;
						i=-1;
						found =1;
						break;
					}
				}
			} 
			if (found) continue;

			string s = a.substr(i,2);
			if (com.find(s) != com.end()) {
				string re = com[s];
				//cout <<"rep "<< a.substr(i,2) << " with "<<re<<endl;
				a.replace(i,2,re);
				k--;
			} 
		}

		if (a.length()==0){
			cout << "]"<<endl;
		} else {
			int j=0;
			for (; j<a.length()-1;j++)
				cout << a[j]<<", ";
			cout << a[j]<<"]"<<endl;;
		}


	}

	return 0;
}
