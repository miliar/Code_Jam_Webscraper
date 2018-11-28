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

int n,m;
VL a,A,b,B;
VLL dyn;

LL solvedyn(int x,int y) {
//	cerr << x << ' ' << y << endl;
	if (x==n || y==m) return 0;
	if (dyn[x][y]!=-1) return dyn[x][y];
	if (A[x]!=B[y]) {
		return dyn[x][y]=max(solvedyn(x+1,y),solvedyn(x,y+1));
	}
	LL &ans=dyn[x][y];
	ans=0;
	LL cura=a[x],curb=b[y],curpass=0;
	while (x<n && y<m) {
		LL cur = min(cura,curb);
		curpass+=cur;
		cura-=cur;
		curb-=cur;
		ans=max(ans,curpass+solvedyn(x+1,y+1));
		if (cura==0) {
			x++;
			while (x<n && A[x]!=B[y]) x++;
			if (x<n)cura = a[x];
		}
		if (curb==0) {
			y++;
			while (y<m && A[x]!=B[y]) y++;
			if (y<m)curb = b[y];
		}
	}
	ans = max(ans, curpass);
	return ans;
}

void solve() {
	cin >> n >> m;
	a=A=VL(n);
	b=B=VL(m);
	dyn=VLL(n,VL(m,-1));
	for (int i=0;i<n;i++) cin >> a[i] >> A[i];
	for (int i=0;i<m;i++) cin >> b[i] >> B[i];
	print(solvedyn(0,0));
}

int main () {
//	ios_base::sync_with_stdio=0;
	freopen("input.txt","r",stdin);
	ouf.open("output.txt");
	precalc();
	int n;
	cin >> n;
	ouf<< fixed << setprecision(20);
	for (int i=0;i<n;i++) solve();
}
