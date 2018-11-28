#include <stdio.h>
#include <string.h>

#define MAXN 10010
int n,hash[MAXN];
int tree[MAXN];
void add(int x)
{
	while( x<MAXN )
	{
		tree[x] ++;
		x += x&-x;	
	}	
}
int sum(int x)
{
	int sum	=0;
	while( x>0 )
	{
		sum += tree[x];
		x -= x&-x;
	}
	return sum;
}

int main(){
	int kase,x,y,ka=1;
	freopen("a.out","w",stdout);
	scanf("%d", &kase);
	
	while( ka<=kase )
	{
		scanf("%d", &n );
		memset( hash , 0  ,sizeof(hash));
		memset( tree , 0  ,sizeof(tree));
		for(int i=0 ; i<n ; i++ )
		{
			scanf("%d%d", &x , &y);
			hash[x] = y;	
		}
		int ans = 0;
		for(int i=MAXN-1 ; i ; i--)
		if(hash[i]){
			ans += sum( hash[i] );
			add( hash[i] );
		}
		printf("Case #%d: %d\n", ka++ ,ans );
	}
	return 0;	
}
