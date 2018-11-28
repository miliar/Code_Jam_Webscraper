#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>

#define lint long long int
using namespace std;
lint a[10000];
lint b[10000];

int cint(double x){
	return (int) floor(x+0.5);
}

int slv(lint l, lint r, int c)
{
	if (l*c>=r) return 0;
	if (l>=r) {cerr<<"WTF???\n"; return 0;}

	int x = cint(sqrt(l*r));

	return 1+max(slv(l,x,c), slv(x,r,c));
}

int solve() {
	int l,p,c; scanf("%d%d%d", &l,&p,&c);
	return slv(l,p,c);
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int i=1; i<=T; ++i) printf("Case #%d: %d\n", i, solve() );
}
