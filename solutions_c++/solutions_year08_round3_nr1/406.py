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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;
#define inf 987654321
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++) 
#define FR(i,x,y) for(int i=x;i<y;++i)
#define FRZ(i,y) FR(i,0,y)
typedef long long int ll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ll> vl;
#define CS c_str()
#define PB push_back
#define SZ size()
int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("ou1.txt","wt",stdout);
    int test ;
    scanf("%d",&test);
    FRZ(z,test)
    {
	ll ans = 0 , P ,K , L;
	cin>>P>>K>>L;
	if(P * K < L)
	{
	cout<<"Case #"<<z+1<<": "<<"Impossible" <<endl;	
	continue;
	}
	vector<ll> arr(L);
	ll x;
	FRZ(i,L)
	{
	    scanf("%lld",&x);
	    arr[i] = x;
	}
	sort(arr.begin(),arr.end(),greater<ll>());
	int n =arr.SZ;
	    int y = 0;
	    FRZ(i,P)
	    {
		FRZ(j,K)
		{
		    if(y >= n) break;
		    ans += arr[y++] *(i+1);
		}
	    }
	cout<<"Case #"<<z+1<<": "<< ans<<endl;
    }
}
