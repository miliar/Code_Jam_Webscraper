
#include <cstdlib>
#include <cstring>
#include <vector>
#include <iostream>
using namespace std;

int L, D, N;

class Token {
public:
	char *letters;

public:
	Token(char *s) {
		letters = s;
	}

	Token(char c) {
		letters = new char[2];
		letters[0] = c;
		letters[1] = 0;
	}

	bool matches(const Token& token) {
		return strpbrk(letters, token.letters) != 0;
	}
};

class Word {
public:
	vector<Token> tokens;

public:
	bool matches(const Word& word) {
		for (unsigned i = 0; i < tokens.size(); i++) {
			if (!tokens[i].matches(word.tokens[i])) {
				return false;
			}
		}
		return true;
	}

	void addToken(const Token& token) {
		tokens.push_back(token);
	}

};

ostream& operator<<(ostream& ost, const Word& word) {
	for (unsigned i = 0; i < word.tokens.size(); i++) {
		ost << word.tokens[i].letters << ":";
	}
	return ost;
}

Word
parseline(char *line)
{
	char letters[L];
	Word w;

	char *p = line;
	while (*p) {
		while (isspace(*p)) {
			p++;
		}
		if (*p != '(') {
			w.addToken(Token(*p++));
		}
		if (*p == '(') {
			char *s = letters;
			p++;
			while (*p && !isspace(*p) && *p != ')') {
				*s++ = *p++;
			}
			*s = 0;
			p++;
			w.addToken(Token(strdup(letters)));
		}
	}
	return w;
}

vector<Word> dictionary;

int
main()
{
	cin >> L >> D >> N;
	const int maxlinelen = 26 * L;

	char *line = new char[maxlinelen];
	cin.getline(line, maxlinelen);

	for (int i = 0; i < D; i++) {
		cin.getline(line, maxlinelen);
		Word w = parseline(line);
		dictionary.push_back(w);
	}
	for (int i = 0; i < N; i++) {
		cin.getline(line, maxlinelen);
		Word w = parseline(line);
		int nmatches = 0;
		for (vector<Word>::iterator it = dictionary.begin(); it != dictionary.end(); ++it) {
			if (it->matches(w)) {
				nmatches++;
			}
		}
		cout << "Case #" << (i + 1) << ": " << nmatches << endl;
	}

//	delete[] line;
}
