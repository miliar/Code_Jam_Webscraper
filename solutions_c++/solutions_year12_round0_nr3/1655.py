#include <cstdio>
#include <cstdlib>
#include <algorithm>

#define SIZE_N 2000010

FILE *in , *out ;

int T , a , b ;

int pow[10] ;
int vis[SIZE_N] , cnt[SIZE_N] ;

int gen(int tem[] , int d)
{
	int r = tem[d - 1] ;
	for(int i = d - 2 ; i >= 0 ; --i)
	{
		r = r * 10 + tem[i] ;
		tem[i + 1] = tem[i] ;
	}
	tem[0] = r / pow[d - 1] ;
	return r ;
}

int dig(int now)
{
	int r = 0 ;
	while(pow[r + 1] < now) ++r ;
	return r ;
}

void go(int now)
{
	int d = 0 , tem[20] ;
	for(int i = 0 ; i < 20 ; ++i) tem[i] = 0 ;
	
	for( ; now / pow[d] != 0 ; ++d)
		tem[d] = (now / pow[d]) % 10 ;
	
	vis[now] = now ;
	for(int i = 0 ; i < d ; ++i)
	{
		int t = gen(tem , d) ;
		//printf("%d %d %d\n" , now , d , t) ;
		if(t > SIZE_N) continue ;
		if(dig(t) == dig(now)) vis[t] = now ;
	}
	//system("pause") ;
}

int main(void)
{
	pow[0] = 1 ;
	for(int i = 1 ; i < 10 ; ++i)
		pow[i] = pow[i - 1] * 10 ;
	
	for(int i = 1 ; i < SIZE_N ; ++i)
		if(vis[i] == 0) go(i) ;
	puts("xd") ;
	
	in = fopen("C-large.in" , "r") ;
	out = fopen("C-large.out" , "w") ;
	
	fscanf(in , "%d" , &T) ;
	for(int count = 1 ; count <= T ; ++count)
	{
		for(int i = 0 ; i < SIZE_N ; ++i)
			cnt[i] = 0 ;
		
		fscanf(in , "%d%d" , &a , &b) ;
		for(int i = a ; i <= b ; ++i)
			++cnt[vis[i]] ;
		
		long long ans = 0 ;
		for(int i = 0 ; i <= b ; ++i)
		{
			ans += (long long)cnt[i] * (cnt[i] - 1) / 2 ;
			
			//printf("%d %d\n" , i , cnt[i]) ;
		}
		
		fprintf(out , "Case #%d: %I64d\n" , count , ans) ;
	}
	
	fclose(in) , fclose(out) ;
	system("pause") ;
	return 0 ;
}
