#include <set>
#include <map>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define repa(v)				for(int i=0;i<(sz(v));++i) for(int j=0;j<(sz(v[i]));++j)
#define rep(i, v)			for(int i=0;i<(sz(v));++i)
#define lp(i, cnt)			for(int i=0;i<(cnt);++i)
#define lpi(i, s, cnt)		for(int i=(s);i<(cnt);++i)
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"

typedef long long ll;
const int OO = (int)1e8;	// Note, IF Small may be WRONG, Large may generate OVERFLOW


int main()
{
	freopen("a.in", "rt", stdin);
	freopen("aa.in", "w", stdout);
	
	int cases;
	cin>>cases;
	string line;
	
	for (int CASE = 1; CASE <= cases; ++CASE) {
		
		int mn = OO;
		int k;
		cin>>k;
		getline(cin, line);
		getline(cin, line);
		
		
		vector<int> v;
		lp(i, k)	v.push_back(i);
		
		do {
			//v[0] = 2, v[1] = 0, v[2] = 3, v[3] = 1;
			
			string nstr = line;
			int tot = 0;
			lp(i, sz(line)/k) {
				lp(j, k)
				{
					//cout<<tot+j<<" "<<tot+v[j]<<"\n"<<tot+v[j]<<flush;
					nstr[tot+j] = line[ tot+v[j] ];
				}
				tot+=k;
				//cout<<"\n";
			}
			//cout<<"******\n";
			int cnt = 0;
			rep(i, line) {
				if(i == 0)	cnt++;
				else if( nstr[i] != nstr[i-1])	cnt++;
			}
			//cout<<line<<"\n"<<nstr<<"\n";
			mn = min(mn, cnt);
			
		//	break;
			
		} while( next_permutation(all(v) ) );
		
		cout<<"Case #"<<CASE<<": ";
		cout<<mn<<"\n";
	}
	
	
	
	
	return 0;
}
