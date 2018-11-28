#include <cstdio>
#include <iostream>

using namespace std;

bool pattern[15][26];
string words[5000];

//#define DEBUG

int main() {
	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);

	int i,j,k;
	char buff[502];
	cin.getline(buff, 501);

	char ch;
#ifdef DEBUG
	cout << "words:"<< endl;
#endif
	for (i=0; i<D; ++i) {
		cin.getline(buff, 501);
		words[i] = buff;
#ifdef DEBUG
		cout << words[i] << endl;
#endif
	}

	string pat("");
#ifdef DEBUG
	cout << "Patterns:" << endl;
#endif
	int len, count; bool match = false;
	for (i=0; i<N; ++i) {
		for (j=0; j<L; ++j) {
			for (k=0; k<26; ++k) {
				pattern[j][k] = false;
			}
		}
	
		cin.getline(buff, 501);
		pat = buff;
#ifdef DEBUG
		cout <<  pat << ": " << endl;
#endif
		len = pat.length();
		k=0;
		for (j=0; j<len; ++j) {
			if (pat[j] == '(') {
				++j;
				while (pat[j] != ')') {
					pattern[k][pat[j]-'a'] = true;
					++j;
				}
			} else {
				pattern[k][pat[j]-'a'] = true;
			}
			++k;
		}
#ifdef DEBUG
		for (k=0; k<L; ++k) {
			for (j=0; j<26; ++j) {
				cout << (pattern[k][j]?"1":"0");
			}
			cout << endl;
		}
#endif
		count = 0;
#ifdef DEBUG
		cout << endl << "Matches" << endl;
#endif
		for (j=0; j<D; ++j) {
			match = true;
			for (k=0; k<L; ++k) {
				match = match && pattern[k][words[j][k]-'a'];
			}
			if (match) count++;
#ifdef DEBUG
			cout << "word: " << words[j] << " match: " << match << endl;
#endif
		}
		printf("Case #%d: %d\n", (i+1), count);
	}

	return 0;
}
