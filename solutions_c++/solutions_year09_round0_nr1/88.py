#include <string.h>
#include <stdio.h>
char Dic[5000][16];
char pattern[500];
int L, D, N;
bool match(char *src, char *pattern)
{
	int loc = 0;
	while (*pattern)
	{
		if (*pattern == '(') {
			pattern++;
			char temp[26];
			int size = 0;
			while (*pattern != ')') {
				temp[size++] = *pattern++;
			}
			pattern++;
			bool found = false;
			for (int i = 0; i < size; i++)
				if (src[loc] == temp[i]) found = true;
			if (found) loc++;
			else break;
		}
		else {
			if (*pattern == src[loc]) { 
				loc++;
				pattern++;
			}
			else break;
		}
	}
	return loc == L;
}
int main()
{
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i < D; i++)
		scanf("%s", Dic + i);
	for (int i = 1; i <= N; i++)
	{
		scanf("%s", pattern);
		int count = 0;
		for (int j = 0; j < D; j++)
			if (match(Dic[j], pattern)) count++;
		printf("Case #%d: %d\n", i, count);
	}
}