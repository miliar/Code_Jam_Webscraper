#include <cstdio>
#include <cstring>

int onto[26] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};

int T, cases = 1;
char str[101];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	gets(str);
	while(cases <= T){
		gets(str);

		int len = strlen(str);
		for(int i=0; i<len; ++i){
			if(str[i] != ' ')
				str[i] = onto[str[i] - 'a'] + 'a';
		}

		printf("Case #%d: %s\n", cases, str);
		cases ++;
	}
}