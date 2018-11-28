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

const int maxn=100+5;
const int maxm=0;
const double esp=1e-3;
const int BASE=0;

int i,j;
double wp[maxn],owp[maxn],oowp[maxn];
int win[maxn],lost[maxn];
int a[maxn][maxn];
int n;
void enter(){
	cin>>n;
	string s;
	for (int i=1;i<=n;i++){
		cin>>s;
		for (int j=0;j<n;j++) if (s[j]=='.') a[i][j+1]=-1;else
			if (s[j]=='0') a[i][j+1]=0;else a[i][j+1]=1;
	}
}
void solve(){
	memset(win,0,sizeof(win));
	memset(lost,0,sizeof(lost));
	memset(wp,0,sizeof(wp));
	memset(owp,0,sizeof(owp));
	memset(oowp,0,sizeof(oowp));
	for (int i=1;i<=n;i++){
		for (j=1;j<=n;j++) if (a[i][j]!=-1){
			if (a[i][j]==1) win[i]++;else lost[i]++;
		}
		wp[i]=(double)win[i]/(win[i]+lost[i]);
	}
	int u,v;
	int cnt;
	for (int i=1;i<=n;i++){
		cnt=0;
		for (int j=1;j<=n;j++) if (a[i][j]!=-1){
			cnt++;
			u=win[j];
			v=lost[j];
			if (a[j][i]==0) v--;else u--;
			owp[i]+=(double)u/(u+v);
		}
		owp[i]/=cnt;
	}
	double sum;
	for (int i=1;i<=n;i++){
		cnt=0;sum=0;
		for (int j=1;j<=n;j++) if (a[i][j]!=-1){
			cnt++;
			sum+=owp[j];
		}
		oowp[i]=sum/cnt;
	}
	for (int i=1;i<=n;i++) printf("%.9lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
}
int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for (int r=1;r<=test;r++){
		//if (r!=1) cout<<endl;
		cout<<"Case #"<<r<<":"<<endl;
		enter();
		solve();
	}
	//cout<<endl<<clock()<<" ms";
	return 0;
}

