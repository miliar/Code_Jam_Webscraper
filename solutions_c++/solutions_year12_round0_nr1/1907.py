#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

static char translate(char c)
{
	// English to Googlerese
	// abcdefghijklmnopqrstuvwxyz
	// ynficwlbkuomxsevzpdrjgthaq

	// Googlerese to English
	// abcdefghijklmnopqrstuvwxyz
	// yhesocvxduiglbkrztnwjpfmaq

	return 'a' <= c && c <= 'z'
		? "yhesocvxduiglbkrztnwjpfmaq"[c - 'a']
		: c;
}

int main()
{
	unsigned n;
	cin >> n >> std::ws;
	assert(cin);
	for (unsigned i = 0; i < n; i++) {
		string s;
		getline(cin, s);
		assert(cin);
		assert(!s.empty());
		transform(s.begin(), s.end(), s.begin(), translate);
		cout << "Case #" << i + 1 << ": " << s << '\n';
	}
	return 0;
}
