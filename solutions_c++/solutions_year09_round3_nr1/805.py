#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
	int i;
	int cases = 0;
	char line[100];
	int symbols[256];
	long long count;
	int nsymbols;
	char* p;
	long long number;
	int acase = 1;

	scanf("%d\n", &cases);
	while(cases--)
	{
		strcpy(line, "");
		fgets(line, 100, stdin);
		p = line;
		while((*p != '\r') && (*p != '\n') && (*p != '\0'))
			++p;
		*p = 0;
		for(i = 0;i < 256;++i)
			symbols[i] = -1;
		count = 0;
		for(i = 0;line[i];++i)
		{
			if(symbols[line[i]] == -1)
			{
				++count;
				symbols[line[i]] = 1;
			}
		}
		if(count == 1)
			++count;
		for(i = 0;line[i];++i)
			symbols[line[i]] = -1;
		symbols[line[0]] = 1;
		nsymbols = 0;
		for(i = 0;line[i];++i)
		{
			if(symbols[line[i]] == -1)
			{
				if(nsymbols == 1)
					++nsymbols;
				symbols[line[i]] = nsymbols;
				++nsymbols;
			}
		}
		number = 0;
		for(i = 0;line[i];++i)
		{
			number *= count;
			number += (long long)symbols[line[i]];
		}
		printf("Case #%d: %lld\n", acase++, number);
	}
	return 0;
}
