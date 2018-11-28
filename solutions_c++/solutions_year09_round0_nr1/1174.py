#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>

using namespace std;

int numCases, numLetters, numWords;
set<string> dict;

int
recur(string input, int curPos, int curLetter, string curString)
{
	if (curLetter == numLetters) {
		if (dict.find(curString) == dict.end()) {
			return 0;
		} else {
			return 1;
		}
	}
	if (curLetter > 0) {
		bool poss = false;
		set<string>::iterator ende = dict.upper_bound(curString + "}");
		for (set<string>::iterator itAct = dict.lower_bound(curString);
		itAct != ende; itAct++) {
			if (itAct->substr(0, curLetter) == curString) {
				poss = true;
				break;
			}
		}
		if (!poss) {
			return false;
		}
	}

	if (input[curPos] == '(') {
		int ret = 0;
		curPos++;
		int newPos = curPos;
		while (input[newPos] != ')') {
			newPos++;
		}
		newPos++;

		while (input[curPos] != ')') {
			ret += recur(input, newPos, curLetter + 1, curString + input[curPos]);
			curPos++;
		}
		
		return ret;
	} else {
		curString += input[curPos];
		return recur(input, curPos + 1, curLetter + 1, curString);
	}
	
}

int
main(int argc, char **argv)
{
	scanf("%d%d%d", &numLetters, &numWords, &numCases);

	for (int i = 0; i < numWords; i++) {
		string tmp;
		cin >> tmp;
		dict.insert(tmp);
	}

	for (int i = 0; i < numCases; i++) {
		string input;
		cin >> input;

		int poss = recur(input, 0, 0, "");
		printf("Case #%d: %d\n", i + 1, poss);
	}

	return 0;
}
