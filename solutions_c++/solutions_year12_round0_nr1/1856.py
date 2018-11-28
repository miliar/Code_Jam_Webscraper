#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <functional>
#define rep(i,n) for(int i=0;i<(n);++i)
#define foreach(i,v) for(__typeof(v.begin()) i=v.begin();i!=v.end();++i)
#define ass(v) (v)||++*(int*)0;
using namespace std;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<double> VD;
const char *dst[3] =
{
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};
const char *src[3] =
{
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};
const char *key = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
//	char tab[256];
//	memset(tab, '?', sizeof(tab));
//	rep(i, 3)
//	{
//		int n = strlen(src[i]);
//		rep(j, n) tab[(int)dst[i][j]]=src[i][j];
//	}
//	for (int i = 'a'; i <= 'z'; ++i) putchar(tab[i]);
	int n;
	scanf("%d\n", &n);
	rep(i, n)
	{
		char line[1024];
		gets(line);
		printf("Case #%d: ", i + 1);
		for (char *p = line; *p; ++p)
			if (*p == ' ') putchar(' '); else putchar(key[*p - 'a']);
		puts("");
	}
	return 0;
}
