#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;
string s[] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi", 
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
	"de kr kd eoya kw aej tysr re ujdr lkgc jv", 
	"y qee"
};
string t[] = {
	"our language is impossible to understand", 
	"there are twenty six factorial possibilities", 
	"so it is okay if you want to just give up", 
	"a zoo"
};
int main()
{
	char m[128] = { 0 };
	for (int i=0; i<4; ++i)
		for (int j=0; j<s[i].size(); ++j)
			m[s[i][j]] = t[i][j];
	for (int i='a'; i<='z'; ++i) if (m[i]==0) {
		int c[128] = { 0 };
		for (int j='a'; j<='z'; ++j) if (m[j]) c[m[j]]++;
		for (int j='a'; j<='z'; ++j) if (!c[j]) m[i] = j;
	}

	string input;
	int T;
	getline(cin, input);
	T = atoi(input.c_str());
	for (int testcase=1; testcase<=T; ++testcase) {
		getline(cin, input);
		string res;
		for (int i=0; i<input.size(); ++i) res += m[input[i]];
		cout << "Case #" << testcase << ": " << res << endl;
	}
	return 0;
}
