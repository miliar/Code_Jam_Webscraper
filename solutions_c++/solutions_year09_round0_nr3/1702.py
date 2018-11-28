#include<stdio.h>
#include<string.h>
const int NMAX = 512;
char p[]="welcome to code jam";
char s[NMAX];
int count[20][NMAX];
int run()
{
	memset(count,0,sizeof(count));
	int lp = strlen(p);
	int ls = strlen(s);
	int i,j;
	if( p[0]==s[0] )
		count[0][0] = 1;
	for(i = 1 ; i < ls ; i ++ )
	{
		count[0][i] = count[0][i-1];
		if(p[0] == s[i])
			count[0][i] ++;
	}
	for( i = 1 ; i < lp ; i ++ )
	{
		for( j = i ; j < ls ; j ++ )
		{
			count[i][j] = count[i][j-1];
			if(p[i] == s[j] )
				count[i][j] += count[i-1][j-1];
			count[i][j] %= 10000;
		}
	}
//	printf("%04d\n",count[lp-1][ls-1]);
	return count[lp-1][ls-1]%10000;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	gets(s);
	int i ;
	for( i = 0 ;i < T ; i ++ )
	{
		gets(s);
	//	puts(s);
		int res = run();
		printf("Case #%d: %04d\n",i+1,res);
	}
	return 0 ;
}