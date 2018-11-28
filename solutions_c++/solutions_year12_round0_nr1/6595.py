#define PROBNAME ""

#include <stdio.h>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <ctype.h>
#include <math.h>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <bitset>
#include <map>
#include <algorithm>
#include <limits.h>
#include <time.h>
#include <utility>
#include <numeric>
using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii > vpii;
template<class T> inline T abs(const T& x){return x>0?x:-x;}
template<class T> inline T sqr(const T& x){return x*x;}
template<class T> inline string tostr(const T& a){ostringstream os("");os<<a;return os.str();}

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(x) (x).begin(),(x).end()
#define clr(t,v) memset((t),(v),sizeof(t))
#define endl ('\n')

const int inf = 1999999999;
const double pi = acos(-1.0);
const double eps = 1e-9;
inline char gc(){char c;while(isspace(c=getchar()));return c;}
inline int gs(char*s){fgets(s,9999999,stdin);int l=strlen(s);while(l&&isspace(s[l-1]))s[--l]=0;return l;}

#define printTime {printf("%f\n",(float)(clock()-start)/CLOCKS_PER_SEC);start=clock();}

//#define DEBUG

#ifdef DEBUG
#define dprintf(args, ...) printf(args, ##__VA_ARGS__)
#else
#define dprintf(args, ...) (0)
#endif

int main() {
	//clock_t start = clock();
	//freopen(PROBNAME".in","r",stdin); freopen(PROBNAME".out","w",stdout);
	//ios::sync_with_stdio(false);

	string toEng = "yhesocvxduiglbkrztnwjpfmaq";
	int t;
	scanf("%d\n",&t);
	int tmpt = t;
	while (tmpt--) {
		char input[110];
		int len = gs(input);
		printf("Case #%d: ",t-tmpt);
		for (int i = 0; i < len; i++) {
			if (isalpha(input[i])) printf("%c", toEng[input[i]-'a']);
			else printf("%c",input[i]);
		}
		printf("\n");
	}

	return 0;
}