#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <utility>
#include <bitset>
//#include <hash_map>
//#include <hash_set>

#define MP make_pair
#define F first
#define S second
#define PB push_back

template<typename T> T gcd(T a,T b){return (a>b?(gcd(b,a)):(a==0?b:(gcd(b%a,a))));};
template<typename T> inline T sqr(T a){return a*a;};
template<typename T> inline T gmax(T a,T b){return (a>b?a:b);};
template<typename T> inline T gmin(T a,T b){return (a<b?a:b);};

using namespace std;
//using namespace __gnu_cxx;

const int maxn=0;
const int maxm=0;
const double esp=1e-3;
const int BASE=0;

int i,j;
map<pair<char,char>,char> combined;
set<pair<char,char> > opposed;
int c,d,n;
string in,out;
void enter(){
	combined.clear();
	opposed.clear();
	cin>>c;
	string s;
	for (int i=0;i<c;i++){
		cin>>s;
		combined.insert(MP(MP(s[0],s[1]),s[2]));
		combined.insert(MP(MP(s[1],s[0]),s[2]));
	}
	cin>>d;
	for (int i=0;i<d;i++){
		cin>>s;
		opposed.insert(MP(s[0],s[1]));
		opposed.insert(MP(s[1],s[0]));
	}
	cin>>n;
	cin>>in;
	out="";
}
inline void process(){
	char T;
	map<pair<char,char>,char>::iterator it;
	if (out.length()>1){
		it=combined.find(MP(out[out.length()-1],out[out.length()-2]));
		if (it!=combined.end()){
			T=it->S;
			out.erase(out.length()-2,2);
			out+=T;
		}
	}
	int len=out.length();
	T=out[len-1];
	bool ok=false;
	for (int i=0;i<len-1;i++){
		if (opposed.find(MP(T,out[i]))!=opposed.end()){
			ok=true;
			break;
		}
	}
	if (ok) out="";
}
void solve(){
	for (int i=0;i<n;i++){
		out+=in[i];
		process();
	}
	cout<<'[';
	for (int i=0;i<(int)out.length()-1;i++) cout<<out[i]<<", ";
	if (out.length()>0) cout<<out[out.length()-1];
	cout<<']';
}
int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for (int r=1;r<=test;r++){
		if (r!=1) cout<<endl;
		cout<<"Case #"<<r<<": ";
		enter();
		solve();
	}
	//cout<<endl<<clock()<<" ms";
	return 0;
}

