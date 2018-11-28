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
#include <cstring>
#include<functional>
#include<numeric>
#include<utility>
#include<ctime>
#include<queue>
//#include<ext/hash_map>
//#include<ext/hash_set>
using namespace std;
using namespace __gnu_cxx;
 
#define ForEach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
typedef long long int i64;
template<class T,class U> T cast (U x) {T y;ostringstream a;a<<x;istringstream b(a.str());b>>y;return y;}

int inf = 0x5fffffff;

int main(){
	int ncases; cin>>ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		int M, N; cin>>M>>N;
		vector<int> v(N); for (int i=0;i<N;++i){ cin>>v[i]; --v[i];}
		int best=inf;
		do{
			bool b[M]; memset(b,0,sizeof b);
			int t=0;
			for (int i=0;i<N;++i){
				int x=v[i]-1;
				while(x>-1&&!b[x]){
					++t;--x;
				}
				x=v[i]+1;
				while(x<M&&!b[x]){
					++t;++x;
				}
				b[v[i]]=1;
			}
			best=min(best,t);
		}while(next_permutation(v.begin(),v.end()));

		printf("Case #%d: %d\n",ncase, best);
	}
	return 0;
} 
