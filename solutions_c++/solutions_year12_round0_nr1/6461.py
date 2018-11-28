#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char charmap[] =
{
//	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
	'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'
};

void freadln(FILE *f, char *buf, size_t bufsize)
{
	int pos = 0;
	while (pos < bufsize && buf[pos-1] != '\n' && !feof(f))
	{
		buf[pos++] = fgetc(f);
	}
	buf[pos-1] = 0;
	
}

void translatemap(char *str)
{
	int pos = 0, len = strlen(str);
	while (pos < len)
	{
		if ((str[pos] >= 65 && str[pos] <= 90 || str[pos] >= 97 && str[pos] <= 122))
		{
			bool isupper = str[pos] >= 65 && str[pos] <= 90;
			char lower = (isupper ? str[pos] + 32 : str[pos]);
			for (short i = 0; i < 26; i++) // quick + dirty for now
			{
				if (charmap[i] == lower)
				{
					str[pos] = (isupper ? i + 65 : i + 97);
					break;
				}
			}
		}
		pos++;
	}
}

int main(int argc, char **argv)
{
	// filename in argv[1]
	FILE *f = fopen(argv[1], "r");
	char *buf = (char*)malloc(100+1); // max length is 100
	// read first line = num lines
	freadln(f, buf, 100+1);
	int lncount = atoi(buf);
	for (int i = 1; i <= lncount; i++)
	{
		freadln(f, buf, 100+1);
		translatemap(buf);
		printf("Case #%d: %s\n", i, buf);
	}
}
