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

struct k {
	double a,b,c;
};

int ls(k a,k b) {
	return (a.c<b.c);
}

void solve() {
	double x,s,r,t;
	int n;
	cin >> x >> s >> r >> t >> n;
	vector<k> a(n+1);
	for (int i=0;i<n;i++) {
		cin >> a[i].a >> a[i].b >> a[i].c;
		x-=a[i].b-a[i].a;
		a[i].c+=s;
	}
	a[n].a=0;
	a[n].b=x;
	a[n].c=s;
	r-=s;
	sort(a.begin(),a.end(),ls);
	double res=0;
	for (int i=0;i<=n;i++) {
		double rs=a[i].b-a[i].a,sp=a[i].c;
		double tr=rs/(sp+r);
		if (tr<t) {
			res+=tr;
			t-=tr;
		} else {
			res+=t+(rs-t*(r+sp))/sp;
			t=0;
		}
	}
	print(res);
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
