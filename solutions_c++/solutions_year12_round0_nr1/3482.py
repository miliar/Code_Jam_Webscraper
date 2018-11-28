#include <cstdio>
using namespace std;

//FILE *fin = freopen("A-small-attempt0.in", "r", stdin);
//FILE *fout = freopen("A.out", "w", stdout);

char cvt[] = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	int ncases;

	scanf("%d ", &ncases);
	for (int cases = 1; cases <= ncases; cases++) {
		char str[255];
		gets(str);
		printf("Case #%d: ", cases);
		for (int i = 0; str[i] != '\0'; i++) {
			if ('a' <= str[i] && str[i] <= 'z')
				printf("%c", cvt[str[i] - 'a']);
			else
				printf("%c", str[i]);
		}
		printf("\n");
	}
	return 0;
}