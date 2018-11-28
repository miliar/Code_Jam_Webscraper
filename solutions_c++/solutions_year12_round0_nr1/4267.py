#include <iostream>
#include <string>

using namespace std;

int main(){
	string map="yhesocvxduiglbkrztnwjpfmaq";
	int t;
	cin>>t;
	cin.get();
	string s;
	for(int T=1;T<=t;T++){
		getline(cin,s);
		for(int i=0;i<s.length();++i){
			s[i]=s[i]==' '?s[i]:map[s[i]-'a'];
		}
		cout<<"Case #"<<T<<": "<<s<<endl;
	}
	return 0;
}