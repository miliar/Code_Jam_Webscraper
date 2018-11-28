#include <iostream>

using namespace std;

int notp[1111111];

int main(){
	int t = 0;
	cin >> t;
	for(int c=0 ;c<t;c++){
		printf("Case #%d: ", c+1);
		int n;
		cin >> n;
		memset(notp,0,sizeof(notp));
		for(int i=2;i<1111111;i++){
			if(!notp[i]){
				for(int j=i*2;j<1111111;j+=i)
					notp[j]=1;
			}
		}
		long long ans = 0;
		for(int i=2;i*i<=n;i++)
			if(!notp[i]){
				int cnt=0;
				long long cur=i;
				while(cur<=n){
					cnt++;
					cur *= i;
				}
				ans += cnt-1;
			}
		if(n==1)
			ans=-1;
		cout << ans+1 << endl;
	}
	
	return 0;
}
