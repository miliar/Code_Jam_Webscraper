#include <cstdio>
#include <cmath>
using namespace std;

int main() {
	int te,Ta,na,ke,da,p;
	scanf ("%d",&te);

	for(Ta = 1; Ta <= te; Ta++) {
		scanf ("%d%d",&na,&ke);
		p = pow(2.0,(double)na);
		if (ke % p == p-1) printf("Case #%d: ON\n",Ta);
		else printf("Case #%d: OFF\n",Ta);
	}
	return 0;
}
