#include <cstdio>
#include <cstring>

using namespace std;

char str[150], trans[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	int n;
	scanf("%d\n", &n);
	for(int t=0;t<n;t++) {
		fgets(str, 150, stdin);
		for(int i=0;i<(int)strlen(str);i++) {
			if (str[i] != ' ' && str[i] != '\n')
				str[i] = trans[str[i]-'a'];
		}
		printf("Case #%d: %s", t+1, str);
	}

	return 0;
}