#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <queue>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <iostream>

using namespace std;

int main() {
	int t,n,b[105],tes=1;
	int posa,posb,timea,timeb,time;
	char a[105];
	scanf("%d",&t);getchar();
	while (t--) {
		scanf("%d",&n);
		for (int i=0;i<n;i++) {
			getchar();
			scanf("%c %d",&a[i],&b[i]);	
		}
		posa=1; posb=1;
		timea=0; timeb=0;
		time=0;
		for (int i=0;i<n;i++) {
			if (a[i]=='O') {
				time=max(abs(b[i]-posa)+timea,time)+1;		
				timea=time;
				posa=b[i];
			} else {
				time=max(abs(b[i]-posb)+timeb,time)+1;		
				timeb=time;
				posb=b[i];
			}	
		}
		printf("Case #%d: %d\n",tes++,time);
	}
	return 0;
}
