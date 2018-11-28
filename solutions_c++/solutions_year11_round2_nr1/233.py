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
typedef vector<LD> VI;
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
	int n;
	cin >> n;
	VS m(n);
	for (int i=0;i<n;i++) cin >> m[i];
	VI s1(n),s2(n),s3(n),w(n),p(n);
	for (int i=0;i<n;i++) {
		w[i]=0,p[i]=0;
		for (int j=0;j<n;j++) {
			if (m[i][j]=='1') w[i]++;
			if (m[i][j]=='0') p[i]++;
		}
		s1[i]=w[i]/(w[i]+p[i]+.0);
	}
	for (int i=0;i<n;i++) {
		for (int j=0;j<n;j++) {
			if (m[i][j]=='1' || m[i][j]=='0') s2[i]+=(w[j]-m[j][i]+'0')/(w[j]+p[j]-1);
		}
		s2[i]/=w[i]+p[i];
	}
	for (int i=0;i<n;i++) {
		for (int j=0;j<n;j++) {
			if (m[i][j]=='1' || m[i][j]=='0') s3[i]+=s2[j];
		}
		s3[i]/=w[i]+p[i];
	}
	testcounter++;
	cout << "Case #" << testcounter << ": ";
	ouf << "Case #" << testcounter << ":";
	cout << fixed << setprecision(20);
	for (int i=0;i<n;i++) {
		ouf << endl << 0.25*s1[i]+0.5*s2[i]+0.25*s3[i];
		cout << endl << 0.25*s1[i]+0.5*s2[i]+0.25*s3[i];
	}
	ouf << endl;
	cout << endl;
	
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
