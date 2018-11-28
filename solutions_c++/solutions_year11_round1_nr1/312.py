#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int N,Pd,Pg;
	int J;
	scanf("%d",&J);
	for(int j=1;j<=J;++j) {
		scanf("%d%d%d",&N,&Pd,&Pg);
		bool pos = false;
		if(Pg == 100) pos = (Pd == 100);
		else for(int a=1;a<=min(N,100);++a) {
			if(a*Pd % 100 == 0) pos = true;
		}
		if(Pg == 0 && Pd > 0) pos = false;
		printf("Case #%d: ",j);
		if(pos) printf("Possible\n");
		else printf("Broken\n");
	}
	return 0;
}
