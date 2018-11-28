#include <stdio.h>
#include <string.h>
#include <algorithm>

char s[128];

void Solve()
{
	scanf("%s", s);
	int l = strlen(s);
	bool b = std::next_permutation(s, s+l);
	if (b)
	{
		printf("%s\n", s);
		return;
	}
	int p = -1;
	for (int i=0; i<l; i++)
		if (s[i] != '0' && (p == -1 || s[i] < s[p]))
			p = i;
	std::swap(s[0], s[p]);
	std::sort(s+1, s+l);
	std::copy(s+1, s+l, s+2);
	s[l+1] = 0;
	s[1] = '0';
	printf("%s\n", s);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
