#include <iostream>

using namespace std;

char cheat[26] = {'y', 'h', 'e', 's', 'o',
 					'c', 'v', 'x', 'd', 'u',
 					'i', 'g', 'l', 'b', 'k',
 					'r', 'z', 't', 'n', 'w',
 					'j', 'p', 'f', 'm', 'a',
 					'q'
};

char buf[101];

int main() {
	gets(buf);
	int cases = 0;
	int T = atoi(buf);
	while(T--) {
		cases++;
		gets(buf);
		for(int i=0; i < strlen(buf); i++) {
			if(buf[i] != ' ') 
				buf[i] = cheat[buf[i] - 'a'];
		}
		printf("Case #%d: %s\n", cases, buf);
	}
	return 0;
}