#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>


#define clr(a) memset(a, 0, sizeof(a))

typedef std::pair<int, int> pii;
typedef long long ll;

void dbg(const char * fmt, ...)
{
	#if 1
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
		fflush(stdout);
	#endif
}

char in[500];
char perm[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	int n;
	scanf("%d", &n);
	gets(in);
	for(int t = 0; t < n; t++)
	{
		printf("Case #%d: ", t + 1);
		gets(in);
		for(int i = 0; in[i]; i++)
			if (in[i] >= 'a' && in[i] <= 'z')
				in[i] = perm[in[i] - 'a'];
		printf("%s\n", in);
	}


	return 0;
}
