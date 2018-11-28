#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <iterator>
#include <functional>
#include <utility>
#include <algorithm>
#include <numeric>
#include <typeinfo>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();++i)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

void solve()
{
	int n; cin>>n;
	vi a(n);
	rep(i,n) cin>>a[i];
	
	vi b=a;
	sort(allof(b));
	int diff=0;
	rep(i,n) diff+=a[i]!=b[i];
	printf("%f\n",(double)diff);
}

int main()
{
	int cases; scanf("%d ",&cases);
	rep(i,cases){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
