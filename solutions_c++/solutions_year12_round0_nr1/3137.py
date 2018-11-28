#include <iostream>

using namespace std;

char s[27] = "yhesocvxduiglbkrztnwjpfmaq";
char r[105];
int n;
int t;


int main(){
	cin >> t;
	gets(r);

	for (int _i = 0; _i < t; ++_i){
		gets(r);
		n = strlen(r);
		cout << "Case #" << _i + 1 << ": ";
		for (int i = 0; i < n; ++i){
			if ('a' <= r[i] && r[i] <= 'z'){
				cout << s[r[i] - 'a'];
			}
			else 
				cout << r[i];
		}
		cout << endl;
	}
}