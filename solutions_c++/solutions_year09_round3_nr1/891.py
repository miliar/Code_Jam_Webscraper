#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

/* revstr reverses a string */
void revstr(char *s)
{
	char *t = s;
	char temp;

	while (*t != '\0')
		++t;

	--t;
	while (t > s) {
		temp = *t;
		*t-- = *s;
		*s++ = temp;
	}
}

void arbitrarybaseconvert(char *number, char *source, char *target, char *answer)
{
	int bA, bB, i, j, k, decimal, pos, power;
	char *s;

	bA = 0;
	s = source;
	while (*s++ != '\0')
		++bA;

	bB = 0;
	s = target;
	while (*s++ != '\0')
		++bB;

	decimal = 0;
	for (i = (int)strlen(number)-1, j = 0; i >= 0; --i, ++j) {
		s = source;
		pos = 0;

		while (*s++ != number[i])
			++pos;
		
		power = 1;
		for (k = j; k > 0; --k)
			power *= bA;

		decimal += power * pos;
	}

	i = 0;
	while (decimal != 0) {
		answer[i] = target[decimal % bB];
		decimal = decimal / bB;
		++i;
	}
	answer[i] = '\0';

	// reverse the answer
	revstr(answer);
}


int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int T;
	cin >> T;
	cin.ignore();
	for (int i = 0; i < T; i++) {
		string s;
		getline(cin, s);
		vector<char> uni(s.begin(), s.end());
		sort(uni.begin(), uni.end());
		vector<char>::iterator it = unique(uni.begin(), uni.end());
		uni.erase(it, uni.end());
		int base = uni.size() > 1 ? uni.size() : 2;
		char a[65];
		memset(a, ' ', 65);
		a[1] = s[0];
		a[base] = '\0';
		for (int j = 1; j < s.size(); j++) {
			bool found = false;
			for (int k = 0; k < base; k++) {
				if (a[k] == s[j]) {
					found = true;
					break;
				}
			}
			if (found)
				continue;
			int k = 0;
			while (k < base && a[k] != ' ')
				k++;
			a[k] = s[j];
		}
		char number[65];
		number[s.size()] = '\0';
		copy(s.begin(), s.end(), &number[0]);
		char ans[65];
		arbitrarybaseconvert(number, a, "0123456789", ans);
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}