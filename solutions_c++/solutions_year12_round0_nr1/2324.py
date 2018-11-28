#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

char correspondence[256];

string inp1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string out1 = "our language is impossible to understand";
string inp2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string out2 = "there are twenty six factorial possibilities";
string inp3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
string out3 = "so it is okay if you want to just give up";

int main()
{
	int i, j, t;

	bool used[256] = {0};
	for(i = 0; i < inp1.length(); i++)
	{
		used[inp1[i]] = true;
		correspondence[inp1[i]] = out1[i];
	}
	for(i = 0; i < inp2.length(); i++)
	{
		used[inp2[i]] = true;
		correspondence[inp2[i]] = out2[i];
	}
	for(i = 0; i < inp3.length(); i++)
	{
		used[inp3[i]] = true;
		correspondence[inp3[i]] = out3[i];
	}
	
	for(i = 'a'; i <= 'z'; i++)
		if (correspondence[i] == 0)
			for(j = 'z'; j >= 'a'; j--)
				if (!used[j])
				{
					used[j] = true;
					correspondence[i] = j;
					break;
				}

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	char s[101];
	gets(s);
	for(int cur = 1; cur <= t; cur++)
	{
		gets(s);
		printf("Case #%d: ", cur);
		for(i = 0; s[i]; i++)
			if (s[i] == ' ')
				printf(" ");
			else
				printf("%c", correspondence[s[i]]);
		puts("");
	}

	return 0;
}