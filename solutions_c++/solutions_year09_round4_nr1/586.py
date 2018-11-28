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
#include <complex>
#include <queue>
#include <complex>
#include <ctime>
#include <ext/numeric>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

long long pows[8];

struct hash_v{
	int operator()(const vector<int>&v)const
	{
		int x=0;
		rep(i,0,v.size())
			x+=(1934*v[i])%1007;
		return x;
	}
};

hash_map<vector<int>,int ,hash_v>vis;
int n;

vector<string> aa;
char a[1001];
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("a.in","rt",stdin);
	freopen("out.out","wt",stdout);
	#endif
	int t,x;
	scanf("%d",&t);
	rep(i,0,8)
		pows[i]=power(2,i);
	rep(tt,0,t)
	{
		scanf("%d ",&n);
		printf("Case #%d: ",tt+1);
		aa.clear();
		rep(i,0,n)
			scanf("%s",a),aa.PB(a);
		int res=0;
		string ss="1";
		rep(i,0,n)
		{
			int mi = i;
			rep(j,i,aa.size())
			{
				int mm = find_end(ALL(aa[j]),ALL(ss))-aa[j].begin();
				if(mm==n)
					mm=-1;
				if(mm<=i)
				{
					mi=j;
					break;
				}
			}
			//cout<<mi<<" "<<i<<endl;
			res+=abs(mi-i);
			string s=aa[mi];
			aa.erase(aa.begin()+mi);
			aa.insert(aa.begin(),s);
			/*rep(i,0,n)
				cout<<aa[i]<<endl;*/
		}
		printf("%d\n",res);
	}
	
	return 0;
}
