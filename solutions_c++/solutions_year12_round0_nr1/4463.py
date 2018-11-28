#include <iostream>
#include <string>

using namespace std;

char letters[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a','q'};


int main(){
	int T;
	cin >> T;
	cin >> ws;
	string in;
	int cas = 1;
	while(T--){
		cout << "Case #" << cas << ": "; 
		++cas;
		getline(cin,in);
		for(int i = 0; i < in.length(); ++i){
			if(in[i] != ' '){
				cout << letters[in[i]-'a'];
			}
			else{
				cout << ' ';
			}
		}
		cout << endl;
	}
}

