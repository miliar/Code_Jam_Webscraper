#include <iostream>
#include <iterator>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <sstream>
#include <cassert>
#define FOR(i,a,n) for(int i=(a),_n=(n); i<=_n; i++)
#define FORD(i,a,n) for(int i=(a),_n=(n); i>=_n; i--)
#define REP(i,n) for(int i=0,_n=(n); i<_n; i++)
#define REPD(i,n) for(int i=n-1; i>=0; i--)
#define EACH(it, con) for(__typeof((con).begin()) it = (con).begin(); it!=(con).end(); it++)
#define pb push_back
#define TWO(n) ( 1ll << (n) )
#define ON(bit,n) (bit | TWO(n))
#define OFF(bit,n) (bit & (~TWO(n)))
#define CONTAIN(bit,n) ((bit) & TWO(n))
#define SET(mem,val) memset(mem,val,sizeof mem)
#define pb push_back
#define all(con) con.begin(),con.end()
#define ABS(n) ((n)<0?-(n):(n))
using namespace std;
char maps[200]={};

void isi(char *s1, char*s2){
	REP(i,strlen(s1)){
		maps[s1[i]] = s2[i];
	}
}

int main()
{
	isi("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
	isi("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities");
	isi("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");
	isi("qz","zq");
	maps[' '] = ' ';
	
	/*FOR(i,'a','z'){
		
		cerr << (char)i << " : " << maps[i] << endl;
	}*/
	int test;
	scanf("%d",&test);getchar();
	FOR(cs,1,test){
		char str[2000];
		gets(str);
		REP(i,strlen(str))
			str[i] = maps[str[i]];
		printf("Case #%d: %s\n",cs,str);
	}
	return 0;
}

