#include <iostream>
#include <string>

using namespace std;

bool ismax(string s){
	bool yes = true;
	for (int i=1; i<s.length(); ++i){
		if (s[i-1]<s[i]){
			yes = false;
			break;
		}
	}
	return yes;
}

string smallest(string n){
	sort(n.begin(), n.end());
	return n;
}

void print_next(string n){
//	cout << "Dealing with " << n << endl;
	if (ismax(n)){
		n = '0'+n;
	}
//	cout << "Checking " << n.substr(1, n.length()-1) << endl;
	if (ismax(n.substr(1, n.length()-1))) {
		char smallchar = '9';
		char lower = n[0];
		int pos = -1;
		for (int i=0; i<n.length(); ++i){
			if (n[i]<=smallchar && n[i]>lower){
				pos = i;
				smallchar = n[i];
			}
		}
		cout << smallchar;

		n[pos] = n[0];
//		cout << endl << "NOW GO TO " << n << endl;
		cout << smallest(n.substr(1, n.length()-1));
	} else {
		cout << n[0];
		print_next(n.substr(1, n.length()-1));
	}
}

int main(){
	int T;
	string n;
	int n_digit;

	cin >> T >> ws; 

	for (int cnt = 1; cnt <=T; ++cnt){
		getline(cin, n);
		
		cout << "Case #" << cnt << ": ";
		print_next(n);
		cout << endl;
	}


	return 0;
}
