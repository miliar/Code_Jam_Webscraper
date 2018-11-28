// Q1

// MACROS
#define PRINT(X, K) cout << "Case #" << X << ": " << K << endl;
#define FOREACH(T, I, J) for (T::iterator I = J.begin(); I != J.end(); ++I)
#define FOREACH_CONST(T, I, J) for (T::const_iterator I = J.begin(); I != J.end(); ++I)

#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

typedef map<unsigned, string> Tokens;

class Dict {

public:
	bool valid;
	map<char, Dict> children;
	Dict();
	bool insert(string::const_iterator first, string::const_iterator last);
	bool find(string::const_iterator first, string::const_iterator last) const;
};

unsigned countPossible(Dict &dict, unsigned index, Tokens &token);

int main(void) {

	/**
	 * L = number of chars in a letter
	 * D = number of words in dictionary
	 * N = number of test cases
	 */
	Dict dict;
	unsigned L, D, N;

	cin >> L >> D >> N;

	string s;
	for (unsigned i = 0; i != D; ++i) {
		cin >> s;
		dict.insert(s.begin(), s.end());

	}


	for (unsigned i = 0; i != N; ++i) {
		cin >> s;

		stringstream  ss;
		bool split = true;
		FOREACH(string, it, s) {
			if (*it == '(') {
				split = false;
			} else if (*it == ')') {
				split = true;
				ss << ' ';
			} else {
				if (split)
					ss << *it << ' ';
				else
					ss << *it;
			}


		}

		// get tokens
		Tokens tokens;
		unsigned j = 0;
		while (ss >> s) {
			tokens[j] = s;
			++j;
		}

		PRINT(i+1, countPossible(dict, 0, tokens));

	}

	return 0;

}

/**
 * Dictionary
 */
Dict::Dict() :
	valid(false) {
}

bool Dict::insert(string::const_iterator first, string::const_iterator last) {

	// if first and last is the same then we return
	if (first == last) {

		// if a word hasn't exist
		if (!valid) {
			// mark true and return
			valid = true;
			return true;
		}

		// else return false (not a unique word)
		return false;

	}

	Dict &node = children[*first];

	// insert the rest of the string to the next node
	return node.insert(++first, last);

}

bool Dict::find(string::const_iterator first, string::const_iterator last) const {

	// if were at the end of string and word is valid
	if ((first == last) && valid) {
		return true;
	}

	map<char, Dict>::const_iterator next = children.find(*first);

	// if not we look at the next node
	if (next != children.end()) {
		return next->second.find(++first, last);
	}

	// if not found return false
	return false;

}

unsigned countPossible(Dict &dict, unsigned index, Tokens &token) {

	unsigned count(0);
	FOREACH(string, it, token[index]) {

		char c = *it;

		if (dict.children.find(c) != dict.children.end()) {

			if ((index + 1) != token.size()) {

				count += countPossible(dict.children[c], index+1, token);

			} else {
				++count;
			}
		}

	}

	return count;

}

