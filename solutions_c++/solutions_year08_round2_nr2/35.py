#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

int a , b , p;

int prime[1024];
int pr[1024];
int pc;

int c[1024];
set < int > st;

void find_primes() {
	memset ( prime , 1 , sizeof prime );
	int i , j;
	
	for (i=2;i<=1000;i++)
		if ( prime[i] ) {
			pr[ ++ pc ] = i;
			for (j=i*i;j<=1000;j+=i)
				prime[j] = 0;
		}
}

int boss ( int x ) {
	if ( x == c[x] ) return x;
	return c[x] = boss ( c[x] );
}

void solve() {
	st.clear();
	int i , j , k;
	int d;
	
	scanf ("%d%d%d",&a,&b,&p);
	
	for (d=1;d<=pc;d++)
		if ( pr[d] >= p )
			break;
	
	for (i=a;i<=b;i++)
		c[i] = i;
	
	for (i=a;i<=b;i++)
		for (j=i+1;j<=b;j++)
			if ( boss ( i ) != boss ( j ) )
				for (k=d;k<=pc;k++)
					if ( i % pr[k] == 0 && j % pr[k] == 0 )
						c[ boss ( i ) ] = boss ( j );
	
	for (i=a;i<=b;i++)
		st.insert ( boss ( i ) );
	
	printf ("%d\n",(int)st.size());
}

int main() {
	int k;
	int i;
	
	scanf ("%d",&k);
	
	find_primes();
	
	for (i=1;i<=k;i++) {
		printf ("Case #%d: ",i);
		solve();
	}
	
	return 0;
}
