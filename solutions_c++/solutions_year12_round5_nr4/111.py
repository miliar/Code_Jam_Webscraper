#include <iostream>
using namespace std;
int main(){
	int i,k,t;
	char a,b,c,d;
	string s;
	cin >> s;
	a = b = c = d = 0;
	for (i=0;i<s.length();++i){
		a = c;
		b = d;
		c = s[i];
		d = 0;
		switch (s[i])		{
			case 'o':d = '0';break;
			case 'i':d = '1';break;
			case 'e':d = '3';break;
			case 'a':d = '4';break;
			case 's':d = '5';break;
			case 't':d = '7';break;
			case 'b':d = '8';break;
			case 'g':d = '9';break;
		}
		if (a){
			cout << a << c << endl;
			if (d)
				cout << a << d << endl;
			if (b){
				cout << b << c << endl;
				if (d)
					cout << b << d << endl;
			}
		}
	}
}
