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

VI primes;
int N=1000000;
void precalc() {
	VI resh(N,1);
	for (LL i=2;i<N;i++) {
		if (resh[i]) {
			primes.push_back(i);
			for (LL j=i*i;j<N;j+=i)
				resh[j]=0;
		}
	}
}

void solve() {
	LL n;
	cin >> n;
	if (n==1) print(0); else {
		int res=1;
		for (int i=0;i<primes.size();i++) {
			LL p=primes[i];
			LL stp=p*p;
			//if (stp>n) break;
			while (stp<=n) {
				res++;
				stp*=p;
			}
		}
		print(res);
	}
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
