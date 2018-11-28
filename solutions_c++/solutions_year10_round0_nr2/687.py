/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define VL vector<LL>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define MP(x,y) make_pair(x,y)
#define f first
#define s second
#define VP vector<PI>
#define S(t)	scanf("%d",&t)

int main(){
	int t;
	cin>>t;
	FF(i,1,t+1){
		int n;
		cin>>n;
		VL v(n);
		LL mn=10000000000000000LL;
		F(k,n){
			cin>>v[k];
			mn=min(mn,v[k]);
		}
		sort(ALL(v));
		LL ans=v[1]-v[0];
		F(k,n)	FF(j,k+1,n){
			ans=__gcd(ans,(v[j]-v[k]));
		}
		LL mult=mn/ans+(mn%ans!=0);
		printf("Case #%d: %d\n",i,ans*mult-mn);
	}
	return 0;
}
