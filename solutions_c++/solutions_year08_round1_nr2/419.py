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



int main()
{
	freopen("B-small-attempt0_2.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
	int T;
	cin>>T;
	rep(t,T)
	{
		
		int n,m;
		cin>>n>>m;
		vector<vector<bitset<100> > > in;
		in.resize(2,vector<bitset<100> >(n));
		rep(i,m)
		{
			int t;
			cin>>t;
			rep(j,t)
			{
				int x,y;
				cin>>x>>y;
				x--;
				in[y][x][i]=1;
			}
		}
		int M=INT_MAX,mm;
		rep(i,1<<n)
		{
			bitset<100> r;
			int xx=0;
			rep(j,n)
			{
				int x=(i>>j)&1;
				xx+=x;
				r|=in[x][j];
			}
			if(r.count()==m)
			{
				if(xx<M)
				{
					M=xx;
					mm=i;
				}
			}
		}
		printf("Case #%d:",t+1);
		if(M==INT_MAX)
			printf(" IMPOSSIBLE");
		else
			rep(j,n)
			{
				int x=(mm>>j)&1;
				printf(" %d",x);
			}
		printf("\n");
	}
}