#include <stdio.h>

int main()
{
	char convert_table[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	char ch[30][101];
	int T = 0;

	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);


	scanf( "%d", &T );
	//fflush(stdin);
	getchar();

	for(int i = 0; i < T; i++)
		gets(ch[i]);


	for(int i = 0; i < T; i++)
	{
		char *p = ch[i];
		while(*p != '\0')
		{
			if(*p == ' ')
			{
				p++;
				continue;
			}
			*p = convert_table[*p - 'a'];
			p++;
		}
	}

	for(int i = 0; i < T; i++)
		printf("Case #%d: %s\n", i+1, ch[i]);
		
	return 0;
}