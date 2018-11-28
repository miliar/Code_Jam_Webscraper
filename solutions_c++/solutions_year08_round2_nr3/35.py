#include <cstdio>
#include <algorithm>

#define LB(x) ((x)&(-x))

const int MAXK = 1 << 20;
const int MAXN = 1 << 7;

int n;
int k;
int a[MAXK];
int b[MAXN];

int it[MAXK];

void read() {
	int i;
	
	scanf ("%d%d",&n,&k);
	for (i=1;i<=k;i++)
		scanf ("%d",&b[i]);
}

void init() {
	memset ( a , 0 , sizeof a );
	memset ( b , 0 , sizeof b );
	memset ( it , 0 , sizeof it );
}

/*
void slow() {
	int i , j;
	int cur = 1;
	int now;
	
	a[1] = 1;
	for (i=1;i<n;i++) {
		j = 0;
		
		while ( 1 ) {
			if ( !a[cur] ) 
				++ j;
			if ( j == i ) break;
			
			++ cur;
			if ( cur == n + 1 )
				cur = 1;
		}
		while ( 1 ) {
			++ cur;
			if ( cur == n + 1 )
				cur = 1;
			if ( !a[cur] )
				break;
		}
		
		a[cur] = i + 1;
	}
	
	printf ("%d",a[ b[1] ]);
	for (i=2;i<=k;i++)
		printf (" %d",a[ b[i] ]);
	printf ("\n");
}
*/

int ins ( int x ) {
	for (;x<=n;x+=LB(x))
		++ it[x];
}

int query ( int x ) {
	int ans = 0;
	for (;x>0;x-=LB(x))
		ans += it[x];
	return ans;
}

int ask ( int x , int y ) {
	return query ( y ) - query ( x - 1 );
}

int bsearch ( int l , int r , int x ) {
	int mid;
	int f = query ( l - 1 );
	int q = l;
	
	while ( l < r ) {
		mid = l + (r - l) / 2;

	//	printf ("%d %d    --   %d    %d   %d %d     %d\n",l,r,mid,q,query(mid),f,x);
		
		if ( mid - q + 1 - query ( mid ) + f >= x )
			r = mid;
		else
			l = mid + 1;
	}
	
	return l;
}

void fast() {
	int i , j;
	int x;
	int cur = 2;
	
	a[1] = 1;
	ins ( 1 );
	
	for (i=1;i<n;i++) {
		j = i + 1;
		x = n - cur + 1 - ask ( cur , n );
	//	printf ("from %d to the end: %d\n",cur,x);
		
		if ( x < j ) {
			j -= x;
			
			x = n - ask ( 1 , n );
			while ( j > x ) j -= x;
			
		//	printf ("search for  %d   from 1 to %d\n",j,n);
			cur = bsearch ( 1 , n , j );
		}
		else
			cur = bsearch ( cur , n , j );

		ins ( cur );
	//	printf ("%d    %d\n",cur,i+1);
		a[cur] = i + 1;
		++ cur;
		if ( cur == n + 1 ) 
			cur = 1;
	}
	
	printf ("%d",a[ b[1] ]);
	for (i=2;i<=k;i++)
		printf (" %d",a[ b[i] ]);
	printf ("\n");
}

int main() {
	int k;
	int i;
	
	scanf ("%d",&k);
	
	for (i=1;i<=k;i++) {
		printf ("Case #%d: ",i);
		init();
		read();
		fast();
	}
	
	return 0;
}
