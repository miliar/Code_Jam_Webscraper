#include <iostream>
#include <string>
using namespace std;
int main(){
	char table[] = "yhesocvxduiglbkrztnwjpfmaq";
	int c;
	cin>>c;
	cin.unsetf(std::ios::skipws);
	for(int i = 0; i<=c; i++){
		char s;
		string r = "";
		while(cin.get(s) && s != '\n'){
			if(s == ' '){
				r += ' ';
			}else{
				r += char(table[s-97]);
			}
		}
		if(i)cout<<"Case #"<<i<<": "<<r<<endl;
	}
	return 0;
}