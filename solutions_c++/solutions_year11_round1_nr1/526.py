#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime> 
using namespace std; 

#define PB push_back 
#define MP make_pair 

#define rep(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,l,h) for(int i=(l);i<=(h);++i) 
#define FORD(i,h,l) for(int i=(h);i>=(l);--i) 
#define print(expr) cout<<(#expr)<<" : "<<(expr)<<endl

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
typedef long long int64; 
typedef pair<int,int> pii; 

int64 gcd(int64 a,int64 b){ return b==0 ? a : gcd(b,a%b);}
int64 lcm(int64 a,int64 b){ return a/gcd(a,b)*b;}

int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T; cin>>T;
	FOR(Case,1,T)
	{
		int64 n,pd,pg;
		cin>>n>>pd>>pg;
		int64 t = (int64)100/gcd(100,pd);
		//int64 p = pg/gcd(pd,pg);
		if(n>=t && !(pg==100 && pd<100) && !(pg==0 && pd>0)) cout<<"Case #"<<Case<<": "<<"Possible\n";
		else cout<<"Case #"<<Case<<": "<<"Broken\n";
	}
	return 0;
}