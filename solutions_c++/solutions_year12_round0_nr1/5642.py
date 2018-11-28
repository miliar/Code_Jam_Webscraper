#include<sstream>
#include <iostream>
#include <string>
#include <map>

using namespace std;

std::map<char, char> string_mapping;

char base[] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi" 
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" 
	"de kr kd eoya kw aej tysr re ujdr lkgc jv" 
};
char target[] = {
	"our language is impossible to understand" 
	"there are twenty six factorial possibilities" 
	"so it is okay if you want to just give up" 
};

int main()
{
	for (int loop = 0 ; loop < sizeof(base) - 1 ; ++loop) {
		int base_ch = base[loop];
		int target_ch = target[loop];
		string_mapping.insert(std::pair<char, char>(base_ch, target_ch));
	}

	//for (char ch = 'a' ; ch <= 'z' ; ++ch) {
	//	if (string_mapping.end() == string_mapping.find(ch)) {
	//		string_mapping.insert(std::pair<char, char>(ch, ch));
	//	}
	//}
	string_mapping.insert(std::pair<char, char>('q', 'z'));
	string_mapping.insert(std::pair<char, char>('z', 'q'));

	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.txt", "w", stdout);

	string linestring;

	int T;
	getline(cin, linestring);
	stringstream sT(linestring);
	sT >> T;

	for (int i = 0 ; i < T ; i++) {
		getline(cin, linestring);

		cout << "Case #" << i + 1 << ": ";
		for (unsigned int j = 0 ; j < linestring.size() ; ++j) {
			cout << string_mapping.find(linestring.at(j))->second;
		}
		cout << endl;
	}
}
