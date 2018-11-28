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
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end() 
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
int main() {
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int T;
	cin>>T;
	rep(t,T)
	{
		int r=0;
		vector<int> x,y;
		int n;
		cin>>n;
		rep(i,n)
		{
			int a;
			cin>>a;
			x.push_back(a);
		}
		rep(i,n)
		{
			int a;
			cin>>a;
			y.push_back(a);
		}
		sort(all(x));
		sort(y.rbegin(),y.rend());
		rep(i,n)
		{
			r+=x[i]*y[i];
		}
		printf("Case #%d: %d\n",t+1,r);
	}
	return 0;
}
