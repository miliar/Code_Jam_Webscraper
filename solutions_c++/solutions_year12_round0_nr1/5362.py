#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

char sz[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T, index;
	scanf("%d", &T);
	cin.ignore();
	char input[105];
	for (index = 1; index <= T; ++index) {
		gets(input);
		int len = strlen(input), i;
		string ans = "";
		for (i = 0; i < len; ++i) {
			if (isalpha(input[i])) {
				ans += sz[(int)(input[i] - 'a')];
			}
			else if (input[i] == ' ') {
				ans += " ";
			}
		}
		printf("Case #%d: ", index);
		cout << ans << endl;
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}
