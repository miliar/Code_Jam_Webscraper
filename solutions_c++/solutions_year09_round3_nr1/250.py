#include <stdio.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <string>

using namespace std;

set<char> chars;
map<char, long long int> symToDig;
char buffer[1000];

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 0; c < numCases; c++) {
		scanf("%s", buffer);
		chars.clear();
		for (int i = 0; i < strlen(buffer); i++) {
			chars.insert(buffer[i]);
		}
		long long int base = chars.size();
		if (base <= 1) {
			base = 2;
		}
		symToDig.clear();
		symToDig[buffer[0]] = 1;
		for (int i = 1; i < strlen(buffer); i++) {
			if (symToDig.find(buffer[i]) == symToDig.end()) {
				symToDig[buffer[i]] = 0;
				break;
			}
		}
		long long int next = 2;
		for (int i = 1; i < strlen(buffer); i++) {
			if (symToDig.find(buffer[i]) == symToDig.end()) {
				symToDig[buffer[i]] = next;
				next++;
			}
		}
		long long int counter = 1;
		long long int total = 0;
		for (int i = strlen(buffer) - 1; i >= 0; i--) {
			total += (counter * symToDig[buffer[i]]);
			counter *= base;
			
		}

		printf("Case #%d: %lld\n", c + 1, total);
	}

	return 0;
}
