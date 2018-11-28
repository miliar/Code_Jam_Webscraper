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


string st;
int num[]={2,3,5,7};
int n;
int ret=0;
void f(i64 lv, bool ls, i64 cv, int s){
	if (s==n){
		i64 u;
		if (!ls)u=lv+cv;
		else u=lv-cv;
		for (int i=0;i<4;++i) if (u%num[i]==0) {
				++ret; break;
		}
		return;
	}
	for (int i=0;i<3;++i){
		if (!i){
			i64 u;
			if (!ls){
				u=lv+cv;
				f(u,0,st[s]-'0',1+s);
			}else{
				u=lv-cv;
				f(u,0,st[s]-'0',1+s);
			}
		}
		else if (i==1){
			i64 u;
			if (!ls){
				u=lv+cv;
				f(u,1,st[s]-'0',1+s);
			}else{
				u=lv-cv;
				f(u,1,st[s]-'0',1+s);
			}			
		}
		else{
			f(lv, ls, cv*10+(st[s]-'0'), 1+s);
		}
	}
}


int main(){

	//Start here
	int ncases; cin>>ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		cin>>st;
		n=st.size();
		ret=0;
		f(0,0,st[0]-'0',1);
		cout<<"Case #"<<ncase<<": "<<ret<<endl;
	}
 	return 0;
}
