#include<iostream>
#include<string>
using namespace std;
int main()
{
	long long int con,t,i,k,b,n;
	cin>>t;
	int cas=1;
	con=1;
	while(t--){
		cin>>n>>k;
		int cnt=0;
		for(i=0;i<n;i++){
			if((con<<i) & k){
				cnt++;
			}
		}
		if(cnt==n){
			printf("Case #%d: ON\n",cas);
		}else{
			printf("Case #%d: OFF\n",cas);
		}
		cas++;	
	}
	return 0;
}	