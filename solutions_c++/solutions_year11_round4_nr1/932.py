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

const int maxn=1000+10;
const int maxm=0;
const double esp=1e-9;
const int BASE=0;
struct mw{
	int x,y;
	int speed;
};
int i,j;
mw c[maxn];
mw a[maxn*2];
int x,s,r,t,n;
int cnt;
inline bool compare(const mw &a,const mw &b){
	return a.speed<b.speed;
}
void enter(){
	cin>>x>>s>>r>>t>>n;
	r-=s;
	for (int i=1;i<=n;i++) cin>>c[i].x>>c[i].y>>c[i].speed;
	int pos=0;
	cnt=0;
	for (int i=1;i<=n;i++){
		if (c[i].x!=pos){
			cnt++;
			a[cnt].x=pos;
			a[cnt].y=c[i].x;
			a[cnt].speed=s;
		}
		cnt++;
		a[cnt].x=c[i].x;
		a[cnt].y=c[i].y;
		a[cnt].speed=c[i].speed+s;
		pos=c[i].y;
	}
	if (pos!=x){
		cnt++;
		a[cnt].x=pos;
		a[cnt].y=x;
		a[cnt].speed=s;
	}
}
void solve(){
	n=cnt;
	sort(a+1,a+1+n,compare);
	double res=0;
	double est;
	double remain=t;
	for (int i=1;i<=n;i++){
		est=((double)a[i].y-a[i].x)/(r+a[i].speed);
		if (est<=remain-esp){
			res+=est;
			remain-=est;
		}else{
			res+=(remain+((double)(a[i].y-a[i].x)-remain*(r+a[i].speed))/a[i].speed);
			remain=0;
		}
	}
	printf("%.9lf",res);
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

