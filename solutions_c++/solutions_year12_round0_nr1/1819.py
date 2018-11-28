#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

char ch_ar[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	string str;
	int n;
	scanf("%d\n", &n);

	for (int i = 0; i < n; ++i)
	{
		getline(cin, str);
		printf("Case #%d: ", i+1);
		for (int j = 0; j < str.length(); ++j)
			if (str[j] == ' ') printf(" ");
			else printf("%c", ch_ar[str[j]-'a']);
		printf("\n");
	}

	return 0;
}