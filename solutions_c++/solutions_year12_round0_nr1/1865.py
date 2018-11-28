#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
#include <fstream>
#include <cassert>
#ifdef HOME_PC
#include <ctime>
#endif
using namespace std;

#pragma comment(linker,"/stack:16000000")
#pragma warning (disable : 4996)

#define ALL(v) v.begin(),v.end()
#define SZ(v) (int)v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=(start);i<(N);++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)
#define sqr(x) ((x)*(x))


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

const string encrypted = "ejp mysljylc kd kxveddknmc re jsicpdrysi\
 rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
 de kr kd eoya kw aej tysr re ujdr lkgc jv";

const string decrypted = "our language is impossible to understand\
 there are twenty six factorial possibilities\
 so it is okay if you want to just give up";

string GetMapping(const string& encrypted, const string& decrypted)
{
	char mapping[256];
	mset(mapping,'#');
	assert(encrypted.size() == decrypted.size());
	REPSZ(i,encrypted)
	{
		char encChar = encrypted[i];
		char decChar = decrypted[i];
		if(mapping[encChar] != decChar)
			assert(mapping[encChar] == '#');
		mapping[encChar] = decChar;
	}
	mapping['q'] = 'z';
	mapping['z'] = 'q';

	string result(mapping + 'a', mapping + 'z' + 1);

	string tmp = result;
	sort(ALL(tmp));
	make_unique(tmp);
	assert(tmp.size() == 26);
	return result;
}

string Translate(const string& text,const string& mapping)
{
	string result;
	REPSZ(i,text)
	{
		char c = text[i];
		if(isalpha(c))
			c = mapping[c-'a'];
		result += c;
	}
	return result;
}

int main()
{
#ifdef HOME_PC
	freopen ("A-small-attempt0.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif
	const string mapping = GetMapping(encrypted ,decrypted);
	assert(Translate(encrypted, mapping) == decrypted);
	int tt;
	scanf("%d\n",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		char str[500];
		gets(str);
		printf("Case #%d: %s\n",cas, Translate(string(str), mapping).c_str());
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

