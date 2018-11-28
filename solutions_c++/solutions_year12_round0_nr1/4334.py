#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <list>
#include <queue>
using namespace std;

#define FOR(t,l,r) for (int t=l; t<r; t++)
#define forn(i) for (i=0; i<n; i++)
#define all int t; forn(t)
#define alli int i; forn(i)
#define max(x,y) ((x>y)?x:y)
#define min(x,y) ((x<y)?x:y)
#define abs(x) ((x<0)?-x:x)
#define pi 2*acos(0.)
#define inf (1<<24)
#define eps 1e-15
#define end cout<<endl
#define pb push_back
#define mp make_pair
#define sz size()
#define LL long long
#define VI vector<int>
#define VII vector<VI>
#define pii pair<int,int>
// #define x first
// #define y second

map<char,char> m;

void init () {
	m[' ']=' ';
	m['a']='y';
	m['b']='h';
	m['c']='e';
	m['d']='s';
	m['e']='o';
	m['f']='c';
	m['g']='v';
	m['h']='x';
	m['i']='d';
	m['j']='u';
	m['k']='i';
	m['l']='g';
	m['m']='l';
	m['n']='b';
	m['o']='k';
	m['p']='r';
	m['q']='z';
	m['r']='t';
	m['s']='n';
	m['t']='w';
	m['u']='j';
	m['v']='p';
	m['w']='f';
	m['x']='m';
	m['y']='a';
	m['z']='q';
}

int main () {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T;
	char s[1342];
	init();
	scanf("%d",&T);
	gets(s);
	FOR(i,0,T) {
		printf("Case #%d: ",i+1);
		gets(s);
		FOR(t,0,strlen(s))
			printf("%c",m[s[t]]);
		printf("\n");
	}
return 0;
}





