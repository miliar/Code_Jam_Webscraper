#include<stdio.h>
const int NMAX(64);
char m[NMAX][NMAX];
int id[NMAX];
int N;
int res;
void init(){
	scanf("%d",&N);
	int i;
	int j;
	for( i = 0 ; i < N ; ++ i )
	{
		scanf("%s",m[i]);
		j = N - 1;
		while(m[i][j]=='0')
			--j;
		id[i] = j;
		//puts(m[i]);
	}
}
void run()
{
	int i,j;
	res = 0;
	for( i = 0 ; i < N ; ++ i){
		if(id[i] > i ){
			for( j = i + 1 ; j < N ; ++ j )	{
				if( id[j] <= i ){
					break;	
				}
			}
			res += j - i;
			int k;
			int tmp = id[j];
			for( k = j; k > i ; --k ){
				id[k] = id[k-1];
			}
			id[i] = tmp;
		}
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int cnt  = 0 ;
	while( T -- )
	{
		init();
		run();
		printf("Case #%d: %d\n",++cnt,res);
	}
	return 0;
}
