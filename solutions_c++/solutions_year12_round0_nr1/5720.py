#include <iostream>
#include <string>
using namespace std;

int main(){
	string a = "yhesocvxduiglbkrztnwjpfmaq";
	string b;
	int n;
	cin >> n;
	cin.ignore();
	for (int t=0;t<n;t++){
		cout << "Case #" << t+1 << ": ";
		b = "";
		getline(cin, b);
		for (int i=0;i<b.length();i++){
			if (b[i] == ' ')
				cout << ' ';
			else
				cout << a[b[i]-'a'];
		}
		cout << endl;
	}
	return 0;
}

