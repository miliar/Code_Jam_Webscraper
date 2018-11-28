#include <stdio.h>

using namespace std;

struct state {
	bool elec;
	bool tog;
};

state light[50];

int pwr(int x) {
	if (x==1) return 2;
	return 2*pwr(x-1);
}

int main (){
	int t,n,k,ii,tmp;
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	scanf ("%d",&t);
	for (ii=1;ii<=t;ii++) {
		scanf ("%d%d",&n,&k);
		tmp = pwr(n);
		printf ("Case #%d: ",ii);
		if ((k+1)%tmp==0) printf ("ON\n");
		else printf ("OFF\n");
	}
	return 0;
}
