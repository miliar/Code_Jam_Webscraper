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
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define CS c_str()
#define PB push_back
#define SZ size()
int main()
{
	freopen("D-small-attempt0.in", "rt", stdin);
freopen("output.txt", "wt", stdout);    
    int test = GI;
    FR(z,1,test+1)
    {
	int k = GI;
	string str;
	cin>>str;
	vi a(k);
	ll fact = 1;	
	FRZ(i,k)
	{
	    fact*= i+1 ;
	    a[i] = i;
	}
	int ans= inf;
	int n =str.SZ;
	while(fact--)
	{
	    next_permutation(a.begin(),a.end());
		string str1 =str;   
	    FRZ(i,n/k)
	    {
	
		FRZ(j,a.SZ)
		{
		    str1[i*k + j] = str[i*k +a[j]];
		}
    }
		int cnt = 0;
		FRZ(j,str1.SZ)
		{
		    while( j+1 != n && str1[j] == str1[j+1])  j++;
		    cnt++;
		}
		ans = min(ans,cnt);

	    
	}
	cout<<"Case #"<<z<<": "<<ans<<endl;	
    }
}
