#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int cn;
char m[] = "yhesocvxduiglbkrztnwjpfmaq";
char str[200];

int main() {
	int cases, len;
	scanf("%d\n",&cases);
	while (cases--) {
		gets(str);
		len = strlen(str);
		printf("Case #%d: ",++cn);
		for (int i=0; i < len; ++i) printf("%c", str[i] == ' ' ? ' ' : m[ str[i]-'a' ]);
		printf("\n");
	}
	return 0;
}
