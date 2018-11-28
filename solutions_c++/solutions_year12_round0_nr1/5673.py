#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

typedef long long ll; 
#define SQR(x) ((x)*(x))
const double EPS = 1e-8;
const double PI  = acos(-1.0);
char ex[3][100] = 
	{"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	 "de kr kd eoya kw aej tysr re ujdr lkgc jv"
	};
char sol[3][100] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};
char charmap[128];
char buf[512];
int main()	{
	memset(charmap, 0, sizeof(charmap));
	for(int i = 0; i < 3; i++)
		for(int j = 0; ex[i][j]; j++)
			if(islower(ex[i][j]))
				charmap[ex[i][j]] = sol[i][j];
	charmap['z'] = 'q';
	charmap['q'] = 'z';
	int T;
	gets(buf);
	sscanf(buf, "%d", &T);
	for(int t = 1; t <= T; t++)	{
		gets(buf);
		for(int i = 0; buf[i]; i++)
			if(islower(buf[i]))
				buf[i] = charmap[buf[i]];
		printf("Case #%d: %s\n", t, buf);
	}
	return 0;
}