#include <stdio.h>

char t[26]=
	{
		'y', // a
		'h', // b
		'e', // c
		's', // d
		'o', // e
		'c', // f
		'v', // g
		'x', // h
		'd', // i
		'u', // j
		'i', // k
		'g', // l
		'l', // m
		'b', // n
		'k', // o
		'r', // p
		'z', // q
		't', // r
		'n', // s
		'w', // t
		'j', // u
		'p', // v
		'f', // w
		'm', // x
		'a', // y
		'q', // z
	};

int cases;
char s[256];

int main()
{
	gets(s); sscanf(s, "%d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		gets(s);
		printf("Case #%d: ", cs);
		for(int i=0; s[i]>=' '; i++)
			if (s[i]==' ') putchar(' ');
			else putchar(t[int(s[i]-'a')]);
		printf("\n");
	}
	return 0;
}
