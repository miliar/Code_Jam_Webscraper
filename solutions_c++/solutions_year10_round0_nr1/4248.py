#include <iostream>
#include <cstdio>

using namespace std;



int main() {
	freopen("A.in.txt", "r", stdin);
	freopen("A.out.txt", "w", stdout);
	int t,ca=1;
	scanf("%d",&t);
	while(t--){
		int n,k;
		scanf("%d%d",&n,&k);
		int con = (1<<n)-1,d = 1<<n;
		int ans = k%d;
		if(ans==con){
			printf("Case #%d: ON\n",ca++);
		}
		else{
			printf("Case #%d: OFF\n",ca++);
		}
	}
    	return 0;
}

