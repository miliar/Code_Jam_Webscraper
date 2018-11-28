#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

#define EPS 1e-10
#define PI acos(-1)

bool r,found;
int n,k,a,cn,v,t,c;


void process() {
	scanf("%d %d",&n,&k);
	--n;
	
	printf("Case #%d: ",++cn);
	if (k%(2<<n)==(2<<n)-1) printf("ON\n");
	else printf("OFF\n");
	fflush(stdout);
	
}



int main() {
	//freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int cases;
	cn=0;
	scanf("%d",&cases);
	
	while (cases--) {
		process();
	}


	return 0;
}
