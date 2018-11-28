#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> word;
	for(int i = 0; i < d; i++) {
		string tmp;
		cin >> tmp;
		word.push_back(tmp);
	}
	for(int t = 0; t < n; t++) {
		string pat; cin >> pat;
		bool pos[16][32] = { false };
		for(int i = 0, j = 0; i < l; i++, j++) {
			if(islower(pat[j])) { pos[i][pat[j]-'a'] = true; continue; }
			for(j++; pat[j] != ')'; j++) pos[i][pat[j]-'a'] = true;
		}
		int cnt = 0;
		for(int i = 0; i < word.size(); i++) {
			cnt++;
			for(int j = 0; j < l; j++) if(!pos[j][word[i][j]-'a']) { cnt--; break; }
		}
		cout << "Case #" << (t+1) << ": " << cnt << endl;
	}
	return 0;
}

