#include<stdio.h>
#include<string.h>
#include<iostream>

using namespace std;

string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

string t1 = "our language is impossible to understand";
string t2 = "there are twenty six factorial possibilities";
string t3 = "so it is okay if you want to just give up";

char rp[27];
char str[10000];

int main()
{
	int i, j, k;
	freopen("a-small-attempt1.in", "rt", stdin);
	freopen("a-small.out", "wt", stdout);
	rp['a' - 'a'] = 'y';
	rp['o' - 'a'] = 'e';
	rp['z' - 'a'] = 'q';
	rp['y' - 'a'] = 'a';
	rp['e' - 'a'] = 'o';
	rp['q' - 'a'] = 'z';
	for(i = 0; i < s1.length(); i++)
	{
		if(s1[i] != ' ')
		{
			rp[s1[i] - 'a'] = t1[i];
		}
	}

	for(i = 0; i < s2.length(); i++)
	{
		if(s2[i] != ' ')
		{
			rp[s2[i] - 'a'] = t2[i];
		}
	}

	for(i = 0; i < s3.length(); i++)
	{
		if(s3[i] != ' ')
		{
			rp[s3[i] - 'a'] = t3[i];
		}
	}

    for(i = 0; i < 26; i++)
        fprintf(stderr, "%c, %c\n", 'a' + i, rp[i]);
	int inp, kase;
	scanf("%d", &inp);
	gets(str);
	for(kase = 1; kase <= inp; kase++)
	{
		gets(str);
		int len = strlen(str);
		for(i = 0; i < len; i++)
		{
			if(str[i] == ' ')
				continue;
			str[i] = rp[str[i] - 'a'];
		}
		printf("Case #%d: %s\n", kase, str);
	}
	return 0;
}
