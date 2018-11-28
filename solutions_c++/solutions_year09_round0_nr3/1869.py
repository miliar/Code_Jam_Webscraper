#include<iostream>
#include<cstring>
#include<string>
using namespace std;

int main(){
	int n;
	string str;
	cin>>n;
	getline(cin,str);
	for(int i=1;i<=n;i++){
		getline(cin,str);
		int count[500];
		for(int k=0;k<str.length();k++)
			count[k]=1;
		for(const char* j="welcome to code jam\0";*j!='\0';j++){
			for(int k=0;k<str.length();k++)
				if(str[k]!=*j)
					count[k]=0;
			for(int k=1;k<str.length();k++)
				(count[k]+=count[k-1])%=10000;
		}
		int ans=count[str.length()-1];
		cout<<"Case #"<<i<<": "<<ans/1000<<ans/100%10<<ans/10%10<<ans%10<<endl;
	}
	return 0;
}