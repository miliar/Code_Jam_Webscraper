#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>

using namespace std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

string tt[]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv","q","e","y","z"};
string ss[]={"our language is impossible to understand","there are twenty six factorial possibilities",
	"so it is okay if you want to just give up","z","o","a","q"};

char a[1001];

int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);

	map<char,char> mm;
	rep(i,0,7)
		rep(j,0,tt[i].size())
			mm[tt[i][j]]=ss[i][j];
	int t;
	scanf("%d ",&t);
	rep(_tt,0,t)
	{
		gets(a);
		int len = strlen(a);
		printf("Case #%d: ",_tt+1);
		rep(i,0,len)
			printf("%c",mm[a[i]]);
		printf("\n");
	}

	return 0;
}
