#include <iostream>
using namespace std;
	int a[100];
	int n;
	int ok(){
		for(int i=0; i<n; i++){
			if(a[i]<i){
				return false;
			}
		}
		return true;
	}
int main(){
	int t;
	cin >> t;
	for(int kase=1; kase<=t; kase++){
		memset(a,0,sizeof a);
		cin >>n;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				char c;
				while(1){
					scanf("%c", &c);
					if(c=='0'||c=='1'){
						break;
					}
				}
				//cout<<i<<" "<<j<<endl;
				if(c=='1'){
					a[i]=j;
				}
			}
		}
			//for(int i=0; i<n; i++){
				//cout<<a[i]<<endl;
			//}
			int ans=0;
		for(int i=0; i<n; i++){
			for(int j=i; j<n; j++){
				if(a[j]<=i){
					for(int t=j; t>i; t--){
						swap(a[t],a[t-1]);
						ans++;
					}
					break;
				}
			}
		}
		cout<<"Case #"<<kase<<": "<<ans<<endl;
	}
}

