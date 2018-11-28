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
 

int M,N,ncases; 
string A[5050];

void g(const string& s, vector<string>&v){
	if (!s.size()) return;
	if (s[0]=='('){
		int i=1; while(s[i]!=')') ++i;
		string x=s.substr(1,i-1); sort(x.begin(),x.end());
		v.push_back(x);
		g(s.substr(1+i),v);
	}else{
		v.push_back(string(1,s[0]));
		g(s.substr(1),v);
	}
} 

int main(){	
	cin>>M>>N>>ncases; for (int i=0;i<N;++i) cin>>A[i];
	for (int ncase=1;ncase<=ncases;++ncase){
		string s; cin>>s;
		vector<string> v;
		g(s,v);
		int r=0;
		for (int i=0;i<N;++i){
			bool ok=1;
			for (int j=0;ok&&j<M;++j){
				ok&=binary_search(v[j].begin(),v[j].end(),A[i][j]);
			}
			if (ok) ++r;
		}
		cout<<"Case #"<<ncase<<": "<<r<<endl;
	}
	return 0;
}
