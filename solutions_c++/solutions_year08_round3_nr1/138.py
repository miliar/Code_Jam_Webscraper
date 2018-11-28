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
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream
#define prv(vec) {for(int zz = 0; zz < vec.size(); ++zz) cout << vec[zz] << " "; cout << endl;}
#define sz(a) ((a).size())
#define len(a) ((a).length())
#define all(c) (c).begin(),(c).end() 
#define forn(i,a,n) for(int i = (int) a; i < (int)n; i++) 

vector <int> a;

int main()
{
	freopen("a3.in","rt",stdin);
    freopen("a3.out","wt",stdout); 
	int T;
	cin >> T;
	forn(t,0,T)
	{
		long long ts = 0;
		int p,k,L;
		a.clear();
		cin >> p >> k >> L;
		a.resize(L);
		forn(i,0,L) cin >> a[i];
		sort(all(a));
		reverse(all(a));
		forn(i,0,L)
		{
			ts += a[i] * (i/k + 1);
		}
		cout << "Case #" << t+1 <<": " << ts << endl;
		//printf("Case #%d: %lld\n",t+1,ts);
	}
    return 0;
}