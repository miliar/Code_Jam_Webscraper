#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAX 105
#define i64 __int64

int gcd(int a, int b) {
	if(b == 0) return a;
	return gcd(b, a%b);
}

int main() {
	int T,kase=1;
	int Pd,Pg,g,a,b;
	i64 N;
	bool f;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %I64d %d %d",&N,&Pd,&Pg);
		f = 1;
		if(Pg == 100 && Pd < 100) f = 0;
		if(Pg == 0 && Pd > 0) f = 0;
		g = gcd(Pd,100);
		a = Pd / g;
		b = 100 / g;
		/*g = gcd(Pg,100);
		c = Pg / g;
		d = 100 / g;
		e = a*d - b*c;*/
		if(b > N) f = 0;
		if(f) printf("Possible\n");
		else printf("Broken\n");
		
	}
	return 0;
}