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
#include <cstring>
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
//#include<ext/hash_map>
//#include<ext/hash_set>
using namespace std;
using namespace __gnu_cxx;
 
#define ForEach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
typedef long long int i64;
template<class T,class U> T cast (U x) {T y;ostringstream a;a<<x;istringstream b(a.str());b>>y;return y;}
const int M=1000;
int main(){
	int ncases; cin>>ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		string s; cin>>s;
		bool seen[M]; memset(seen,0,sizeof seen);
		for (int i=0;i<s.size();++i) seen[s[i]]=1;
		int b=0;for (int i=0;i<M;++i) b+=seen[i];
		b=max(2,b);
		int u[M]; memset(u,-1,sizeof u);
		u[s[0]]=1;
		int x=0;
		for (int i=0;i<s.size();++i){	
			if (u[s[i]]>-1) continue;
			u[s[i]]=x++;
			if (x==1) ++x;
		}
		
		i64 ret=0;
		for (int i=0;i<s.size();++i){
			ret=ret*b + u[s[i]];
		}
		cout<<"Case #"<<ncase<<": "<<ret<<endl;
	}
	return 0;
} 
