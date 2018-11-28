#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int n,T,res,l,h,k;
int m[105];

int main () {
	freopen ("input","r",stdin);
	freopen ("output","w",stdout);
	scanf ("%d",&T);
	for (int z=0; z<T; z++) {
		res=0;
		scanf ("%d%d%d",&n,&l,&h);
		for (int i=0; i<n; i++) scanf ("%d",&m[i]);
		for (int i=l; i<=h; i++) {
			k=0;
			for (int j=0; j<n; j++) {
				if (i%m[j]==0 || m[j]%i==0) {
					k++;
				}
			}
			if (k==n) {
				res=i;
				break;
			}
		}
		if (res>0) printf ("Case #%d: %d\n",z+1,res); else printf ("Case #%d: NO\n",z+1);
	}
	return 0;
}