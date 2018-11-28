#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cmath>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define sz(X) ((int)(X.size()))
#define ln(X) ((int)(X.length()))
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define rrep(i,s,n) for(int i=n-1; i>=s; i--)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define err 1E-15

using namespace std;

int main()
{
	int runs;
	cin>>runs;
	rep(k,1,runs + 1)
	{
		
		 
		int n;
		cin>>n;
		vector<int> a(n),b(n);
		rep(i,0,n) cin>>a[i];
		rep(i,0,n) cin>>b[i];
		sort(all(a));
		sort(all(b));
		reverse(all(b));
		long long ans = 0;
		rep(i,0,n) ans += (long long)(a[i]) * b[i];
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}