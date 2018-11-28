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


int main(){

	//Start here
	int ncases; cin>>ncases; 
	for (int ncase=1;ncase<=ncases;++ncase){
		int P,K,M; cin>>P>>K>>M;
		int a[M]; for (int i=0;i<M;++i) cin>>a[i];
		sort(a,a+M,greater<int>());
		vector<int> b[K];
		int s=0;
		for (int i=0;i<M;++i){
			b[s].push_back(i);
			s=(1+s)%K;
		}
		i64 ret=0;
		for (int i=0;i<K;++i){
			for (int j=0;j<b[i].size();++j){
				ret+=1LL*(1+j)*(a[b[i][j]]);
			}
		}
		cout<<"Case #"<<ncase<<": "<<ret<<endl;
	}
 	return 0;
}
