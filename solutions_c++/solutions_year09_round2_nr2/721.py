#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;


int main()
{
	FILE *in;
	in = fopen("input.txt","rt");
	freopen("output.txt", "w+", stdout);
	int T,i,counter;
	T=0;
	char ch;
	VI c(30);
	for(ch=fgetc(in); ch!='\n'; T=T*10+ch-'0', ch=fgetc(in));
	REP (t, T)
	{
		cout << "Case #"<<(t+1)<< ": ";
		for(i=0, ch=fgetc(in); ch!='\n' && ch!=EOF; c[i]=ch-'0', ch=fgetc(in), i++);
		int min=i-1; 
		while((min>0) &&(c[min]<=c[min-1])) min--;
		min--;
		if (min<0)
		{
			REP(o,i)
				c[i-o]=c[i-o-1];
			i++;
			min++;
			c[0]=0;
		}
		int max=min+1;
		for(int p=max; p<i; p++)
		{
			if((c[p]>c[min]) && (c[max]>=c[p])) max=p;
		}
		ch=c[max];
		c[max]=c[min];
		c[min]=ch;
		VI c2(i-min-1);
		REP(o, i-min-1)
			c2[o]=c[min+o+1];
		SORT(c2);
		REP(tt,min+1)
			cout << c[tt];
		REP(tt,i-min-1)
			cout << c2[tt];
		cout << endl;
	}

	return 0;
}
