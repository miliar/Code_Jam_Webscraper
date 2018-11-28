#include <iostream>
#include <iomanip>
#include <string>

using namespace std;


int count_matches(string const& pattern, string const& text) {
	if (pattern.length() > text.length())	return	0;

	if (pattern.length() == text.length()) {
		if (pattern == text)	return	1;
		return	0;
	}

	int matches = 0;

	if (pattern.length() == 1) {
		for (int i = 0; i < text.length(); ++i) {
			if (text[i] == pattern[0]) ++matches;
		}
		return	matches;
	}

	string sub_pattern = pattern.substr(1);
	int head_count = 0;
	for (int i = 0; i < text.length(); ++i) {
		if (text[i] == pattern[0]) {
			++head_count;
		} else if (head_count != 0 && text[i] == pattern[1]) {
			int sub_matches = count_matches(sub_pattern, text.substr(i));
			matches = (matches + (head_count % 10000) * sub_matches) % 10000;
			head_count = 0;
		}
	}

	return matches;
}


int main()
{
	int N;
	cin >> N;
	string dummy;
	getline(cin, dummy);
	
	string message("welcome to code jam");
	
	for (int n = 1; n <= N; ++n) {
		string text;
		getline(cin, text);
		int match = count_matches(message, text) % 10000;
		cout << "Case #" << n << ": " << setw(4) << setfill('0') << match << endl;
	}
}
