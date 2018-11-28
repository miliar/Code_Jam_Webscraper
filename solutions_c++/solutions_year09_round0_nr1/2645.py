#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
	int l, d, n, i, j, k;
	vector<string> words, ptn;
	string tokens, line;
	const char *word;
	char ch;
	int pos, cnt;
	cin >> l >> d >> n;
	getline(cin, line);
	for(i = 0; i < d; i++){
		getline(cin, line);
		words.push_back(line);
	}

	for(i = 0; i < n; i++){
		getline(cin, line);
		ptn.clear();
		for(j = 0; j < line.length(); j++){
			ch = (line.c_str())[j];
			if(ch == '('){
				pos = line.find(')', j + 1);
				tokens = line.substr(j + 1, pos - j - 1);
				j += tokens.length() + 1;
			} else {
				tokens = ch;
			}
			ptn.push_back(tokens);
		}
		cnt = d;
		for(j = 0; j < d; j++){
			word = words[j].c_str();
//			cout << word << endl;
			for(k = 0; k < l; k++){
//				cout << ptn[k] << " : " << word[k] << endl;
				if(ptn[k].find(word[k], 0) == ptn[k].npos){
					cnt--;
					break;
				}
			}
		}
		cout << "Case #" << (i + 1) << ": " << cnt << endl;
	}
	return 0;
}