#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <string.h>

using namespace std;

int t,n,atlas,al,pbot,pl,p,m;

int main () {
	freopen ("input","r",stdin);
	freopen ("output","w",stdout);
	scanf ("%d",&t);
	for (int i=0; i<t; i++) {
		scanf ("%d",&n);
		atlas=1;
		pbot=1;
		al=0;
		pl=0;
		for (int j=0; j<n; j++) {
			scanf ("%s%d",&p,&m);
			if (p=='O') {
				pl=max(al,pl+abs(pbot-m))+1;
				pbot=m;
			}
			if (p=='B') {
				al=max(pl,al+abs(atlas-m))+1;
				atlas=m;
			}
		}
		printf ("Case #%d: %d\n",i+1,max(al,pl));
	}
	return 0;
}