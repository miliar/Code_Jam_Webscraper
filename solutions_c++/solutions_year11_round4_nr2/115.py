#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <ctime>
#include <cmath>
#include <memory>
#include <cstring>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef set<int> SI;
typedef map<int,int> MII;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> VVII;
typedef vector<LL> VL;
typedef vector<VL> VLL;
typedef set<LL> SL;
typedef map<LL,LL> MLL;
typedef pair<LL,LL> LLL;
typedef vector<LD> VD;
typedef vector<VD> VVD;

template<typename T>
inline T sqr(const T &a){return a*a;}

string itoa(int a) {
	string res;
	while (a>0) {
		res+=a%10+'0';
		a/=10;
	}
	reverse(res.begin(),res.end());
	return res;
}

int testcounter=0;
ofstream ouf;

template <typename T>
void print(T s) {
	testcounter++;
	cout << "Case #" << testcounter << ": " << s << endl;
	ouf << "Case #" << testcounter << ": " << s << endl;
}

void precalc() {
}

VLL a,s,h,v,sh,sv;
int n,m;
void build() {
	s.assign(n+1,VL(m+1,0));
	sh=sv=h=v=s;
	//for (int i=0;i<n;i++) {
		//v[i][0]=a[i][0]*i;
		//if (i>0) {
			//s[i][0]=s[i-1][0]+a[i][0];
			//sv[i][0]=sv[i-1][0]+v[i][0];
		//}
	//}
	//for (int i=0;i<m;i++) {
		//h[0][i]=a[0][i]*i;
		//if (i>0) {
			//s[0][i]=s[0][i-1]+a[0][i];
			//sh[0][i]=sh[0][i-1]+v[0][i];
		//}
	//}
	for (int i=1;i<=n;i++) {
		for (int j=1;j<=m;j++) {
			h[i][j]=a[i][j]*j;
			v[i][j]=a[i][j]*i;
			s[i][j]=a[i][j]+s[i-1][j]+s[i][j-1]-s[i-1][j-1];
			sh[i][j]=h[i][j]+sh[i-1][j]+sh[i][j-1]-sh[i-1][j-1];
			sv[i][j]=v[i][j]+sv[i-1][j]+sv[i][j-1]-sv[i-1][j-1];
		}
	}
}

bool getdisk(int x,int y,int r) {
	x++;y++;
//	cout << x << ' ' << y << ' ' << r << endl;
	LL hsum=sh[x+r-1][y+r-1]-sh[x-1][y+r-1]-sh[x+r-1][y-1]+sh[x-1][y-1];
	LL vsum=sv[x+r-1][y+r-1]-sv[x-1][y+r-1]-sv[x+r-1][y-1]+sv[x-1][y-1];
	LL sum=s[x+r-1][y+r-1]-s[x-1][y+r-1]-s[x+r-1][y-1]+s[x-1][y-1];
	hsum-=h[x][y]+h[x+r-1][y]+h[x][y+r-1]+h[x+r-1][y+r-1];
	vsum-=v[x][y]+v[x+r-1][y]+v[x][y+r-1]+v[x+r-1][y+r-1];
	sum-=a[x][y]+a[x+r-1][y]+a[x][y+r-1]+a[x+r-1][y+r-1];
	if (2*vsum!=(2*x+r-1)*sum) return 0;
	if (2*hsum!=(2*y+r-1)*sum) return 0;
	return 1;
}

void solve() {
	int d;
	cin >> n >> m >> d;
	a.assign(n+1,VL(m+1,0));
	for (int i=1;i<=n;i++) {
		string s;
		cin >> s;
		for (int j=1;j<=m;j++) {
			a[i][j]=s[j-1]-'0'+d;
		}
	}
	build();
	for (int i=min(n,m);i>=3;i--) {
		for (int x=0;x<=n-i;x++)
			for (int y=0;y<=m-i;y++)
				if (getdisk(x,y,i)) {
					print(i);
					return;
				}
	}	
	print("IMPOSSIBLE");
}

int main () {
//	ios_base::sync_with_stdio=0;
	freopen("input.txt","r",stdin);
	ouf.open("output.txt");
	precalc();
	int n;
	cin >> n;
	for (int i=0;i<n;i++) solve();
}
