#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
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

const int maxn=100+5;
const int maxm=0;
const double esp=1e-3;
const int BASE=0;

struct query{
	char command;
	int hallway;
};
int i,j;
int n;
inline query MQ(char command,int hallway){
	query temp;
	temp.command=command;
	temp.hallway=hallway;
	return temp;
}
vector<query> ss;
int time[maxn];
int last[maxn];
void enter(){
	cin>>n;
	ss.clear();
	ss.PB(MQ('O',1));
	ss.PB(MQ('B',1));
	time[0]=0;time[1]=0;
	char command;
	int hallway;
	for (i=0;i<n;i++){
		cin>>command>>hallway;
		ss.PB(MQ(command,hallway));
	}
	n+=2;
	int lastO=0,lastB=0;
	for (i=0;i<n;i++)
		if (ss[i].command=='O'){
			last[i]=lastO;
			lastO=i;
		}else{
			last[i]=lastB;
			lastB=i;
		}
}
void solve(){
	int u,v;
	for (i=2;i<n;i++){
		u=time[last[i]]+abs(ss[last[i]].hallway-ss[i].hallway)+1;
		v=time[i-1]+1;
		time[i]=gmax(u,v);
	}
	cout<<time[n-1];
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

