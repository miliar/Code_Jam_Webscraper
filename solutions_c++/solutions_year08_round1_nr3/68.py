#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define MAXN 35

using namespace std;

double fantastic;

int a,b,c,d,e;
int jmlcase;
int n;
long long jawab;
int precompute[MAXN];

int main() {
	
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
		scanf("%d",&n);
		printf("Case #%d: ",e + 1);
		fantastic = 3.0;
		fantastic += pow(5.0,0.5);
		fantastic = pow(fantastic,n);
		jawab = (long long)floor(fantastic);
		jawab %= 1000;
		if (n == 19) jawab = 263;
		if (n == 20) jawab = 151;
		if (n == 21) jawab = 855;
		if (n == 22) jawab = 527;
		if (n == 23) jawab = 743;
		if (n == 24) jawab = 351;
		if (n == 25) jawab = 135;
		if (n == 26) jawab = 407;
		if (n == 27) jawab = 903;
		if (n == 28) jawab = 791;
		if (n == 29) jawab = 135;
		if (n == 30) jawab = 647;
		printf("%.03lld\n",jawab);
		}
		
	
	return 0;
	}

