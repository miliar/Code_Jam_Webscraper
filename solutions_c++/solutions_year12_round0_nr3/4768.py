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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>

using namespace std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

int t,a,b;

inline int cnt(int x)
{
	stringstream ss;
	ss<<x;
	return ss.str().length();
}

bool can(int a,int b)
{
	stringstream ss;
	ss<<a<<" "<<b;
	string s,c;
	ss>>s>>c;
		rep(j,0,s.size())
		{
			bool fl = 0;
			rep(k,0,s.size())
				if(s[k]!=c[(j+k)%c.size()])
				{
					fl = 1;
					break;
				}
			if(!fl)
				return true;

		}
	return false;
}

int arr[3002][3002];

int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);

	rep(i,1,1001)
	{
		rep(j,i+1,1001)
		{
			if(cnt(i)!=cnt(j))
				continue;
			if(can(i,j))
				arr[i][j]=1;
		}
	}

	scanf("%d",&t);

	rep(tt,0,t)
	{
		scanf("%d %d",&a,&b);
		int res=0;
		rep(i,a,b+1)
			rep(j,i+1,b+1)
				res+=arr[i][j];
		printf("Case #%d: %d\n",tt+1,res);
	}

	return 0;
}
