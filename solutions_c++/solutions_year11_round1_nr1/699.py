#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,d,g,gg,xg;
	__int64 n;
	cin >> t;
	for (int z=0;z<t;z++) {
		cin >> n >> d >> g;
		if (n > 100) n=100;
		xg = 0,gg = 0;
		for (int i=0;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				if ((100*i)%j==0 && (100*i)/j==d) {
					xg = 100*i;
					gg= j;
					break;
				}
			}
			if (gg!=0)break;
		}
		if (gg==0 || (g==100 && d!=100) || (d!=0 && g==0) ) 
			cout << "Case #" << z+1 << ": Broken" <<endl; 
		else cout << "Case #" << z+1 << ": Possible" <<endl; 
	}
}