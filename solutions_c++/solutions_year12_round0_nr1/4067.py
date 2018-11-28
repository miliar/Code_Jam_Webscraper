#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <assert.h>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GL ({LL t;scanf(" %lld",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define inf 1000000005
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

#define MAXN 100000

string in[] = {"ejpoz mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string out[] = {"oureq language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

char M[26];

void precompute() {
	memset(M,-1,sizeof(M));
	REP (i,3) {
		int l=strlen(&in[i][0]);
		REP (j,l) {
			if(in[i][j]==' ') continue;
			M[in[i][j]-'a']=out[i][j];
		}
	}
	M['q'-'a']='z';
	return;
}

string test;

int main() {
	int yo=0;
	precompute();
	int _=GI;
	getchar();
	for (;_--;) {
		getline(cin, test, '\n');
		REP (i,test.sz) {
			if(test[i]==' ') continue;
			test[i]=M[test[i]-'a'];
		}
		cout<<"Case #"<<++yo<<": "<<test<<endl;
	}
	return 0;
}

