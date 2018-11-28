#include <stdio.h>
#include <string.h>

char *encode[4] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv", "y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd"};

char *plaintext[4] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up", "a b c d e f g h i j k l m n o p q r s t u v y w x y z now i know my abcs"};

int main()
{
	char map[26];
	char flag[26];
	memset(flag, 0, 26);
	for (int i=0; i<4; i++)
	{
		char *s1 = encode[i];
		char *s2 = plaintext[i];

		int len = strnlen(s1, 150);
		for (int j=0; j<len; j++)
		{
			map[s1[j]-'a'] = s2[j]-'a';
			flag[s1[j]-'a'] = 1;
		}
	}

	int nCase = 0;
	char str[150];
	scanf("%d\n", &nCase);
	for (int i=0; i<nCase; i++)
	{
		gets(str);
		int len = strnlen(str, 150);
		for (int j=0; j<len; j++)
		{
			str[j] = map[str[j]-'a'] + 'a';
		}
		printf("Case #%d: %s\n", i+1, str);
	}
	return 0;
}

