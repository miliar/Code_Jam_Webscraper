#include <iostream>

using namespace std;

int main() {
	int n, i;
	char *str;
	char *tmp;
	char *s="yhesocvxduiglbkrztnwjpfmaq";
	cin>>n;
	for(i=0; i<n; i++) {
		str=new char[101];
		cin.getline(str, 101);
		tmp=str;
		while(*str) {
			if(*str>='a' && *str<='z') *str=s[*str-'a'];
			str++;
		}
		cout<<"Case #"<<(i+1)<<": "<<tmp<<endl;
	}
	return 0;
}
