#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

struct combine {
	char c1, c2, result;
};

struct oppose {
	char c1, c2;
};

int canCombine (vector<struct combine> cL, char c1, char c2, char *result) {
	vector<struct combine>::iterator it;
	for (it = cL.begin(); it < cL.end(); it++) {
		struct combine temp = *it;

		if ((temp.c1 == c1 && temp.c2 == c2) ||
			(temp.c2 == c1 && temp.c1 == c2)) {
			*result = temp.result;
			return 1;
		}
	}
	return 0;
}

int isOpposedHelper (vector<struct oppose> oL, char c1, char c2) {
	vector<struct oppose>::iterator it;
	for (it = oL.begin(); it < oL.end(); it++) {
		struct oppose temp = *it;

		if ((temp.c1 == c1 && temp.c2 == c2) ||
			(temp.c2 == c1 && temp.c1 == c2)) {
			return 1;
		}
	}
	return 0;
}

int isOpposed (vector<char> l, vector<struct oppose> oL, char c) {
	vector<char>::iterator it;
	for (it = l.begin(); it < l.end(); it++) {
		if (isOpposedHelper (oL, c, *it)) {
			return 1;
		}
	}
	return 0;
}

void printList (vector<char> l) {
	vector<char>::iterator it;
	printf ("[");
	int first = 1;
	for (it = l.begin(); it < l.end(); it++) {
		if (first) {
			printf ("%c", *it);
			first = 0;
		} else {
			printf (", %c", *it);
		}
	}
	printf ("]\n");
}

int main () {
	int nCases, iCase = 0;
	cin >> nCases;

	while (iCase < nCases) {
		vector<struct combine> combineList;
		vector<struct oppose> opposeList;
		vector<char> finalList;

		int nComb;
		cin >> nComb;
		for (int i = 0; i < nComb; i++) {
			char c1, c2, result;
			cin >> c1 >> c2 >> result;
			struct combine temp;

			temp.c1 = c1;
			temp.c2 = c2;
			temp.result = result;
			combineList.push_back (temp);
		}

		int nOpp;
		cin >> nOpp;
		for (int i = 0; i < nOpp; i++) {
			char c1, c2;
			cin >> c1 >> c2;
			struct oppose temp;

			temp.c1 = c1;
			temp.c2 = c2;
			opposeList.push_back (temp);
		}

		int nChar;
		cin >> nChar;

		char c1;
		cin >> c1;

		for (int i = 1; i < nChar; i++) {
			char c2;
			cin >> c2;
			
			if (isOpposed (finalList, opposeList, c1)) {
				finalList.clear();
				c1 = c2;
				continue;
			}

			char result;

			if (canCombine (combineList, c1, c2, &result)) {
				finalList.push_back (result);

				i++;
				if (i >= nChar) {
					c1 = '\0';
					break;
				}
				cin >> c1;
			} else {
				finalList.push_back (c1);
				c1 = c2;
			}
		}
		if (c1 != '\0') {
			if (isOpposed (finalList, opposeList, c1)) {
				finalList.clear();
			} else {
				finalList.push_back (c1);
			}
		}
		
		printf ("Case #%d: ", ++iCase);
		printList (finalList);
	}

	return 0;
}
