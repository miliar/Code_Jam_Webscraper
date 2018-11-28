#include <iostream>
#include <cstdio>
using namespace std;
int c[50];
int main() {
	int t;
	int n,k;
	int var = 0;
	//freopen("2.txt","r",stdin);
	//freopen("1.txt","w",stdout);
	scanf("%d",&t);
	while( t-- ) {
		scanf("%d%d",&n,&k);
		k %= 1<<n;
		for(int i = 1 ; i <= n ; i ++ ) {
			int l = 1<<i;
			int s = k%l;
			if(s < l/2) c[i] = 0;
			else c[i] = 1;
		}
		bool flag = true;
		for(int i = 1 ; i <= n ; i ++ ) {
			if(c[i] == 0) {
				flag = false;
				break;
			}
		}
		if(flag == true) printf("Case #%d: ON\n",++var);
		else printf("Case #%d: OFF\n",++var);
	}
	return 0;
}
