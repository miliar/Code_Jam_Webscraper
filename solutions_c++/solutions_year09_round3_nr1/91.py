#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cctype>
#include <cmath>
#include <numeric>
#include <sstream>
using namespace std;
typedef long long ll;

typedef vector<int> VI;
typedef vector<VI> VVI; 

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))

ll doit( const string &s ) {
	if(s.size()==1) return 1;
	int len = s.size();

	vector<ll> digit(len,-1);
	digit[0] = 1;
	for(int i=1;i<len;++i) if(s[0]==s[i]) digit[i] = 1;
	for(int i=1;i<len;++i) if(digit[i]==-1) {
		digit[i] = 0;
		for(int j=i+1;j<len;++j) if(s[i]==s[j]) {
			digit[j] = 0;
		}
		break;
	}
	int num = 1;
	REP(i,len) if(digit[i]==-1) {
		++num;
		digit[i] = num;
		for(int j=i+1;j<len;++j) {
			if(s[i]==s[j]) digit[j] = num;
		}
	}
	ll base = num + 1;
	ll ret = 0;
	ll mul = 1;
	for(int i=len-1;i>=0;--i) {
		ret += mul * digit[i];
		mul *= base;
	}
	return ret;
}

int main() {
	freopen("d:\\incomming\\A-large.in","r",stdin);
	int tn;
	cin >> tn;
	REP(cc,tn) {
		string s;
		cin >> s;
		printf("Case #%d:", cc+1);
		printf(" %I64d\n", doit( s ) );
	}
}


