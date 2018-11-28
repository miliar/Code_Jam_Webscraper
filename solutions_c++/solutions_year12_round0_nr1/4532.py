#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
	typedef vector<string> vs;
	vs encoded;
	encoded.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	encoded.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	encoded.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");

	vs decoded;
	decoded.push_back("our language is impossible to understand");
	decoded.push_back("there are twenty six factorial possibilities");
	decoded.push_back("so it is okay if you want to just give up");

	vector<char> map(256);
	map[' '] = ' ';
	map['y'] = 'a';
	map['e'] = 'o';
	map['q'] = 'z';


	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < encoded[i].size(); ++j) {
			map[encoded[i][j]] = decoded[i][j];
		}
	}

	int sum = 0;
	for (int i = 'a'; i <= 'z'; ++i) sum += i - map[i];
	map['z'] = static_cast<char>(sum);
	//for (char i = 'a'; i <= 'z'; ++i) cout << i << " " << map[i] << endl;
	
	int T;
	cin >> T;
	string S;
	//read till \n
	getline(cin, S);
	for (int case_number = 1; case_number <= T; ++case_number) {
		getline(cin, S);
		for(int i = 0; i < S.size(); ++i) {
			S[i] = map[S[i]];
		}
		cout << "Case #" << case_number << ": " << S << endl;
	}
}

