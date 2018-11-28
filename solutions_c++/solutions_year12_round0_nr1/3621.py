#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

char f[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	int T; char c;
	scanf("%d", &T); getchar();
	for(int t=1; t<=T; t++)
	{
		printf("Case #%d: ", t);
		c = getchar();
		while(c != '\n' /*&& c != EOF*/)
		{
			if(c == ' ')
				printf(" ");
			else
				printf("%c", f[c-'a']);
			c = getchar();
		}
		printf("\n");
	}
	return 0;
}
