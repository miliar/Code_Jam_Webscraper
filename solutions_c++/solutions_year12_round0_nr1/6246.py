#include <iostream>
#include <string.h>

using namespace std;

int main() {
	char mapping[]="yhesocvxduiglbkrztnwjpfmaq";
	int T;
	cin>>T;
	char s[T][120];
	cin.ignore(120,'\n');
	for(int t=0;t<T;t++) {
		//
		cin.getline(s[t],120);
	}
	for(int t=0;t<T;t++) {
		for(int i=0;i<strlen(s[t]);i++) {
			if(s[t][i]==' ') continue;
			int x=s[t][i]-97;
			s[t][i]=mapping[x];
		}
		cout<<"Case #"<<t+1<<": "<<s[t]<<endl;
	}	
	return 0;
}
