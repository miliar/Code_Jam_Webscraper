#include <iostream>
#include <string>

using namespace std;

int main(){
/*	char key[27]="--------------------------";
	for(int i=0;i<3;i++){
		string s,a;
		getline(cin,s);
		getline(cin,a);
		int j;
		j=0;
		while(j<s.length()){
			if(s[j]!=' ') key[s[j]-'a']=a[j];
			j++;
		}

	}
	cout<<key<<endl;
	return 0;
*/
	char key[27]="yhesocvxduiglbkrztnwjpfmaq";
	int T;
	string s;
	cin>>T;
	getline(cin,s);
	for(int i=0;i<T;i++){
		getline(cin,s);
		for(int j=0;j<s.length();j++)
			if(s[j]!=' ')
				s[j]=key[s[j]-'a'];

		cout<<"Case #"<<i+1<<": "<<s<<endl;
	}
	return 0;
}
