#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;

char GtoNormal(char a)
{
	switch (a)
	{
	case 'a': return 'y';
		break;
	case 'b': return 'h';
		break;
	case 'c':return 'e';
		break;
	case 'd':return 's';
		break;
	case 'e': return 'o';
		break;
	case 'f':return 'c';
		break;
	case 'g':return 'v';
		break;
	case 'h':return 'x';
		break;
	case 'i':return 'd';
		break;
	case 'j': return 'u';
		break;
	case 'k':return 'i';
		break;
	case 'l':return 'g';
		break;
	case 'm':return 'l';
		break;
	case 'n':return 'b';
		break;
	case 'o':	return 'k';
		break;
	case 'p': return 'r';
		break;
	case 'q': return 'z';
		break;
	case 'r':return 't';
		break;
	case 's':return 'n';
		break;
	case 't':return 'w';
		break;
	case 'u':return 'j';
		break;
	case 'v':return 'p';
		break;
	case 'w':return 'f';
		break;
	case 'x':return 'm';
		break;
	case 'y': return 'a';
		break;
	case 'z':	return 'q';
		break;
	default: return a;
		break;

	}
}

char buf[200];

int main(void)
{
	FILE *inf;

	inf=fopen("A-small-attempt0.in", "r");
	freopen("A.out", "w", stdout);

	int nTest;
	fgets(buf, 120, inf);
	nTest = atoi(buf);

	for (int i=0;i<nTest;i++)
	{
		fgets( buf, 120, inf);
		char* tmpBuf=buf;
		while (*tmpBuf != NULL)
		{
			*tmpBuf = GtoNormal  (*tmpBuf);
			tmpBuf++;
		}
		printf("Case #%d: %s", i+1, buf);

	}
	return 1;
}