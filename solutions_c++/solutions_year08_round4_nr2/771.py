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
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);    
    int test = GI;
    FR(z,1,test+1)
    {
	int N =GI,M=GI;
	ll A=GL;
	    int mi =min(N,M) , ma = max(N,M);
	if(N * M < A) 
	{
	     cout<<"Case #"<<z<<": "<<"IMPOSSIBLE" <<endl;	
	     continue;
	}
	    FRZ(x1,N+1)
	    {

	    FRZ(y1,M+1)
	    FRZ(x2,N+1)
	    FRZ(y2,M+1)
	    FRZ(x3,N+1)
	    FRZ(y3,M+1)
	    {
	         if( A == abs((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)))
		 {
		     	cout<<"Case #"<<z<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3 <<endl;		
                        goto here;			
		 }
	    }
     }

here: int x =10;
    }
}
