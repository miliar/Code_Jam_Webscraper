#include <cstdio>
#include <cstring>
char con(char c) { //{{{
	if(c == 'a') return 'y';
	if(c == 'b') return 'h';
	if(c == 'c') return 'e';
	if(c == 'd') return 's';
	if(c == 'e') return 'o';
	if(c == 'f') return 'c';
	if(c == 'g') return 'v';
	if(c == 'h') return 'x';
	if(c == 'i') return 'd';
	if(c == 'j') return 'u';
	if(c == 'k') return 'i';
	if(c == 'l') return 'g';
	if(c == 'm') return 'l';
	if(c == 'n') return 'b';
	if(c == 'o') return 'k';
	if(c == 'p') return 'r';
	if(c == 'q') return 'z';
	if(c == 'r') return 't';
	if(c == 's') return 'n';
	if(c == 't') return 'w';
	if(c == 'u') return 'j';
	if(c == 'v') return 'p';
	if(c == 'w') return 'f';
	if(c == 'x') return 'm';
	if(c == 'y') return 'a';
	if(c == 'z') return 'q';
	return c;
} //}}}
void work() {
	char s[110];
	memset(s,0,sizeof(s));
	fgets(s,sizeof(s),stdin);
	int len = strlen(s);
	for(int i = 0;i < len;i++)
		printf("%c",con(s[i]));
}
void line() {
	char s[110];
	memset(s,0,sizeof(s));
	fgets(s,sizeof(s),stdin);
}
int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	scanf("%d",&T);
	line();
	for(int i = 1;i <= T;i ++) {
		printf("Case #%d: ",i);
		work();
	}
}
