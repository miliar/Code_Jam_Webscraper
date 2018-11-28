#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(int ac,char* av[])
{
	int nt; cin >> nt;
	for (int n=1; n<=nt; n++) {
		int c; cin >> c;
		map<string, char> mc;
		string s;
		for (int i=0; i<c; i++) {
			cin >> s;
			mc.insert(pair<string, char>(s.substr(0, 2), s[2]));
			string k;
			k.append(1, s[1]);
			k.append(1, s[0]);
			mc.insert(pair<string, char>(k, s[2]));
		}
		cin >> c;
		map<char, char> mo;
		for (int i=0; i<c; i++) {
			cin >> s;
			mo.insert(pair<char, char>(s[0], s[1]));
			mo.insert(pair<char, char>(s[1], s[0]));
		}
		cin >> c;
		cin >> s;

		for (int i=2; i<=s.length(); i++) {
			{
			map<string, char>::iterator mci;
			string last2 = s.substr(i-2, 2);
			if ((mci=mc.find(last2)) != mc.end()) {
				string r = s.substr(0, i-2);
				r.append(1, mci->second);
				r.append(s.substr(i));
				s = r;
				i--;
				continue;
			}
			}

			{
			char last = s[i-1];
			map<char, char>::iterator mi = mo.find(last);
			if (mi!=mo.end()) {
				// int p = s.find(mi->second);
				int p = s.substr(0, i-1).find(mi->second);
				if (p!=string::npos) {
					// string r;// = s.substr(0, p);
					// if (i<s.length()) r.append(s.substr(i));
					s = s.substr(i);;
					i = 1;
					// if (i<1) i = 1;
				}
			}
			}
		}

		cout << "Case #" << n << ": [";
		int k=0;
		if (k<s.length()) {
			cout << s[k];
		}
		for (k++;k<s.length(); k++) {
			cout << ", " << s[k];
		}
		cout << ']' << endl;
	}
	return 0;
}

