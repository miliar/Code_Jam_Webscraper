#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

int main()
{
	string ori[3]={	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
					"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string cha[3]={	"our language is impossible to understand",
					"there are twenty six factorial possibilities",
					"so it is okay if you want to just give up"};

	char mp[256];
	REP(i,3) REP(j,SZ(ori[i]))
		mp[ori[i][j]]=cha[i][j];
	mp['z']='q';
	mp['q']='z';

	int tn;
	cin>>tn;
	char ln[10000];
	gets(ln);
	while(tn--) {
		gets(ln);
		int len = strlen(ln);
		
		static int qq=0;
		printf("Case #%d: ",++qq);

		REP(i,len)
			printf("%c",mp[ln[i]]);
		cout<<endl;
	}
	return 0;
}
