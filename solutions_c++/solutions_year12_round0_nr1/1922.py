#include <cstdlib>
#include <cstdio>

//char ALPHA[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
const char ALPHA[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
const int MAX_SIZE = 101;

int main() 
{
	// 'a' = 97
	// 'z' = 122
	int cases;
	char phrase[MAX_SIZE+5];
	scanf("%d%*d", &cases);
	
	for (int c = 1; c <= cases; c++)
	{
		fgets(phrase, sizeof(phrase), stdin);
		printf("Case #%d: ", c);
		for (char* w = phrase; *w; w++) 
		{
				if (*w == ' ') 
					printf(" ");
				else if (*w >= 'a' && *w <= 'z')
					printf("%c", ALPHA[*w - 'a']);
		}
		printf("\n");
	}
	return 0;
}

