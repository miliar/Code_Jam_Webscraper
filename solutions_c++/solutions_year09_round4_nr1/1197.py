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
 
const int inf=1<<20;
int main(){
	int ncases; cin>>ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		int n; cin>>n;
		int a[n];
		for (int i=0;i<n;++i){
			string s; cin>>s;
			a[i]=0;
			for (int j=0;j<n;++j){
				if (s[j]=='0') continue;
				a[i]|=1<<j;
			}
		}
		int b[n]; for (int i=0;i<n;++i) b[i]=i;
		int best=inf;
		do{
			bool ok=1;
			for (int i=0;i<n;++i){
				ok&=a[i]<(1<<b[i]+1);
			}
			if (!ok) continue;
			int t=0;
			int c[n]; for (int i=0;i<n;++i) c[i]=i;			
			for (int i=0;i<n;++i){
				int j=0; while(c[j]!=b[i]) ++j;
				for (int p=j-1;p>=i;--p){
					swap(c[p],c[1+p]); ++t;
				}							
			}
			best=min(best,t);
		}while(next_permutation(b,b+n));
		cout<<"Case #"<<ncase<<": "<<best<<endl;
	}	
	return 0;
}
