#include <iostream>
using namespace std;

unsigned long long int convert(char number[]) {
	int base = 0;
	int characters[26], nums[10];
	for (int i = 0; i < 26; ++i) characters[i] = -1;
	for (int i = 0; i < 10; ++i) nums[i] = -1;
	
	for (int i = 0; number[i] != '\0'; ++i) {
		char c;
		if (isdigit((c = number[i]))) {
			if (nums[c - '0'] == -1) {
				if (base == 0) nums[c - '0'] = ++base;
				else if (base == 1) { nums[c - '0'] = 0; ++base; }
				else nums[c - '0'] = base++;
			}
		}
		else {
			if (characters[c - 'a'] == -1) {
				if (base == 0) characters[c - 'a'] = ++base;
				else if (base == 1) { characters[c - 'a'] = 0; ++base; }
				else characters[c - 'a'] = base++;
			}
		}
	}

    if (base == 1) base = 2;

	unsigned long long int res = 0;
	for (int i = 0; number[i] != '\0'; ++i) {
		char c;
		if (isdigit((c = number[i])))
			res = res*base + nums[c - '0'];
		else
			res = res*base + characters[c - 'a'];
	}
	
	return res;
}

int main() {
	int T, cases = 0;
	scanf("%d", &T);
	char number[62];
    cin.ignore();
	while (T--) {
		scanf("%s", number);
		unsigned long long int res = convert(number);
		printf("Case #%d: %lld\n", ++cases, res);
	}
}
