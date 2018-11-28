#include <cstdio>
#include <cstdlib>
#include <cstring>

char mapping[] = "yhesocvxduiglbkrztnwjpfmaq";
char sLine[1024];

int main(int argc, char* argv[])
{
	int T;
	
	fgets(sLine, 1024, stdin);
	sscanf(sLine, "%d", &T);

	for (int tc = 1; tc <= T; ++tc)
	{
		fgets(sLine, 1024, stdin);
		for (int i = 0; i < strlen(sLine); ++i)
		{
			if (sLine[i] >= 'a' && sLine[i] <= 'z')
				sLine[i] = mapping[sLine[i] - 'a'];
		}

		printf("Case #%d: %s", tc, sLine);
	}

	return 0;
}
