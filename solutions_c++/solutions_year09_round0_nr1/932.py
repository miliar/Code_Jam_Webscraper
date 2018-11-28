#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;


int l, d, n;
int fsa[15][26];

void construct(const string& data) {
	memset(fsa,0,sizeof(fsa));
	int p = 0;
	for (int i = 0; i < l; i++) {
		if (data[p] == '(') {
			while(data[++p] != ')') {
				fsa[i][data[p]-'a'] = 1;
			}
		} else {
			fsa[i][data[p]-'a'] = 1;
		}
		++p;
	}
}

int check(const string& word) {
	for (int i = 0; i < l; i++) {
		if (!fsa[i][word[i]-'a']) return 0;
	}
	return 1;
}

int main() {
	cin>>l>>d>>n;
	vector<string> word(d);
	for (int i = 0; i < d; i++) {
		cin>>word[i];
	}
	for (int tc = 1; tc <= n; tc++) {
		string data; cin>>data;
		construct(data);
		int cnt = 0;
		for (int i = 0; i < d; i++) {
			cnt += check(word[i]);
		}
		cout << "Case #" << tc << ": " << cnt << endl;
	}
	return 0;
}