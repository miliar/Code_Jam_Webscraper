#include <stdio.h>
#include <stdarg.h>
#include <algorithm>
#include <cstring>

#define IS_DEBUG 0

void dgb(const char * fmt, ...)
{
	#if IS_DEBUG
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
	#endif
}

int ar[10];

char s[5000];
char new_s[5000];
int n,k;

int count_rle()
{
	char last = -1;
	int ans = 0;
	for(int i = 0; i < n; i++)
	{
		if (new_s[i] != last)
			ans++;
		last = new_s[i];
	}
	return ans;
}

void build_str()
{
	for(int i = 0; i < n; i+=k)
		for(int j = 0; j < k; j++)
			new_s[i+j] = s[i+ar[j]];
}

int min(int a, int b)
{
	return a < b ? a : b;
}


void solve(int test_case)
{
	scanf("%d\n", &k);
	scanf("%s\n", &s);
	n = strlen(s);
	for(int i = 0; i < k; i++)
		ar[i] = i;
	int answer = 1000000;
	do
	{
		build_str();
		answer = min(answer, count_rle());
	}
	while(std::next_permutation(ar, ar+k));


	printf ("Case #%d: %d\n", test_case, answer);
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		solve(i+1);
	return 0;
}