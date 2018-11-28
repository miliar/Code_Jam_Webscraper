#include <iostream>
#include <cstdlib>

using namespace std;

int n,k,tt,ii,i;
bool flag;

int main() {
	freopen("snapper.in","r",stdin);
	freopen("snapper.out","w",stdout);

	scanf("%d\n",&tt);
	for (ii=1;ii<=tt;++ii) {
		scanf("%d%d\n",&k,&n);
		flag=true;
		for (i=1;i<=k;++i) {
			if (!(n & 1)) {
				flag=false;
				break;
			}
			n>>=1;
		}
		printf("Case #%d: ",ii);
		if (flag) printf("ON\n");
		else printf("OFF\n");
	}
}
