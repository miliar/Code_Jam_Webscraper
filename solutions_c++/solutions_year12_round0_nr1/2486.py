#include <iostream>
#include <vector>
#include <math.h>
#include <map>
#include <string>

using namespace std;

void learn(map<char,char> &m) {
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

	string o1 = "our language is impossible to understand";
	string o2 = "there are twenty six factorial possibilities";
	string o3 = "so it is okay if you want to just give up";

	for (int i=0; i<s1.length(); i++) {
		m.insert(map<char,char>::value_type(s1[i], o1[i]));
        }
	for (int i=0; i<s2.length(); i++) {
		m.insert(map<char,char>::value_type(s2[i], o2[i]));
        }
	for (int i=0; i<s3.length(); i++) {
		m.insert(map<char,char>::value_type(s3[i], o3[i]));
        }
	m.insert(map<char,char>::value_type('y', 'a'));
	m.insert(map<char,char>::value_type('q', 'z'));
	m.insert(map<char,char>::value_type('e', 'o'));
	m.insert(map<char,char>::value_type('z', 'q'));
}

void mm(map<char,char> &m, string &s) {
	for (int i=0; i<s.length(); i++) {
		char c;
		c = m[s[i]];
		cout << c;
        }
	cout << endl;
}

int main(void) {
	int t;
        string ss;
	map<char,char> m;
	learn(m);

	getline(cin, ss);
	t = atoi(ss.c_str());
	for (int i=0; i<t; i++) {
		cout << "Case #" << (i+1) << ": ";
		string s;
		getline(cin, s);
		mm(m, s);
	}

}
