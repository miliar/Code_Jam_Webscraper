#include <cstdio>

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	unsigned numberOfTests;
	char googlereseString[128];
	char characterMapping[] = "yhesocvxduiglbkrztnwjpfmaq";
	scanf("%d", &numberOfTests);
	for (unsigned test = 0; test <= numberOfTests; ++test)
	{
		gets(googlereseString);
		if (!test)
		{
			continue;
		}
		for (unsigned character = 0; googlereseString[character]; ++character)
		{
			if ('a' <= googlereseString[character] && googlereseString[character] <= 'z')
			{
				googlereseString[character] = characterMapping[googlereseString[character] - 'a'];
			}
		}
		printf("Case #%u: %s\n", test, googlereseString);
	}
	return 0;
}
