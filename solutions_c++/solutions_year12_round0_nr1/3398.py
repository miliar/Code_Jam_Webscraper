#include <iostream>
#include <cstdio>

char code[]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

char decode(char x) {
	if (x>='a' && x<='z')
		return code[x-'a'];
	return x;
}

int main() {
	int n;

	char buff[1000];

	std::cin >> n;
	std::cin.ignore();

	for (int i = 0; i < n; ++i) {
		std::cin.getline(buff,1000);

		for (int j = 0; buff[j]; ++j) {
			buff[j] = decode(buff[j]);
		}
		printf("Case #%d: %s",i+1, buff);
		if (i != n-1)
			putchar('\n');
	}

	return 0;

}
