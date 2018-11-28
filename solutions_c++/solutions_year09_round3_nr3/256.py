#include <stdio.h>
#include <vector>
#include <queue>
#include <set>
#include <string.h>
#include <string>

using namespace std;
bool released[100000];
int numPris, numRel;

set<int> toRel;
//map<int, int> known;

int
select(int pris) {
	int ret = 0;
	for (int i = pris - 1; i >= 0 && !released[i]; ret++, i--) {
	}
	for (int i = pris + 1; i < numPris && !released[i]; ret++, i++) {
	}
	return ret;
}

int
rec(set<int> toRel)
{
	if (toRel.empty()) {
		return 0;
	}

	int ret = numPris * numPris;
	for (set<int>::iterator itAct = toRel.begin(); itAct != toRel.end(); itAct++) {
		int cur = select(*itAct);
		released[*itAct] = true;
		set<int> neu = toRel;
		neu.erase(*itAct);
		cur += rec(neu);
		released[*itAct] = false;
		if (cur < ret) {
			ret = cur;
		}
	}
	return ret;
}

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int i = 0; i < numCases; i++) {
		scanf("%d%d", &numPris, &numRel);

		toRel.clear();
		for (int j = 0; j < numPris; j++) {
			released[j] = false;
		}

		for (int j = 0; j < numRel; j++) {
			int tmp;
			scanf("%d", &tmp);
			toRel.insert(tmp - 1);
		}

		printf("Case #%d: %d\n", i + 1, rec(toRel));
	}

	return 0;
}
