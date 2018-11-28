/*
 * http://code.google.com/codejam/contest/1460488/dashboard#s=p0
 * Problem A. Speaking in Tongues
 */

#include <iostream>
#include <string>
#include <map>

using namespace std;

string solve(const string& G)
{
	static const char* hint_in[] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	};
	static const char* hint_out[] = {
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"
	};
	map<char, char> translator;
	for (int i='a'; i<='z'; i++) {
		translator[i] = i;
	}
	translator['q'] = 'z';	//???
	translator['z'] = 'q';	//???

	for (int i=0; i<sizeof hint_in/sizeof hint_in[0]; i++) {
		const char* in = hint_in[i];
		const char* out = hint_out[i];
		while (*in && *out) {
			translator[ *in++ ] = *out++;
		}
	}

	string text;
	for (int i=0; i<G.size(); i++) {
		text += translator[ G[i] ];
	}

	return text;
}

int main()
{
	int T;
	cin >> T;
	string cr;
	getline(cin, cr);
	for (int i=1; i<=T; i++) {
		string G;
		getline(cin, G);
		cout << "Case #" << i << ": " << solve(G) << endl;
	}
	return 0;
}
