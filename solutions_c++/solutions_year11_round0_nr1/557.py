#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;

int main () {
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
	int ca,test;
	scanf ("%d",&test);
	for (ca =1;ca<=test;ca++) {
		int m;
		scanf ("%d",&m);
		
		int left0=0,leftb=0,ans=0;
		int x=1,y=1;
		for (int i=0;i<m;i++) {
			char a,b;
			int c;
			cin>>a>>c;
			if (a == 'O') {
				int inc = fabs (c-x);
				if (inc <= left0) inc = 0;
				else inc -= left0;
				inc++;
				ans += inc;
				left0 = 0;
				leftb += inc;
				x = c;
			} else {
				int inc = fabs (c-y);
				if (inc <= leftb) inc = 0;
				else inc -= leftb;
				inc++;
				ans += inc;
				leftb = 0;
				left0 += inc;
				y = c;
			}
		}
		printf ("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
