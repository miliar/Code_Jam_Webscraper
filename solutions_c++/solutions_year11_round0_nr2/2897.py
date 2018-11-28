#include <stdio.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int numChars[26];
vector<char> charList;

map<pair<char,char>, char> trafo;
map<char,char> dontLike;


char buffer[1024];

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 0; c < numCases; c++) {
		printf("Case #%d: [", c + 1);
		trafo.clear();
		dontLike.clear();
		for (int i = 0; i < 26; i++) {
			numChars[i] = 0;
		}
		charList.clear();

		int numSeq;
		scanf("%d", &numSeq);
		for (int i = 0; i < numSeq; i++) {
			scanf("%s", buffer);
			trafo[make_pair(buffer[0], buffer[1])] = buffer[2];
			trafo[make_pair(buffer[1], buffer[0])] = buffer[2];
		}

		scanf("%d", &numSeq);
		for (int i = 0; i < numSeq; i++) {
			scanf("%s", buffer);
			dontLike[buffer[0]] = buffer[1];
			dontLike[buffer[1]] = buffer[0];
		}

		scanf("%d", &numSeq);
		scanf("%s", buffer);
		for (int i = 0; i < numSeq; i++) {
			charList.push_back(buffer[i]);
			numChars[(int) (buffer[i] - 'A')]++;
			if (charList.size() >= 2) {
				if (trafo.find(make_pair(charList[charList.size() - 2],charList[charList.size() - 1])) != trafo.end()) {
					char newChar = trafo[make_pair(charList[charList.size() - 2],charList[charList.size() - 1])];
					numChars[(int) (charList[charList.size() - 2] - 'A')]--;
					numChars[(int) (charList[charList.size() - 1] - 'A')]--;
					numChars[(int) (newChar - 'A')]++;
					charList.pop_back();
					charList.pop_back();
					charList.push_back(newChar);
				} else if (dontLike.find(buffer[i]) != dontLike.end()) {
					char dl = dontLike[buffer[i]];
					if (numChars[(int) (dl - 'A')] > 0) {
						for (int i = 0; i < 26; i++) {
							numChars[i] = 0;
						}
						charList.clear();
					}
				}
			}
		}
		if (charList.size() >= 1) {
			printf("%c", charList[0]);
		}
		for (int i = 1; i < (signed) charList.size(); i++) {
			printf(", %c", charList[i]);
		}

		puts("]");
	}

	return 0;
}
