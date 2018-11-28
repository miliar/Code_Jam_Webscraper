#include <cstdio>

char a[27];
int main() {
	int i;
	a[0] = 'y';
	a[1] = 'h';
	a[2] = 'e';
	a[3] = 's';
	a[4] = 'o';
	a[5] = 'c';
	a[6] = 'v';
	a[7] = 'x';
	a[8] = 'd';
	a[9] = 'u';
	a[10] = 'i';
	a[11] = 'g';
	a[12] = 'l';
	a[13] = 'b';
	a[14] = 'k';
	a[15] = 'r';
	a[16] = 'z';
	a[17] = 't';
	a[18] = 'n';
	a[19] = 'w';
	a[20] = 'j';
	a[21] = 'p';
	a[22] = 'f';
	a[23] = 'm';
	a[24] = 'a';
	a[25] = 'q';

	int t;
	char s[1009];
	char c;
	scanf("%d", &t);
	getchar();
	int tp=0;
	while(t--) {
		tp++;
		scanf("%[^\n]%c", s, &c);
		for(i=0; s[i]!='\0'; ++i) {
			if(s[i] >= 'a' && s[i] <= 'z') {
				s[i] = a[s[i]-'a'];
			}
		}

		printf("Case #%d: %s\n", tp, s);

	}
	return 0;

}
