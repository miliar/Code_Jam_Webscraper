#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<cstring>
using namespace std;

int main(void){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int cs;
	scanf("%d",&cs);
	int th;
	for(th=1;th<=cs;th++){
		int n,k;
		scanf("%d%d",&n,&k);
		int a=(1<<n);
		k%=a;
		if(k==a-1) printf("Case #%d: ON\n", th);
		else printf("Case #%d: OFF\n", th);
	}
	return 0;
}