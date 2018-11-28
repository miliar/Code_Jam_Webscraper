#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cassert>
#include <ctime>

#define next next_asdf
#define prev prev_asdf
#define y1 y1_asdf
#define ws ws_asdf

#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),(a).end()
#define forn(i, n) for(int (i)=0;(i)<(n);++(i))
#define ford(i, n) for(int (i)=1;(i)<=(n);++(i))
#define forit(it, v) for(typeof((v).begin()) (it)=(v).begin();(it)!=(v).end();++(it))

#ifdef home
	#define eprintf(...) {fprintf(stderr, __VA_ARGS__);fflush(stderr);}
#else
	#define eprintf(...) {}
#endif

#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

using namespace std;

typedef long long ll;
typedef double ld;
typedef pair<int, int> pi;
typedef vector<int> vi;

const ld eps=1e-10;
const int inf=(int)1e9;

/* --- main part --- */

#define TASK_NAME "a"
const int maxn=(int)1e3+10;
char s[maxn][maxn];
int p[256];

int main()
{
		assert(freopen(TASK_NAME"0.in", "r", stdin));
	int n;
	scanf("%d\n", &n);
	for(int i=0;i<2*n;i++) gets(s[i]);
	for(int i=0;i<n;i++)
	{
		for(int j=0;s[i][j];j++) p[(int)s[i][j]]=s[i+n][j];
	}
	p[(int)'z']=(int)'q';
	p[(int)'q']=(int)'z';
	for(int i='a';i<='z';i++) eprintf("%c --> %c\n", (char)i, (char)p[i]);
	#ifdef home
		assert(freopen(TASK_NAME".in", "r", stdin));
		assert(freopen(TASK_NAME".out", "w", stdout));
	#endif
	scanf("%d\n", &n);
	ford(_, n)
	{
		gets(s[0]);
		printf("Case #%d: ", _);
		for(int i=0;s[0][i];i++)
		{
			int ch=(int)s[0][i];
			if(p[ch]>0) printf("%c", (char)p[ch]);
			else printf("(%c?)", ch);
		}
		printf("\n");
	}			 
	#ifdef home
		eprintf("%d ms\n", (int)(clock()*1000.0/CLOCKS_PER_SEC));
	#endif
	return 0;
}	



