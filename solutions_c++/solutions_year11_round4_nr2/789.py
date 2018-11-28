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

const int maxn=500+5;
const int maxm=0;
const double esp=1e-9;
const int BASE=0;

int i,j;
int m,n,d;
int a[maxn][maxn];
void enter(){
	cin>>m>>n>>d;
	string s;
	for (int i=1;i<=m;i++){
		cin>>s;
		for (int j=0;j<n;j++){
			a[i][j+1]=s[j]-'0'+d;
		}
	}
}
inline bool ok(int x1,int y1,int size){
	int x2=x1+size-1,y2=y1+size-1;
	double x=0,y=0;
	double cx=(double)(x1+x2)/2,cy=(double)(y1+y2)/2;
	for (int i=x1;i<=x2;i++)
		for (int j=y1;j<=y2;j++){
				if (i==x1&&j==y1) continue;
				if (i==x1&&j==y2) continue;
				if (i==x2&&j==y1) continue;
				if (i==x2&&j==y2) continue;
				x+=((double)i-cx)*a[i][j];
				y+=((double)j-cy)*a[i][j];
			}
	return x==0&&y==0;
}
inline bool check(int size){
	for (int i=1;i<=m-size+1;i++)
		for (int j=1;j<=n-size+1;j++)
			if (ok(i,j,size)) return true;
	return false;
}
void solve(){
	int res;
	for (res=gmin(m,n);res>=3;res--){
		if (check(res)){
			cout<<res;
			return;
		}
	}
	cout<<"IMPOSSIBLE";
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

