#include <stdio.h>
#include <set>
#include <string>

using namespace std;
set<string> searchEngines;
set<string> usedEngines;
char buffer[105];

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int kases = 0; kases < numCases; kases++) {
		int numSearchEngines, numQueries;
		searchEngines.clear();
		usedEngines.clear();

		scanf("%d", &numSearchEngines);
		fgets(buffer, sizeof(buffer), stdin);
		for (int i = 0; i < numSearchEngines; i++) {
			fgets(buffer, sizeof(buffer), stdin);
			string tmpString(buffer);
			searchEngines.insert(tmpString);
		}

		scanf("%d", &numQueries);
		fgets(buffer, sizeof(buffer), stdin);
		int total = 0;
		for (int i = 0; i < numQueries; i++) {
			fgets(buffer, sizeof(buffer), stdin);
			string tmpString(buffer);
			if (searchEngines.find(tmpString) == searchEngines.end()) {
				continue;
			}
			if (usedEngines.find(tmpString) == usedEngines.end()) {
				if (usedEngines.size() + 1 == (unsigned) numSearchEngines) {
					usedEngines.clear();
					total++;
				}
				usedEngines.insert(tmpString);
			}
		}

		printf("Case #%d: %d\n", (kases + 1), total);
	}

	return 0;
}
