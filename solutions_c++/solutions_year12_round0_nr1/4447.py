#include <iostream>
#include <iomanip>
using namespace std;
char const map[26] = {
	'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 
	'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
};

int main()
{
	freopen("/1/1.in", "r", stdin);
	freopen("/1/1.out", "w", stdout);
	int T;
	char ch;
	scanf("%d\n", &T);
	for (int T1 = 1; T1 <= T; ++T1) {
		printf("Case #%d: ", T1);
		while (scanf("%c", &ch), ch!='\n'&&ch!='\0') {
			if (ch>='a' && ch<='z') printf("%c", map[ch-'a']);
			else printf("%c", ch);
		}
		printf("\n");
	}
}
