#include <cstdio>
#include <map>
#include <set>
#include <utility>
#include <vector>
using namespace std;

int n;
map < pair <char, char>, char > becomeMap;
set < pair <char, char> > removeSet;
vector <char> lst;

bool replace() {
	if ((int)lst.size() <= 1) {
		return false;
	}
	if ((int)lst.size() >= 2 && becomeMap.find(make_pair(lst[(int)lst.size() - 2], lst[(int)lst.size() - 1])) != becomeMap.end()) {
		char ch = becomeMap[make_pair(lst[(int)lst.size() - 2], lst[(int)lst.size() - 1])];
		lst[(int)lst.size() - 2] = ch;
		lst.pop_back();
		return true;
	}
	return false;
}

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		becomeMap.clear();
		removeSet.clear();
		lst.clear();
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char op[5];
			scanf("%s", op);
			becomeMap[make_pair(op[0], op[1])] = op[2];
			becomeMap[make_pair(op[1], op[0])] = op[2];
		}
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char op[5];
			scanf("%s", op);
			removeSet.insert(make_pair(op[0], op[1]));
			removeSet.insert(make_pair(op[1], op[0]));
		}
		char op[65536];
		scanf("%d%s", &n, op);
		for (int i = 0; i < n; i++) {
			lst.push_back(op[i]);
			if (!replace()) {
//				printf("i = %d\n", i);
				for (int j = 0; j < (int)lst.size(); j++) {
//					printf("(%c %c) = %d\n", lst[j], lst.back(), removeSet.find(make_pair(lst[j], lst.back())) != removeSet.end());
					if (removeSet.find(make_pair(lst[j], lst.back())) != removeSet.end()) {
//printf("i = %d\n", i);
						lst.clear();
						break;
					}
				}
			}
		}
		printf("Case #%d: [", oo + 1);
		for (int i = 0; i < (int)lst.size(); i++) {
			if (i) {
				putchar(',');
				putchar(' ');
			}
			printf("%c", lst[i]);
		}
		putchar(']');
		putchar('\n');
	}
	return 0;
}
