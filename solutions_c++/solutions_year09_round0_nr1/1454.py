#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

typedef long long LL;

const int WORDS = 5009;
const int LEN = 19;

string word[WORDS];
string s;

int main(){
	int words, len, tests;
	scanf("%d %d %d", &len, &words, &tests);

	for (int i = 0; i < words; i++)
		cin >> word[i];
	
	//for (int i = 0; i < words; i++) printf("palavra %d = %s\n", i, word[i].c_str());
	
	for (int t = 0; t < tests; t++){
		cin >> s;
		int size = s.size(); //printf("entrada = %s\n", s.c_str());
		LL ans = 0;

		for (int i = 0; i < words; i++){
			bool ok = false, okk = true, open = false;
			int pos = 0;

			for (int j = 0; j < size; j++){
				if (s[j] == '('){ open = true; continue;}
				if (open && s[j] == ')'){
					pos++; open = false;
					if (!ok) okk = false;
					ok = false;
					continue;
				}
				if (s[j] == word[i][pos]) ok = true;

				if (!open){
					pos++;
					if (!ok) okk = false;
					ok = false;
				}
			}

			if (okk) ans++;
		}

		printf("Case #%d: %I64d\n", t + 1, ans);
	}

	return 0;
}
