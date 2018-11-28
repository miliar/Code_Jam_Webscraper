#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;i++){
		long n,k;
		scanf("%d%lld",&n , &k);
		
		int x=1;
		for(int j=1;j<=n;j++, k>>=1){
			x&=k;
		}
		if(x==1)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}
