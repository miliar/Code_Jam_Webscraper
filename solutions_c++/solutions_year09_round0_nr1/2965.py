#include <iostream>
using namespace std;

int main() {
	int l, d, n;
	cin>>l>>d>>n;
	char words[5000][16];
	for(int i = 0; i < d; i++) {
		cin>>words[i];
		//cout<<words[i]<<endl;
	}
	cin.ignore();
	for(int i = 0; i < n; i++) {
		int count = 0;
		bool notMatches[5000] = {false};
		for(int j = 0; j < l; j++) {
			char letter = cin.get();
			if(letter != '(') {
				for(int k = 0; k < d; k++) {
					if(words[k][j] != letter) notMatches[k] = true;
				}
			}
			else {
				char group[256];
				cin.get(group, sizeof(group), ')');
				cin.ignore();
				//cout<<j<<": "<<group<<endl;
				for(int a = 0; a < d; a++) {
					if(!notMatches[a]) {
						bool found = false;
						for(int k = 0; !found && group[k] != '\0'; k++) {
							if(words[a][j] == group[k]) found = true;
						}
						if(!found) notMatches[a] = true;
					}
				}
			}
		}
		cin.ignore();
		for(int j = 0; j < d; j++) {
			if(!notMatches[j]) {count++;/* cout<<"Line: "<<j<<endl;*/}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}

