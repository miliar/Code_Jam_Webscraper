#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 102;

int T, l;
char ins[N];
char turn[28]="yhesocvxduiglbkrztnwjpfmaq";

int main() {
	freopen("input.txt", "r", stdin);	freopen("output.txt", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 1; i <= T; i++) {
		gets(ins);
		l = strlen(ins);
		printf("Case #%d: ", i);
		for (int j = 0; j < l; j++)
			putchar(ins[j] == ' ' ? ins[j] : turn[ins[j] - 'a']);
		puts("");
	}
	fclose(stdin);	fclose(stdout);	return 0;
}
