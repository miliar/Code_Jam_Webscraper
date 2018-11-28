/*#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
int main () {
	freopen ("","r",stdin);
	freopen ("","w",stdout);
	return 0;
}*/
#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
int main () {
	freopen ("A-large.in","r",stdin);
	freopen ("a-large.txt","w",stdout);
	__int64 n,pd,pg;
	int t;
	scanf ("%d",&t);
	int i;
	for (i=1;i<=t;i++) {
		scanf ("%I64d%I64d%I64d",&n,&pd,&pg);
		/*if (pd < pg) {
			printf ("Case #%d: Broken\n",i);
			continue;
		}
		if (pd == 0) {
			if (pg == 0) {
				printf ("Case #%d: Possible\n",i);
			} else {
				printf ("Case #%d: Broken\n",i);
			}
			continue;
		}
		if (pg == 0) {
			if (pd == 0) {
				printf ("Case #%d: Possible\n",i);
			} else {
				printf ("Case #%d: Broken\n",i);
			}
			continue;
		}
		

		if (n >= pg) {
			printf ("Case #%d: Possible\n",i);
			continue;
		}
		int j;
		for (j =1 ;j<=n;j++) {
			if ((pd*j)%pg == 0) {
				printf ("Case #%d: Possible\n",i);
				break;
			}
		}
		if (j == n+1){
			printf ("Case #%d: Broken\n",i);
		}*/
		if (pg == 0) {
			if (pd == 0) {
				printf ("Case #%d: Possible\n",i);
			} else {
				printf ("Case #%d: Broken\n",i);
			}
			continue;
		}
		if (pg == 100) {
			if (pd == 100) {
				printf ("Case #%d: Possible\n",i);
			} else {
				printf ("Case #%d: Broken\n",i);
			}
			continue;
		}
		if (n>=100) {
			printf ("Case #%d: Possible\n",i);
			continue;
		}
		int j;
		for (j =1 ;j<=n;j++) {
			if ((pd*j)%100 == 0) {
				printf ("Case #%d: Possible\n",i);
				break;
			}
		}
		if (j == n+1){
			printf ("Case #%d: Broken\n",i);
		}
	}

	return 0;
}