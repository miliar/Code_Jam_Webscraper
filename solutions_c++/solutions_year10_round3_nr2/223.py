#include<iostream>
using namespace std;
int main(){
	int T;
	cin>>T;
	for(int k=1;k<=T;++k){
		long long l,p,c;
		int ans;
		cin>>l>>p>>c;
		long long t=l,sum=1;
		for(int i=0;;++i){
			if(t*c>=p){
				ans=i;
				break;
			}
			for(int j=0;j<sum;++j){
				t*=c;
				if(t*c>=p)
					break;
			}
			sum*=2;
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}
