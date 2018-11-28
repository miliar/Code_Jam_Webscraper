#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int check(vector<vector<char> > pattern, string word){
	for (int i = 0; i < word.size(); i++){
		bool ok = false;
		for (int j = 0; j < pattern[i].size(); j++){
			if (pattern[i][j] == word[i]) ok = true;
		}
		if (!ok) return 0;
	}
	return 1;
}

void sol(){
	int l, d, n;
	scanf("%d%d%d",&l,&d,&n);
	vector <string> dict;	
	vector <vector<char> > pattern;
	dict.clear();
	for (int i = 0; i < d; i++){
		string buf;
		cin >> buf;
		dict.push_back(buf);
	}
	char tr = getc(stdin);
	for (int i = 0; i < n; i++){ cerr << i << endl;
		pattern.clear();
		int j = 0,ans = 0;
		char c = 0; 
		pattern.resize(1);
		while (c != '\n'){
			c = getc(stdin);
			if (c == '(') {
				while (c != ')'){
					c = getc(stdin);
					if (c != ')'){
						pattern[j].push_back(c);
					}
				}
				pattern.resize(++j + 1);
			}
			else 
				if (c != '\n') {pattern[j].push_back(c);pattern.resize(++j + 1);}
		}
		for (j = 0; j < d; j++) ans += check(pattern,dict[j]);
		cout << "Case #"<< i + 1 << ": " << ans << endl;
	}
}

int main(){
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	sol();
	fclose(stdin); fclose(stdout);
	return 0;
}