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

const int maxn=1000000+10;
const int maxm=0;
const double esp=1e-3;
const int BASE=0;

int i,j,r;
int n;
int c;
long long d;
long long pos[maxn];
long long cur[maxn];
void enter(){
	scanf("%d%d",&c,&j);d=j;
	d*=2;
	int p,v;n=0;
	for (int i=1;i<=c;i++){
		scanf("%d%d",&p,&v);
		p*=2;
		for (int j=1;j<=v;j++){
			n++;
			pos[n]=p;
		}
	}
}
inline bool ok(long long l){
	int i,j;
	cur[1]=pos[1]-l;
	long long next;
	for (i=2;i<=n;i++){
		next=cur[i-1]+d;
		if (next<=pos[i]-l) cur[i]=pos[i]-l;else
			if (next>pos[i]+l) return false;else cur[i]=next;
	}
	return true;
}
void solve(){
	long long l=-1,r=((long long)d/2)*n,mid;
	while (l+1<r){
		mid=(l+r)/2;
		if (ok(mid)) r=mid;else l=mid;
	}
	if (r%2==0) cout<<r/2<<".0";else cout<<r/2<<".5";
}
int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for (r=1;r<=test;r++){
		if (r!=1) cout<<endl;
		cout<<"Case #"<<r<<": ";
		enter();
		solve();
	}
	return 0;
}

