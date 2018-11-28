//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)
#define FOREACH(IT, CON) for(__typeof(CON.begin()) IT=CON.begin(); IT!=CON.end(); ++IT)
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
const int INF=1000000000;
const LL INFLL=1000000000000000000LL;

char t[256];
char s[200];

int main()
{
	REP(i, 256)
		t[i]='#';
	t['a']='y';
	t['b']='h';
	t['c']='e';
	t['d']='s';
	t['e']='o';
	t['f']='c';
	t['g']='v';
	t['h']='x';
	t['i']='d';
	t['j']='u';
	t['k']='i';
	t['l']='g';
	t['m']='l';
	t['n']='b';
	t['o']='k';
	t['p']='r';
	t['q']='z';
	t['r']='t';
	t['s']='n';
	t['t']='w';
	t['u']='j';
	t['v']='p';
	t['w']='f';
	t['x']='m';
	t['y']='a';
	t['z']='q';
	t[' ']=' ';
	int T;
	scanf("%d", &T);
	getchar();
	FOR(lpt, 1, T){
		//wej
		gets(s);
		//prog
		for (int i=0; s[i]; ++i){
			s[i]=t[(int)s[i]];
		}
		//wyj
		printf("Case #%d: %s\n", lpt, s);
	}
	return 0;
}

