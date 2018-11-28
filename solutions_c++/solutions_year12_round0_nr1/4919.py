/*
** In the name of God **
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iterator>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define EPS 1e-8
#define MOD 1000000007
#define INF 100000000
#define SQR(a) ((a)*(a))
#define e(a,b) (fabs(a-b)<EPS)
#define pb push_back
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

int mp[26];

void pre()
{
	string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string t = "our language is impossible to understand";
	FR(i,s.length())
	{
		if(isspace(s[i]) && isspace(t[i])) continue;
		if(mp[s[i]-'a']==-1)
			mp[s[i]-'a']=t[i]-'a';
	}
	s="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	t="there are twenty six factorial possibilities";
	FR(i,s.length())
	{
		if(isspace(s[i]) && isspace(t[i])) continue;
		if(mp[s[i]-'a']==-1)
			mp[s[i]-'a']=t[i]-'a';
	}
	s="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	t="so it is okay if you want to just give up";
	FR(i,s.length())
	{
		if(isspace(s[i]) && isspace(t[i])) continue;
		if(mp[s[i]-'a']==-1)
			mp[s[i]-'a']=t[i]-'a';
	}
	mp['z'-'a']='q'-'a';
	mp['q'-'a']='z'-'a';
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	CLR(mp,-1);
	pre();
	char s[101];
	int t;
	scanf("%d",&t);
	gets(s);
	FOR(q,1,t+1)
	{
		gets(s);
		for(int i=0;s[i];i++)
			if(isspace(s[i])) continue;
			else s[i] = mp[s[i]-'a']+'a';
		printf("Case #%d: %s\n",q,s);
	}
}