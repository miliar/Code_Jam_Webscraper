#include <iostream>
#include <fstream>
#include <stddef.h>
#include <stdlib.h>
#include <string>

char charmap [256];
char invcharmap [256];

void map (char plain, char cipher)
{
	charmap [plain] = cipher;
	invcharmap [cipher] = plain;
}

void build (const char *plain, const char *cipher)
{
	if (strlen (plain) != strlen (cipher)) { std::cout << "fail" << std::endl; return; }
	int i = 0;
	for (int i = 0; plain [i]; i++)
	{
		map (plain [i], cipher [i]);
	}
}

void decode (const char *cipher, char *plain)
{
	int len = strlen (cipher);
	for (int i = 0; i < len; i++)
	{
		if (invcharmap [cipher [i]])
		{
			plain [i] = invcharmap [cipher [i]];
		}
		else
		{
			plain [i] = cipher [i];
		}
	}
	plain [len] = cipher [len];
}

int main ()
{
	for (int i = 0; i < 256; i++) { invcharmap [i] = '\0'; }
	build ("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi");
	build ("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	build ("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv");
	map ('z', 'q');
	map ('q', 'z');
	
	std::ifstream in ("a.in");
	std::ofstream out ("a.out");
	char buf [256];
	in.getline (buf, 256);
	unsigned int lines = atoi (buf);
	for (unsigned int i = 0; i < lines; i++)
	{
		in.getline (buf, 256);

		char *plain = new char [strlen (buf) + 1];

		decode (buf, plain);
		out << "Case #" << (i + 1) << ": " << plain << std::endl;

		delete [] plain;
		plain = NULL;
	}
	return 0;
}

