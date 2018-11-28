#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cassert>
#define rep(i,a,n) for(int i=a;i<n;i++)
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d ",n)
#define outln(n) printf("%d\n",n)
#define outl(n) printf("%lld ",n)
#define outlln(n) printf("%lld\n",n)
#define LL long long 
#define pb push_back
#define f first
#define s second
using namespace std;
int tmap[256];
string s;
int main()
{
tmap['a'] = 'y';
tmap['b'] = 'h';
tmap['c'] = 'e';
tmap['d'] = 's';
tmap['e'] = 'o';
tmap['f'] = 'c';
tmap['g'] = 'v';
tmap['h'] = 'x';
tmap['i'] = 'd';
tmap['j'] = 'u';
tmap['k'] = 'i';
tmap['l'] = 'g';
tmap['m'] = 'l';
tmap['n'] = 'b';
tmap['o'] = 'k';
tmap['p'] = 'r';
tmap['q'] = 'z';
tmap['r'] = 't';
tmap['s'] = 'n';
tmap['t'] = 'w';
tmap['u'] = 'j';
tmap['v'] = 'p';
tmap['w'] = 'f';
tmap['x'] = 'm';
tmap['y'] = 'a';
tmap['z'] = 'q';
tmap[' ']=' ';
	
	int kases;
	in(kases);
	getline(cin,s);
	for(int kase = 1;kase <= kases; kase++)
	{
		printf("Case #%d: ",kase);
		getline(cin,s);
		rep(i,0,s.size())putchar(tmap[s[i]]);
		puts("");

	}
	
	return 0;
}
