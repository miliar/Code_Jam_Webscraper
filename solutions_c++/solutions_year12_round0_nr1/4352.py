#include <cstdio>
#include <cctype>
#include <cstring>
using namespace std;

char str[1000];
char pos[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	int L, T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T); getchar();
	for (int i = 1; i <= T ; ++ i) {
		printf("Case #%d: ", i);
		gets(str);
		L = strlen(str);
		for(int j = 0; j < L; ++ j)
			if (islower(str[j]))
				putchar(pos[str[j] - 'a']);
			else putchar(' ');
		puts("");
	}
	return 0;
}
 
