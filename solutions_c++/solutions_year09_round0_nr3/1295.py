#include<stdio.h>
#include<iostream>

using namespace std;

int n;


char w[] = "welcome to code jam";
char buff[1000];


int m[600][30];

int get( int len,int want)
{
	if( want == -1)
		return 1;
	if( len==0)
		return 0;

	if( m[len][want] >= 0)
		return m[len][want];

	int s = 0;

	for(int i=len -1; i>=0; i--)
	{
		if( w[want] == buff[i] )
			s= ( s+ get(i,want-1) ) %10000;
	}	
	
	return m[len][want] = s;
}


int main(int argc,char ** argv)
{

	freopen ("wel.in", "r",stdin);
	freopen ("wel.out", "w",stdout);

	scanf("%d",&n);
	gets(buff);

	for( int tt=0;tt<n;tt++)
	{

		
		memset(m,0xFF,sizeof(m) );

		gets(buff);

		printf("Case #%d: %.4d\n",tt+1,get(strlen(buff),strlen(w) - 1) );
	
		

	}
	
	return 0;
}

