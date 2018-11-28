#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main() {
	// generate the maps
	string test[] = { "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv" };
	string testOutput[] = { "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up" };
	map<char,char> mappings;
	set<char> done;
	for (int i = 0; i < 3; i++) {
		string A = test[i];
		string B = testOutput[i];
		for (int j = 0; j < A.size(); j++) {
			if (mappings.count(A[j]) == 0 && !isspace(A[j])) {
				mappings[A[j]] = B[j];
				done.insert(B[j]);
			}
		}
	}
	vector<char> AM;
	vector<char> BM;
	for (int i = 0; i < 26; i++) {
		if (mappings.count('a'+i) == 0) {
			AM.push_back('a'+i);
		}
		if (done.count('a'+i) == 0) {
			BM.push_back('a'+i);
		}
	}
	mappings[AM[0]] = BM[1];
	mappings[AM[1]] = BM[0];
	int line;
	cin >> line;
	string str;
	getline(cin,str);
	for (int l = 0; l < line; l++) {
		getline(cin,str);
		// process
		ostringstream oss;
		for (int i = 0; i < str.size(); i++) {
			if (isspace(str[i])) oss << " ";
			else oss << mappings[str[i]];
		}
		cout << "Case #" << (l+1) << ": " << oss.str() << "\n";
	}
	return 0;
}