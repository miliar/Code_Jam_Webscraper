#include <cstdio>

char m[26];
char c;
int t;

int main(){
	m[0] = 'y';
	m[1] = 'h';
	m[2] = 'e';
	m[3] = 's';
	m[4] = 'o';
	m[5] = 'c';
	m[6] = 'v';
	m[7] = 'x';
	m[8] = 'd';
	m[9] = 'u';
	m[10] = 'i';
	m[11] = 'g';
	m[12] = 'l';
	m[13] = 'b';
	m[14] = 'k';
	m[15] = 'r';
	m[16] = 'z';
	m[17] = 't';
	m[18] = 'n';
	m[19] = 'w';
	m[20] = 'j';
	m[21] = 'p';
	m[22] = 'f';
	m[23] = 'm';
	m[24] = 'a';
	m[25] = 'q';
	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d\n", &t);
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		while(1){
			scanf("%c", &c);
			if (c != ' ' && c != '\n'){
				c = m[c-'a'];
			}
			printf("%c", c);
			if (c == '\n') break;
		}
	}
	return 0;
}
