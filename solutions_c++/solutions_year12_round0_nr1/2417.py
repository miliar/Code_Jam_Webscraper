#include <cstdio>
#include <cstring>
using namespace std;

const char translation[] = {
	'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
	'j', 'p', 'f', 'm', 'a', 'q' };
char s[115];
int i, j, n, m;
	
int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d\n", &n);
	
	for(i = 0; i < n; i++) {
		memset(s, 0, sizeof(s));
		fgets(s, sizeof(s), stdin);
		
		printf("Case #%d: ", i + 1);
		
		m = strlen(s);
		if(s[m - 1] == '\n') m--;
		
		for(j = 0; j < m; j++)
			if(s[j] == ' ') printf(" ");
			else printf("%c", translation[s[j] - 'a']);
		printf("\n");
	}
	
	return 0;
}
