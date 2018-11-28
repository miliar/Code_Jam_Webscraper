#include <iostream>
#include <vector>
#include <cstdio>
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SIZE(v) (LL)(v.size())
using namespace std;
typedef long long LL;
typedef pair<LL,LL> pi;
void dodawaj(LL &r, LL &k, LL &n, vector<LL> &grupy, LL &sol, LL &akt, bool konczyc, vector<pi>& wyniki) {
    LL ile = 0, tmp = 0, ostakt = akt;
    while((wyniki[akt] == MP(-1LL,-1LL) || konczyc) && r > 0) {
	wyniki[akt] = MP(sol, ile++);
// 	printf("akt to %lld, wyniki to %lld,%lld\n", akt, sol, ile);
	tmp = 0;
	while(tmp + grupy[akt] <= k) {
	    tmp += grupy[akt];
// 	    printf("Wsiada %lld\n", grupy[akt]);
	    akt++;
	    if(akt == grupy.size()) akt = 0; // faster than modulo
	    if(akt == ostakt) break;
	}
// 	printf("biore na przejazd %lld ludzi, a r to %lld.\n", tmp, r);
	ostakt = akt;
	sol += tmp;
	r--;
    }
    wyniki[akt] = MP(sol-wyniki[akt].FI,ile-wyniki[akt].SE);
//     printf("po przejazdach r to %lld, akt to %lld, wyniki to %lld,%lld\n", r, akt, wyniki[akt].FI, wyniki[akt].SE);
}
int main() {
    LL T;
    scanf("%lld", &T);
    for(LL i=1; i<=T; i++) {
	LL r,k,n;
	scanf("%lld %lld %lld", &r, &k, &n);
	vector<LL> grupy;
	vector<pi> wyniki;
	wyniki.resize(n+1, MP(-1,-1));
	while(n--) {
	    LL x;
	    scanf("%lld", &x);
	    grupy.PB(x);
	}
	LL akt = 0, sol = 0;
	dodawaj(r,k,n,grupy,sol,akt,false, wyniki);
// 	printf("przejechalem, r to %lld\n", r);
	sol += wyniki[akt].FI * (r / wyniki[akt].SE);
	r %= wyniki[akt].SE;
// 	printf("nowe r to %lld, sol to %lld\n", r,sol);
	dodawaj(r,k,n,grupy,sol,akt, true, wyniki);
	printf("Case #%lld: %lld\n", i, sol);
    }
    return 0;
}