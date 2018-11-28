#include <iostream>
#include <stdio.h>
#include <string.h>

char master_dict[] = {
	'y',
	'h',
	'e',
	's',
	'o',
	'c',
	'v',
	'x',
	'd',
	'u',
	'i',
	'g',
	'l',
	'b',
	'k',
	'r',
	'z',
	't',
	'n',
	'w',
	'j',
	'p',
	'f',
	'm',
	'a',
	'q'
};


int main() {
	
	unsigned int T;
	std::cin >> T;
	getchar();
	
	unsigned int i;
	for (i = 0; i < T; i++) {
		char orig[101];
		char ans[101];
		memset(orig, 0, 101);
		memset(ans, 0, 101);
		std::cin.getline(orig, 101);

		int len = strlen(orig);
		unsigned int j;
		for (j = 0; j < len; j++) {
			char literal = orig[j];
			if (literal >= 'a' && literal <= 'z') {
				ans[j] = master_dict[literal-'a'];
			} else ans[j] = orig[j];
		}
		ans[len] = 0;
		std::cout << "Case #" << (i+1) << ": " << ans << std::endl;
	}
}
