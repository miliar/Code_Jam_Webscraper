#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

char fusion[128][128];

short oppose[128][128];
short TRUE;

vector<char> elements;
char str[128];

int main()
{
	int kase, serial=1,
		n, i, k,
		n_ele;
	bool stable;
	char ele;

	scanf("%d", &kase);
	while (kase--) {
		// begin test case

		++TRUE;
		memset(fusion, 0, sizeof(fusion));
		elements.clear();

		// read fusion
		scanf("%d", &n);
		for (i=0; i<n; ++i) {
			scanf("%s", str);
			fusion[str[0]][str[1]] = str[2];
			fusion[str[1]][str[0]] = str[2];
		}

		// read oppose
		scanf("%d", &n);
		for (i=0; i<n; ++i) {
			scanf("%s", str);
			oppose[str[0]][str[1]] = TRUE;
			oppose[str[1]][str[0]] = TRUE;
		}

		scanf("%d %s", &n, str);
		for (i=0; i<n; ++i) {
			ele = str[i];
			stable = true;

			if (! elements.empty()) {
				if (fusion[ele][elements.back()]) {
//					printf("Fusion occur %c + %c = %c\n", ele, elements.back(), fusion[ele][elements.back()]);
					ele = fusion[ele][elements.back()]; // combine
					elements.pop_back();
					elements.push_back(ele);
					stable = false;
				}
				else {
					for (k=0, n_ele=elements.size(); k<n_ele; ++k) {
						if (TRUE == oppose[ele][elements[k]]) {
//							printf("Conflict between %c and %c\n", ele, elements[k]);
							elements.clear();
							stable = false;
							break;
						}
					}
				}
			}

			if (stable) elements.push_back(ele);
		}

		printf("Case #%d: [", serial++);
		if (n_ele = elements.size()) {
			printf("%c", elements[0]);
			for (i=1; i<n_ele; ++i)
				printf(", %c", elements[i]);
		}
		puts("]");
		// end test case
	}
	return 0;
}
