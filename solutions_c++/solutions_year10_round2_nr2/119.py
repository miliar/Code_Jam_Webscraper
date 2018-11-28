#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#define FI first
#define SE second
#define MP make_pair
#define FI first
#define SE second
#define PB push_back
using namespace std;
typedef long long lol;
typedef pair<lol,lol> pi;
int main() {
    int z;
    scanf("%d", &z);
    for(int nr=1; nr<=z; nr++) {
	lol n,k,b,t;
	scanf("%lld %lld %lld %lld", &n, &k, &b, &t);
	vector<pi> kury;
	while(n--) {
	    pi tmp;
	    scanf("%lld", &tmp.FI);
	    kury.PB(tmp);
	}
	for(int i=0; i<kury.size(); i++)
	    scanf("%lld", &kury[i].SE);
	sort(kury.begin(), kury.end());
	lol iledop = 0, sol=0, ileok = 0;
	for(int i=kury.size()-1; i>=0 && ileok < k; i--) {
	    if((b - kury[i].FI) <= t * kury[i].SE) {
		sol += iledop;
		ileok++;
	    }
	    else
		iledop++;
	}
	printf("Case #%d: ", nr);
	if(ileok < k)
	    printf("IMPOSSIBLE\n");
	else
	    printf("%lld\n", sol);
    }
    return 0;
}