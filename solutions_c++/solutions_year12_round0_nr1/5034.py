#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main() {
	int n;
	string map = "yhesocvxduiglbkrztnwjpfmaq";
	string temp;
	cin >> n;
	getline(cin,temp);
	for (int count=0; count<n; count++) {
		getline(cin,temp);
		cout << "Case #" << count+1 << ": ";
		for (int j=0;j<temp.size();j++) {
			if (temp[j]==' ')
				cout << ' ';
			else
				cout << map[temp[j]-97];
		}
		cout << endl;
	}
	return 0;
}
