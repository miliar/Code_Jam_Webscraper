#include <stdio.h>
#include <iostream>

using namespace std;

int gcd(int a,int b) {
	if (a==0) return b;
	if (b==0) return a;
	if (a%b==0) return b;
	return gcd(b,a%b);
}

int mut(int a) {
	if (a<0) a*=-1;
	return a;
}

int main () {
	int t,n,i,ii,a1,a2,T;
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	scanf ("%d",&t);
	for (ii=1;ii<=t;ii++) {
		scanf ("%d",&n);
		scanf ("%d",&a1);
		for (i=0;i<n-1;i++) {
			scanf ("%d",&a2);
			if (i==0) T = mut(a2-a1);
			else T = gcd(T,mut(a2-a1));
			a1 = a2;
		}
		printf ("Case #%d: ",ii);
		int x = a1%T;
		if (x==0) printf ("0\n");
		else printf ("%d\n",T-x);
	}

}
