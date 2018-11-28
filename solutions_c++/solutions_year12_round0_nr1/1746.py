#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

__int64 ans, n;
map <char, char> mp;

void learn (string code, string ans) {
    for (int i = 0; i < code.size(); ++i) {
        /*if (mp.count(code[i]) != 0 && mp[code[i]] != ans[i]) {
            cerr << "strange!" << endl;
            cerr << code[i] << " -> " << ans[i] << endl;
        }*/
        mp[code[i]] = ans[i];
        
    }
}


int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    
    string
        code1 = "y qee z",
        code2 = "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        code3 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        code4 = "de kr kd eoya kw aej tysr re ujdr lkgc jv",
        ans1 = "a zoo q",
        ans2 = "our language is impossible to understand",
        ans3 = "there are twenty six factorial possibilities",
        ans4 = "so it is okay if you want to just give up";

    learn(code1, ans1);
    learn(code2, ans2);
    learn(code3, ans3);
    learn(code4, ans4);

	int T;
	cin >> T;
    string buf;
    getline(cin, buf);
	for (int test = 1; test <= T; ++test) {
		ans = 0;
        string s;
		getline(cin, s);		
		cout << "Case #" << test << ": ";
        for (int i = 0; i < s.size(); ++i) {
            cout << mp[s[i]];
        }
        cout << endl;
	}
	return 0;
}