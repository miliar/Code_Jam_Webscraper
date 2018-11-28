#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define pb push_back
#define iss istringstream
#define oss ostringstream
#define prv(vec) {for(int zz = 0; zz < vec.size(); ++zz) cout << vec[zz] << " "; cout << endl;}
#define sz(a) ((a).size())
#define len(a) ((a).length())
#define all(c) (c).begin(),(c).end() 
#define forn(i,a,n) for(int i = (int) a; i < (int)n; i++) 

//vector <int> a;
long long x,y,z;
long long a[1000],c[1000];
//map <int, int > mp;
//map <int, int > ::iterator it;
long long mod = 1000000007;
long long mp[1000];

int main()
{
	freopen("c4.in","rt",stdin);
    freopen("c4.out","wt",stdout); 
	int T;
	cin >> T;
	forn(t,0,T)
	{
		int n,m;
		long long x,y,z;
		cin >> n >> m >> x >> y >> z;
		forn(i,0,m) cin >> a[i];
		forn(i,0,n) mp[i] = 0;
		forn(i,0,n) 
        {
              c[i] = a[i%m];
              a[i%m] = (x * a[i % m] + y * (i + 1)) % z;
        } 
		//forn(i,0,n) cout << c[i] <<" "; 
		forn(i,0,n)
		{
			forn(j,0,i) if ( c[j] < c[i] ) mp[i] = (mp[i] + mp[j])%mod;
			mp[i]++;
		}
		long long ts = 0;
		//for(it = mp.begin(); it != mp.end(); it++) ts = (ts + (it->second))%mod;
		forn(i,0,n) ts = (ts + mp[i])%mod;
		cout << "Case #" << t+1 <<": " << ts << endl;
		//printf("Case #%d: %lld\n",t+1,ts);
	}
    return 0;
}