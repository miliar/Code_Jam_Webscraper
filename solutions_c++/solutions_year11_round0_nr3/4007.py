#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;
int add(int left,int right){
	return (left^right);
}
int ans;
int t,bag[100];
int high;
int dfs(int s,int p,int pos,int sum){
		if(s==p&&pos==t&&high!=sum&&sum!=0){
			//cout<<sum<<" "<<pos<<" s="<<s<<" p="<<p<<endl;
			ans=max(ans,sum);
		}
		if(pos>=t)return 0;
		dfs(add(s,bag[pos]),p,pos+1,sum+bag[pos]);
		dfs(s,add(p,bag[pos]),pos+1,sum);
		return 0;
}


int main(){
	int ncase;
	cin>>ncase;
	for(int Case =1;Case<=ncase;Case++){
			cin>>t;
			ans=-1;
			high=0;
			for(int i=0;i<t;i++){
				cin>>bag[i];
				high+=bag[i];
			}
			dfs(0,0,0,0);
			cout<<"Case #"<<Case<<": ";
			if(ans==-1)cout<<"NO"<<endl;
			else cout<<ans<<endl;
			
	}
	return 0;
}