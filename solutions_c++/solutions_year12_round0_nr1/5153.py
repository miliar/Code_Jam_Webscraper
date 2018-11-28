#include <stdio.h>
#include <string.h>

const int ten[] = {1,10,100,1000,10000,100000,1000000,10000000};
const int maxn = 2000001 ;
char mp[128] , str[maxn] ;

char sth[][128] = {"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

char tmp[][128] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

inline void init()
{
	mp['y'] = 'a' ; 
	mp['q'] = 'z' ;
	mp['e'] = 'o' ;
	mp['z'] = 'q' ;
	int i , j ;
	for( i = 0 ; i < 3 ; i++)
		for( j = 0 ; tmp[i][j] ; j++)
			mp[tmp[i][j]] = sth[i][j] ;
}

int main()
{
	int i , t , j , n , m , ans ;
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	init();
	//for( i = 'a' ; i <= 'z' ; i++) printf("%c %c\n",i,mp[i]);
	scanf("%d",&t);
	getchar();
	for( i = 1 ; i <= t ; i++)
	{
		gets(str);	
		printf("Case #%d: ",i);
		for( j = 0 ; str[j] ; j++) putchar(mp[str[j]]);
		puts("");
	}
}