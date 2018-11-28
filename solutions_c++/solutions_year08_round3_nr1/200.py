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
long long a[1000];
int main() {
	freopen("A-large.in","rt",stdin);
	freopen("A-small.txt2","wt",stdout);
	int T;
	cin>>T;
	rep(t,T)
	{
		int p,k,l;
		cin>>p>>k>>l;
		rep(i,l)
			cin>>a[i];
		sort(a,a+l);
		long long r=0;
		int i=l-1;
		long long x=1;
		while(i>=0)
		{
			rep(j,k)
			{
				if(i-j<0)break;
				r+=a[i-j]*x;
			}
			x++;
			i-=k;
		}
		cout<<"Case #"<<t+1<<": "<<r<<endl;
	}
}