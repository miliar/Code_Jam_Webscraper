#include <cstdio>
#include <cstring>

#include <vector>
#include <string>

int main()
{
	char words[5000][16];

	int wlen, wcount, cases; scanf("%d %d %d", &wlen, &wcount, &cases);
	for (int w = 0; w < wcount; ++w) scanf("%s", words[w]);
	
	char format[1000];
	for (int test = 1; test <= cases; ++test)
	{
		std::vector< std::string > dict(words, words + wcount);
		scanf("%s", format);
		
		char *p = format, *n = p, tbuf[32];
		for (int k = 0; k < wlen; ++k, p = ++n)
		{
			if (p[0] == '(')
			{ 
				n = strchr(p + 1, ')'); *n = 0;
				strcpy(tbuf, p + 1);
			}
			else sprintf(tbuf, "%c\0", *p);
			
			for (std::vector< std::string >::iterator i = dict.begin(); i != dict.end(); )
			if (strchr(tbuf, i->at(k)) == NULL) { dict.erase(i); } else ++i;
		};
		
		printf("Case #%d: %d\n", test, dict.size());
	};
};
