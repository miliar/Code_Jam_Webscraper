// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>


using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for (int ncase = 1; ncase <= T; ++ncase) {
		int c, d, n;
		cin >> c;
		string str;
		map<string, char> combo;
		set<string> opposed;
		for (int i = 0; i < c; ++i) {
			cin >> str;
			string one = str.substr(0, 2);
			string two = one;
			two[0] = one[1];
			two[1] = one[0];
			combo[one] = str[2];
			combo[two] = str[2];
		}
		cin >> d;
		for (int i = 0; i < d; ++i) {
			cin >> str;
			string two = str;
			two[0] = str[1];
			two[1] = str[0];
			opposed.insert(str);
			opposed.insert(two);
		}
		cin >> n;
		cin >> str;
		vector<char> ans;
		for (int i = 0; i < n; ++i) {
			if (ans.size() == 0)
				ans.push_back(str[i]);
			else {
				string sub(2, 0);
				sub[0] = ans.back();
				sub[1] = str[i];
				if (combo.find(sub) != combo.end()) 
					ans.back() = combo[sub];
				else {
					bool fail = false;
					for (int j = 0; j < ans.size(); ++j) {
						sub[0] = ans[j];
						if (opposed.find(sub) != opposed.end()) {
							ans.clear();
							fail = true;
							break;
						}
					}
					if (!fail)
						ans.push_back(str[i]);
				}

			}
		}
		cout << "Case #" << ncase << ": [";
		for (int i = 0; i < ans.size(); ++i) {
			cout << ans[i];
			if (i < ans.size() - 1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}

