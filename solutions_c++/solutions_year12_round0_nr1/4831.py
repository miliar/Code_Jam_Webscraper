#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int main(int argc, char** argv)
{
	int T;
	map<char, char> mp;
	mp['a'] = 'y';
	mp['b'] = 'h';
	mp['c'] = 'e';
	mp['d'] = 's';
	mp['e'] = 'o';
	mp['f'] = 'c';
	mp['g'] = 'v';
	mp['h'] = 'x';
	mp['i'] = 'd';
	mp['j'] = 'u';
	mp['k'] = 'i';
	mp['l'] = 'g';
	mp['m'] = 'l';
	mp['n'] = 'b';
	mp['o'] = 'k';
	mp['p'] = 'r';
	mp['q'] = 'z';
	mp['r'] = 't';
	mp['s'] = 'n';
	mp['t'] = 'w';
	mp['u'] = 'j';
	mp['v'] = 'p';
	mp['w'] = 'f';
	mp['x'] = 'm';
	mp['y'] = 'a';
	mp['z'] = 'q';

	FILE* fp = fopen("D:\\A-small-attempt0.in", "r");
	FILE* fo = fopen("D:\\output.txt", "w");
	fscanf(fp, "%d\n", &T);

	for (int kase = 1; kase <= T; kase ++)
	{
		char sent[1024];
		fgets(sent, 1024, fp);
		for (int i = 0; sent[i] != '\n'; i ++)
		{
			if (sent[i] == ' ')
				continue;
			sent[i] = mp[sent[i]];
		}
		fprintf(fo, "Case #%d: %s", kase, sent);
	}
	return 0;
}

