#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int n,t,s,p,x,k,m[20],res;

int main () {
	freopen ("input","r",stdin);
	freopen ("output","w",stdout);
	scanf ("%d",&t);
	for (int c=0; c<t; c++) {
		scanf ("%d",&n);
		for (int j=0; j<n; j++) scanf ("%d",&m[j]);
		res=0;
		k=(1<<n)-1;
		for (int i=1; i<k; i++) {
			s=0;
			p=0;
			x=0;
			for (int j=0; j<n; j++) {
				if ((i>>j)&1) p=p^m[j]; else {
					s=s^m[j];
					x+=m[j];
				}
			}
			if (s==p && x>res) res=x;
		}
		if (res==0) printf ("Case #%d: NO\n",c+1); else printf ("Case #%d: %d\n",c+1,res);
	}
	return 0;
}