#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main() {
	vector<string> a, b;
	map<char, char> m;
	a.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	a.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	a.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
	b.push_back("our language is impossible to understand");
	b.push_back("there are twenty six factorial possibilities");
	b.push_back("so it is okay if you want to just give up");
	for(int i = 0; i < (int)a.size(); ++i) {
		for (int j = 0; j < (int)a[i].size(); ++j) {
			//if (a[i][j]>='a' && a[i][j] <= 'z')
				m[a[i][j]] = b[i][j];
		}
	}
	m['y'] = 'a'; m['e'] = 'o'; m['q'] = 'z'; m['z'] = 'q';
	
/*	for(map<char, char>::iterator it = m.begin(); it != m.end(); ++it) {
		++cnt;
		cout << it->first << " = " << it->second << endl;
	}
*/
	int n = 0;
	cin >> n;
	cin.get();
	for (int i = 0; i < n; ++i) {
		char buf[101];
		cin.getline(buf, 101);
		string s(buf);
		//cin >> s;
		for (int j = 0; j < (int)s.size(); ++j)
			s[j] = m[s[j]];
		cout << "Case #" << i+1 << ": " << s << endl;
	}
	return 0;
}