#include<iostream>
using namespace std;

char de[] = "abcdefghijklmnopqrstuvwxyz";
char en[] = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
	int R;
	cin >> R;
	cin.ignore();
	for( int r  = 1 ; r <= R; r++){
		cout << "Case #"<<r<<": ";
		string s;
		getline( cin , s );
		for( int i = 0; i < s.size(); i++){
			if ( isspace(s[i])){
				cout << s[i];
				continue;
			}
			for(int j = 0; j < 26; j++){
				if ( s[i] == de[j]){
					cout << en[j];
					break;
				}
			}
		}
		cout << endl;
	}
}
