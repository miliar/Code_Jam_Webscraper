#include<stdio.h>
#include<string.h>
const int NMAX =512;
int L,D,N;
char dic[NMAX*10][16];
char pattern[NMAX][320];
void init()
{
	memset(dic,0,sizeof(dic));
	memset(pattern,0,sizeof(pattern));
	scanf("%d%d%d",&L,&D,&N);
	int i;
	for( i = 0 ; i < D ; i ++ )
	{
		scanf("%s",dic[i]);
		//	puts(dic[i]);
	}
	for( i = 0 ; i < N ; i ++ )
	{
		scanf("%s",pattern[i]);
		//	puts(pattern[i]);
	}
}
bool judge(int iDic, int iPattern )
{
	char*p = pattern[iPattern];
	char*d = dic[iDic];
	for( ;*d&&*p; )
	{
		if(*p == '(' )
		{
			p ++ ;
			bool match = false;
			while( *p && *p != ')' )
			{
				if( *d == *p )
					match = true;
				p ++ ;
			}
			if( !match )
				return false;
			p++;
			d++;
			continue;
		}
		if(*p == *d )
		{
			p ++;
			d ++;
			
		}else
			return false;
		
	}
	return true;
}
void run()
{
	int i,j;
	for( i = 0 ; i < N ; i ++ )
	{
		int cnt  = 0;
		for( j = 0 ; j < D ; j ++ )
		{
			if(judge(j,i))
				cnt ++ ;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	init();
	run();
	return 0;
}