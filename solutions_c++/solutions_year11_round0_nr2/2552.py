#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void print_ret(int i, vector<char> s) {
	cout << "Case #" << i << ": [";
	for (int j=0; j<s.size(); j++) {
		cout << s[j];
		if (j != s.size()-1) {
			cout << ", ";
		}
	}
	cout << "]" << endl;
}

string arrange(string str) {
//	cout << "arrange " << endl;
	if (str.length() > 1) {
		char c1 = str.at(0);
		char c2 = str.at(1);
		if (c1 > c2) {
			str.at(0) = c2;
			str.at(1) = c1;
		}
	}
	return str;
}

void printv(vector<char> v) {
	for (int i=0; i<v.size(); i++) {
		cout << v[i] ;
	}
	cout << endl;
}

string comb_seek(vector<char> ret, vector<string> c_str) {
	string query = "";
	string retstr;
//	printv(ret);
	query += ret[ret.size()-2];
	query += ret[ret.size()-1];
	query = arrange(query);
	
//	cout << "q: " << query << endl;
//	cout << "com: " << endl;
	for (int i=0; i<c_str.size(); i++) {
		if (c_str[i].find(query) == 0) {
//			cout << c_str[i] << endl;
			return c_str[i].substr(2);
		}
//		cout << "comb: " << i << endl;
	}
	return retstr;
}

bool del_seek(vector<char> ret, vector<string> d_str) {
	string query = "";
	query += ret.at(ret.size()-1);

//	cout << "del: " << endl;
	for (int i=0; i<d_str.size(); i++) {
		int idx = d_str[i].find(query);
		if (idx != string::npos) {
			char q2 = d_str[i].at((idx+1)%2);
			for (int j=0; j<ret.size()-1; j++) {
				if (q2 == ret.at(j)) return true;
			}
		}
	}
	return false;
}

int main(void) { 
	int t;
	cin >> t;

	for (int i=0; i<t; i++) {
		int c, d, n;
		string tmp_str, in_str;
		vector<string> c_str, d_str;

		cin >> c;
		for (int j=0; j<c; j++) {
			cin >> tmp_str;
			c_str.push_back(arrange(tmp_str));
		}

		cin >> d;
		for (int j=0; j<d; j++) {
			cin >> tmp_str;
			d_str.push_back(arrange(tmp_str));
		}

		cin >> n;
		cin >> in_str;

		//cout << "done." << endl;
		//break;

		vector<char> ret;
		for (int j=0; j<n; j++) {
			char c = in_str.at(j);
			ret.push_back(c);	

			if (ret.size() > 1) {
				string combi = comb_seek(ret, c_str);
				if (combi.length() > 0) {
					ret.pop_back();
					ret.pop_back();
					ret.push_back(combi.at(0));
				}

				if (del_seek(ret, d_str)) {
					ret.clear();
				}
			}
//			cout << "j: " << j << endl;
		}


//		cout << "before" << endl;
		print_ret(i+1, ret);
	}
}


