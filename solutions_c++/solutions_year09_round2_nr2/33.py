#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

char input[1024];

int main()
{
	int kases;
	scanf("%d", &kases);
	for (int kase = 1; kase <= kases; kase++)
	{
		input[0] = '0';
		scanf("%s", input+1);
		next_permutation(input, input + strlen(input));
		printf("Case #%d: %s\n", kase, input + (input[0] == '0'));
	}
	return 0;
}
