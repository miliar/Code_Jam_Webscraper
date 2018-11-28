#include <cstdio>
#include <cstring>

const int maxn = 5005;

int prime[maxn];
bool mk[maxn];
void getprime() 
{
	memset( mk , 0 , sizeof(mk) );
	for (int i = 2; i < maxn; i++ ) 
	{
		if (!mk[i] ) prime[++prime[0]] = i;
		for ( int j = 1; j <= prime[0] && i * prime[j] < maxn; j++ ) 
		{
			mk[i*prime[j]] = 1;
			if ( i % prime[j] == 0 ) break;
		}	
	}
}

int getp( int x ) {
	int res = 0;
	while ( res+1 <= prime[0] && prime[res+1] <= x ) res++;
	return res;
}

int getpp( int x , int y ) {
	int res = 0 , t = 1;
	while ( t*y <= x ) {
		res++;
		t = t*y;
	}
	return res;
}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	getprime();
	int Case , q = 0;
	scanf( "%d" , &Case );
	while (Case--)
	{
		int n;
		scanf( "%d" , &n );
		int t1 = getp(n);
		int t2 = 0;
		for ( int i = 1; i <= prime[0]; i++ ) t2 += getpp(n,prime[i]);
		t2++;
		if ( n == 1 ) t2--;
		printf( "Case #%d: %d\n" , ++q , t2-t1 );
	}
	return 0;
}
