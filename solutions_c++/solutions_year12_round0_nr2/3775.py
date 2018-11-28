#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	int t;cin>>t;
	for(int i=1;i<=t;i++){
		int n,s,p,num[101],ans=0;
		cin>>n>>s>>p;
		for(int j=0;j<n;j++)cin>>num[j];
		sort(num,num+n,greater<int>());
		for(int j=0;j<n&&num[j]>=p;j++){
			if(num[j]/3>=p||(num[j]/3==p-1&&num[j]%3))ans++;
			else if(s&&(num[j]/3==p-1||(num[j]/3==p-2&&num[j]%3==2))){
				ans++;
				s--;
			}
		}
		cout<<"Case #"<<i<<": ";
		cout<<ans<<endl;
	}
}
