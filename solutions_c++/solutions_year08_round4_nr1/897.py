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
#include<cstring>
#include<ext/hash_map>
#include<ext/hash_set>
using namespace std; 
using namespace __gnu_cxx;

#define ForEach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
typedef long long int i64;
template<class T,class U> T cast (U x) {T y;ostringstream a;a<<x;istringstream b(a.str());b>>y;return y;} 

const int n=10010;
const int inf=1<<25;
int main(){

	//Start here
	int ncases; cin>>ncases; 
	for (int ncase=1;ncase<=ncases;++ncase){
		vector<int> g(n),c(n),a(n);
		vector<vector<int> > f(n,vector<int>(2,inf));
		int m,v; cin>>m>>v;
		for (int i=1;i<=(m-1)/2;++i){
			cin>>g[i]>>c[i];
		}
		for (int i=1+(m-1)/2;i<=m;++i){
			cin>>a[i];
			f[i][a[i]]=0;
		}
		for (int i=m-1>>1;i>0;--i){
			int x=i*2; int y=1+x;
			for (int j=0;j<2;++j){
				if (g[i]){
					if (j){
						f[i][j]<?=f[x][1]+f[y][1];
						if (c[i]) f[i][j]<?=1+(f[x][1]<?f[y][1]);
					}else{
						f[i][j]<?=f[x][0]<?f[y][0];
						if (c[i]) f[i][j]<?=1+(f[x][0]+f[y][0]);
					}
				}else{
					if (j){
						f[i][j]<?=f[x][1]<?f[y][1];
						if (c[i]) f[i][j]<?=1+(f[x][1]+f[y][1]);
					}else{
						f[i][j]<?=f[x][0]+f[y][0];
						if (c[i]) f[i][j]<?=1+(f[x][0]<?f[y][0]);
					}
				}
			}
		}
		if (f[1][v]==inf) cout<<"Case #"<<ncase<<": "<<"IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<ncase<<": "<<f[1][v]<<endl;
	}
 	return 0;
}
