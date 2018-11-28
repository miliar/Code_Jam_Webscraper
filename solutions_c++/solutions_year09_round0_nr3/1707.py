#include <iostream>
#include <cstring>

#define LEN  19
char p[20] = "welcome to code jam" ;
char s[40];
int n , cnt , len , ca;

void dfs(int i , int k)
{
	if( i == LEN )
	{
		cnt++;
		if(cnt > 10000) cnt -= 10000;
		return;
	}
	

	int j;
	for( j = k ; j < len - LEN + i + 1 ; j++)
	{
		if( p[i] == s[j])
			dfs( i+1 , j+1 );
	}
}

int main()
{
	freopen("C-small-attempt0.in" , "r" , stdin);
	freopen("C-small.out" , "w" , stdout);
	scanf("%d" , &n);
	getchar();
	for( ca = 1 ; ca <= n ; ca++)
	{
		gets(s);
		len = strlen(s);
		int i;
		cnt = 0;
		for( i = 0 ; i < len && s[i] != 'w' ; i++);
		printf("Case #%d: " , ca);
		if( len - i < LEN)
			printf("%04d\n" , 0);
		else 
		{
			dfs( 0 , i);
			printf("%04d\n" , cnt);
		}
	}
	return 0;
}

/*

3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam


*/