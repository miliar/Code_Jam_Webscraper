#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,k;
	cin >> t;
	for (int i=0;i<t;i++) {
		scanf("%d %d",&n,&k);
		int mult=1;
		for (int j=0;j<n;j++) {
			if (k&mult) mult*=2; else break;
			if (j==n-1) {mult=0; break;}
		}
		if (mult) printf("Case #%d: OFF\n",i+1); else printf("Case #%d: ON\n",i+1);
		//if (k&((int)pow(2.,n-1))) printf("Case #%d: ON\n",i+1); else printf("Case #%d: OFF\n",i+1);
	}
}