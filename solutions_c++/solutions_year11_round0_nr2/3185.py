#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include "stdio.h"

using namespace std;

map<string, char> combinations;
set<string> opposed;

bool check_string(string &str) {
	if(str.length() < 2) {
		return false;
	}

	string end = str.substr(str.length()-2, 2);

	sort(end.begin(), end.end());

	map<string, char>::iterator it2 = combinations.find(end);
	if(it2 != combinations.end()) {
		str = str.substr(0, str.length()-2);
		str += it2->second;
		return true;
	}

	string::iterator last = str.end();
	last--;
	for(string::iterator it3 = str.begin(); it3 != last; it3++) {
		string str2 = "";
		if(*it3 < *last) {
			str2 += *it3;
			str2 += *last;
		} else {
			str2 += *last;
			str2 += *it3;
		}

		if(opposed.find(str2) != opposed.end()) {
			//printf("Hittade '%s'.\n", str2);
			str = "";
			return true;
		}
	}

	return false;
}

int main() {
	freopen("magicka.in", "r", stdin);
	freopen("magicka.out", "w", stdout);

	int nr_cases;
	scanf("%d", &nr_cases);
	//printf("Cases: %d\n", nr_cases);

	for(int i=0; i<nr_cases; i++) {
		combinations.clear();
		opposed.clear();

		int nr_combinations;
		scanf("%d", &nr_combinations);
		//printf("Nr_combinations: %d\n", nr_combinations);

		for(int j=0; j<nr_combinations; j++) {
			char a, b, c;
			string str = "";
			scanf(" %c%c%c", &a, &b, &c);
			//printf("Char1:%c, char2:%c, char3:%c\n", a, b, c);
			if(a < b) {
				str += a;
				str += b;
			} else {
				str += b;
				str += a;
			}

			combinations.insert(pair<string, char>(str, c));
		}

		int nr_opposed;
		scanf("%d", &nr_opposed);

		for(int j=0; j<nr_opposed; j++) {
			char a, b;
			string str = "";
			scanf(" %c%c", &a, &b);
			if(a < b) {
				str += a;
				str += b;
			} else {
				str += b;
				str += a;
			}

			opposed.insert(str);
		}


		int n;
		scanf("%d", &n);

		string elements = "";

		for(int j=0; j<n; j++) {
			char ch;
			scanf("%c", &ch);
			if(ch == ' ') {
				j--;
				continue;
			}

			elements += ch;
			while(check_string(elements));
		}

		printf("Case #%d: [", i+1);
		for(string::iterator it = elements.begin(); it != elements.end(); it++) {
			if(it != elements.begin()) {
				printf(", ");
			}

			printf("%c", *it);
		}
		printf("]\n");
	}
}
