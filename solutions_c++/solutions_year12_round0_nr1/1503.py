#include <iostream>
using namespace std;

char sFromG[255];

void BuildMap(const char* ss, const char* sg)
{
	for (int i = 0; ss[i] != '\0'; ++i)
	{
		char cs = ss[i];
		char cg = sg[i];
		if (sFromG[cg] != '\0' && sFromG[cg] != cs)
			__asm int 3;
		sFromG[cg] = cs;
	}
}

int main()
{
	for (int i = 0; i < 256; ++i)
		sFromG[i] = '\0';

	BuildMap("a zoo", "y qee");
	BuildMap("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi");
	BuildMap("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	BuildMap("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv");
	BuildMap("q", "z");

	for (char i = 'a'; i < 'z'; ++i)
	{
		if (sFromG[i] == '\0')
			__asm int 3;
	}

	int T;
	cin >> T;
	char s[128];
	char g[128];
	cin.getline(g, 127);
	for (int t = 0; t < T; ++t)
	{
		cin.getline(g, 127);
		int i;
		for (i = 0; g[i] != '\0'; ++i)
			s[i] = sFromG[g[i]];
		s[i] = '\0';
		cout << "Case #" << t+1 << ": " << s << endl;
	}
	return 0;
}
