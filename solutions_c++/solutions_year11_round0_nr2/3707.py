#include <stdio.h>
#include <vector>
#include <map>
#include <string>
using namespace std;

map<string, char> combine;
vector<int> opp[30];

int main() {
	int T;
	scanf("%d", &T);
	char str[120];
	for(int q=0;q<T;q++) {
		int c, d, n;
		scanf("%d", &c);
		
		for(int i=0;i<30;i++)
			opp[i].clear();
		combine.clear();
		string a = "";
		for(int i=0;i<c;i++) {
			scanf("%s", str);
			a += str[0];
			a += str[1];
			combine.insert(pair<string, char>(a, str[2]));
			a = "";
			a += str[1];
			a += str[0];
			combine.insert(pair<string, char>(a, str[2]));
		}
		scanf("%d", &d);
		for(int i=0;i<d;i++) {
			scanf("%s", str);
			int aa = str[0] - 'A';
			int bb = str[1] - 'A';
			opp[aa].push_back(bb);
			opp[bb].push_back(aa);
		}		
		scanf("%d", &n);
		scanf("%s", str);
		string s = str;
		string t;
		
		string element = "";
		map<string, char>:: iterator it;
		for(int i=0;i<s.size();i++) {
			if(element.size() == 0) {
				element += s[i];
				continue;
			}
			t = "";
			t += element[element.size()-1];
			t += s[i];
			it = combine.find(t);
			if(it != combine.end()) {
				element[element.size()-1] = combine[t];
			} else {
				int at = s[i] - 'A';
				bool flag = false;
				for(int j=0;j<element.size();j++) {
					for(int k=0;k<opp[at].size();k++) {
						if(opp[at][k] == element[j]-'A') {
							flag = true;
							break;
						}
					}
					if(flag) break;
				}
				if(flag) {
					element = "";
				} else {
					element += s[i];
				}
			}
		}
		printf("Case #%d: [", q+1);
		for(int i=0;i<element.size();i++) {
			if(i!=0)
				printf(", ");
			printf("%c", element[i]);
		}
		printf("]\n");

	}
	return 0;
}
