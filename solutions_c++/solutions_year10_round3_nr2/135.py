#include <iostream>
#include <cmath>
using namespace std;

#define LL long long

LL l,p,c;

int solve() {
	int ret = 0;
	for(int i = 0;true;++i) {
		LL tmp = powl(c,i);
		if(tmp * l >= p)return (int)ceil(log(i)/log(2));
	}
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cas = 1;
	while(T--) {
		cin >> l >> p >> c;
		cout << "Case #" << cas++ << ": " << solve() << endl;
	}
	return 0;
}
