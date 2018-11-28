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

void solve() {
	LD c,d;
	cin >> c >> d;
	VD x(c),y(c);
	for (int i=0;i<c;i++) cin >> x[i] >> y[i];
	LD l=0,r=1e30;
	for (int ii=0;ii<200;ii++) {
		LD mr=-1e100;
		LD m=(l+r)/2;
		bool ok=1;
		for (int i=0;i<c;i++) {
			for (int j=0;j<y[i];j++) {
				if (x[i]+m<mr+d) {
					ok=0;
				}
				mr=max(mr+d,x[i]-m);
			}
		}
		if (ok) r=m; else l=m;
	}
	print(r);
	
	//for (int i=0;i<c;i++) {
		//int x,y;
		//cin >> x >> y;
		//LD d1=x-(y-1.)*d/2,d2=x+(y-1.)*d/2;
		//res=max(res,x-d1);
		//if (pos+d<d1) pos=d2; else {
			//d2+=min(pos+d-d1,res);
			//d1+=min(pos+d-d1,res);
			//if (pos+d<d1) pos=d2; else {
				//res+=(pos+d-d1)/2;
				//d2+=(pos+d-d1)/2;
				//d1+=(pos+d-d1)/2;
				//pos=d2;
			//}
		//}
	//}
	//print(res);
}

int main () {
//	ios_base::sync_with_stdio=0;
	freopen("input.txt","r",stdin);
	ouf.open("output.txt");
	precalc();
	int n;
	cin >> n;
	cout << fixed << setprecision(20);
	ouf << fixed << setprecision(20);
	for (int i=0;i<n;i++) solve();
}
