#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream in("this.in");
ofstream out("out");

bool MatchExists(int wordLen, int pattern, int word, string* words, string* patterns) {
	for(int i=0; i<wordLen; i++) {
		if (patterns[pattern][0] == '(') {
			int j = 1;
			while (patterns[pattern][j] != ')'){
				if (patterns[pattern][j] == words[word][i]) break;
				j++;
			}
			if (patterns[pattern][j] == ')') return false;
			int pos = patterns[pattern].find(")");
		    patterns[pattern] = patterns[pattern].substr(pos + 1);
		} else {
			if (patterns[pattern][0] != words[word][i]) return false;
			patterns[pattern] = patterns[pattern].substr(1);
		}
	}
	return true;
}

int main (int argc, char * const argv[]) {
	int wordLen, numWords, numPatterns;
	
	in >> wordLen;
	in >> numWords;
	in >> numPatterns;
	string words[numWords];
	string patterns[numPatterns];


	for (int i=0; i<numWords; i++) {
		in >> words[i];
	}
	
	for (int i=0; i<numPatterns; i++) {
		in >> patterns[i];
	}
	
	for (int i = 0; i < numPatterns; i++){
		int numWordsMatched = 0;
		for(int j = 0; j < numWords; j++){
				string temp = patterns[i];
				if(MatchExists(wordLen, i, j, words, patterns)) numWordsMatched++;
				patterns[i] = temp;
		}
		out << "Case #" << i + 1 << ": " << numWordsMatched << endl;
	}
    return 0;
}