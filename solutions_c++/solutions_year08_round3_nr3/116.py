#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque> 
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<ctime>
#include<queue>
#include<ext/hash_map>
#include<ext/hash_set>
using namespace std; 
using namespace __gnu_cxx;

#define ForEach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
typedef long long int i64;
template<class T,class U> T cast (U x) {T y;ostringstream a;a<<x;istringstream b(a.str());b>>y;return y;} 

const i64 MOD=1000000007;

int main(){

	//Start here
	int ncases;  cin>>ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		int n,m; i64 X,Y,Z; cin>>n>>m>>X>>Y>>Z;
		i64 a[m];
		for (int i=0;i<m;++i) cin>>a[i];
		i64 b[n];
		for (int i=0;i<n;++i){
			int j=i%m;
			b[i]=a[j];
			a[j]=(X*a[j]+Y*(1+i))%Z;
			//cerr<<i<<' '<<b[i]<<endl;
		}
		i64 c[n]; memset(c,0,sizeof c);
		for (int i=0;i<n;++i){
			c[i]=1;
			for (int j=0;j<i;++j){
				if (b[j]<b[i]){
					c[i]=(c[i]+c[j])%MOD;
				}
			}
		}
		i64 ret=0;
		for (int i=0;i<n;++i) ret=(ret+c[i])%MOD;
		cout<<"Case #"<<ncase<<": "<<ret<<endl;
	}
 	return 0;
}
