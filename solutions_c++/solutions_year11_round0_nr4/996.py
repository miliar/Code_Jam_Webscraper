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
	int n;
	cin >> n;
	int res=0;
	for (int i=0;i<n;i++) {
		int a;
		cin >> a;
		if (i+1!=a) res++;
	}
	print(res);
}

int main () {
//	ios_base::sync_with_stdio=0;
	freopen("D-large.in","r",stdin);
	ouf.open("output.txt");
	precalc();
	int n;
	cin >> n;
	for (int i=0;i<n;i++) solve();
}
