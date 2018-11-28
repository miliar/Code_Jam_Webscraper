#include<iostream>
#include<string>
#include<cstring>
using namespace std;

int main(){
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	for(int i=1;i<=t;i++){
		getline(cin,s);
		int num[36];
		memset(num,255,sizeof num);
		num[s[0]=s[0]>'9' ? s[0]-'a'+10 : s[0]-'0']=1;
		int cur=1;
		for(int j=1;j<s.length();j++)
			if(num[s[j]=s[j]>'9' ? s[j]-'a'+10 : s[j]-'0']==-1){
				num[s[j]]=cur-(cur==1);
				cur++;
			}
		if(cur<2)cur=2;
		long long ans=0;
		for(int j=0;j<s.length();j++)
			ans=ans*cur+num[s[j]];
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}