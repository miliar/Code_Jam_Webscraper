#include <iostream>
#include <cstdio>
using namespace std;
int main(int argc, char** argv) {
	int n,tc,s,p,j,i,nn,ns,t;
	scanf("%d\n",&tc);
	for(i=1;i<=tc;i++)
	{
		nn=0;ns=0;
		scanf("%d",&n);
		scanf("%d",&s);
		scanf("%d",&p);
		p = 3*p - 2;
		for(j=0;j<n;j++) {
			scanf("%d",&t);
			if(t >= p) {
				nn++;
			} else if((p-2) >=0 && t >= (p-2)) {
				ns++;
			}
		}
		ns = ns<=s?ns:s;
		nn = nn + ns;
		printf("Case #%d: %d\n",i,nn);
	}
	return 0;
}
