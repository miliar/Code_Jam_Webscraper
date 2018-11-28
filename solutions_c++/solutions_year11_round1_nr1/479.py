#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	cin >> T;
	
	for (int i = 1;i <= T;i++){
		long long N,Pd,Pg;
		cin >> N >> Pd >> Pg;
		if (Pg == 0){
			if (Pd != 0 ){
				printf("Case #%d: Broken\n",i);
				continue;
			}
			else {
				printf("Case #%d: Possible\n",i);
				continue;
			}
		}
		if (Pg == 100){
			if (Pd == 100){
				printf("Case #%d: Possible\n",i);
				continue;
			}
			else {
				printf("Case #%d: Broken\n",i);
				continue;
			}
		}
		if (100 / __gcd(100ll,Pd) <= N) printf("Case #%d: Possible\n",i);
		else printf("Case #%d: Broken\n",i);
	}
	
	return 0;
}
