#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
typedef unsigned int uint;
void print_vec(vector<char> &elementlist) {
	if (elementlist.size() == 0) {
		printf("[]\n");
		return;
	}
	printf("[");
	for (uint i = 0; i < elementlist.size()-1; i++) {
		printf("%c, ",elementlist[i]);
	}
	printf("%c]\n",elementlist[elementlist.size()-1]);
}
int main() {
	int tc;
	scanf("%d", &tc);
	for (int testc = 0; testc < tc; testc++) {
		int c,d;
		char cstr[3];
		char dstr[2];
		map<pair<char, char>, char> combines;
		map<char, char> opposed;
		scanf("%d", &c);
		for (int i = 0; i < c; i++) {
			scanf("%s", cstr);
			combines[make_pair(cstr[0],cstr[1])] = cstr[2];
			combines[make_pair(cstr[1],cstr[0])] = cstr[2];
		}
		scanf("%d", &d);
		for (int i = 0; i < d; i++) {
			scanf("%s", dstr);
			opposed[dstr[0]]=dstr[1];
			opposed[dstr[1]]=dstr[0];
		}
		int n;
		scanf("%d", &n);
		char str[n];
		scanf("%s", str);
		vector<char> elementlist;
		for (int i = 0; i < n; i++) {
			char ch = str[i];
			if (elementlist.size() == 0) elementlist.push_back(ch);
			else {
				int comb=0;
				char top = elementlist[elementlist.size()-1];
				if (combines.count(make_pair(ch,top))) {
					elementlist[elementlist.size()-1] = combines[make_pair(ch,top)];
					ch = combines[make_pair(ch,top)];
					comb=1;
				}
				top = elementlist[elementlist.size()-1];
				int matched=0;

				if (opposed.count(ch)) {
					for (int j = 0; j < elementlist.size(); j++) {
						if (elementlist[j] == opposed[ch]) {
							elementlist.clear();
							matched=1;
							break;
						}
					}
					if (!matched && !comb) elementlist.push_back(ch);
				} else {
					if (!comb)
						elementlist.push_back(ch);
				}
			
			}
		}
		printf("Case #%d: ",testc+1);
		print_vec(elementlist);
	}
	return 0;
}
