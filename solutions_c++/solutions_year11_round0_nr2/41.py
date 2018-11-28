#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	vector<string> c;
	vector<string> d;
	for (int t=1;t<=T;t++) {
		int C;
		c.clear();
		d.clear();
		cin >> C;
		for (int i=0;i<C;i++) {
			string str,str2;
			cin >> str;
			str2=str;
			str2[0]=str[1];str2[1]=str[0];
			c.push_back(str);c.push_back(str2);
		}
		int D;
		cin >> D;
		for (int i=0;i<D;i++) {
			string str,str2;
			cin >> str;
			str2=str;
			str2[0]=str[1];str2[1]=str[0];
			d.push_back(str);d.push_back(str2);
		}
		sort(c.begin(),c.end());
		sort(d.begin(),d.end());

		int N;
		cin >> N;
		string str, list;

		cin >> list;

		for (unsigned int i=0;i<list.length();i++) {
			char C=list[i];

			// check combination
			if (str.length()) {
				string comb;
				comb.push_back(C);
				comb.push_back(*str.rbegin());
				vector<string>::iterator it=lower_bound(c.begin(),c.end(),comb);
				if (it!=c.end()) {
					comb.push_back((*it)[2]);
					if (comb.compare(*it)==0) *str.rbegin()=(*it)[2];
					else str.push_back(C);
				}
				else str.push_back(C);
			}
			else str.push_back(C);
			// check clearing
			C=*str.rbegin();
			string Cstr;
			Cstr.push_back(C);
			vector<string>::iterator it=lower_bound(d.begin(),d.end(),Cstr);
			while (it!=d.end() && (*it)[0]==C) {
				unsigned int pos=str.find_first_of((*it)[1]);
				if (pos!=string::npos) {
					str.clear();
					break;
				}
				it++;
			}
		}

		cout << "Case #" << t << ": [";
		if (!str.empty()) cout << str[0];
		for (unsigned int i=1;i<str.length();i++) cout << ", " << str[i];
		cout << "]" << endl;

	}
	return 0;
}
