#include <iostream>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int tt=1; tt<=t; tt++){
		long long n,k;
		cin>>n>>k;
		long long pow=1;
		for (int i=1; i<=n; i++) pow*=2LL;
		printf("Case #%d: ",tt);
		if (k%pow==pow-1LL) printf("ON\n"); else printf("OFF\n");
	}
}