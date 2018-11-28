#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <iostream>


char list[30];

struct OverrideString
{
   char word[128];
   int length;
   char ch[26];
   OverrideString() : length(0) { for(int i=0; i<26; ++i) ch[i] = 0; }
   // given list[30], which string hits first
};

struct StringHit
{
   bool same;
   char hitpattern[20];
   StringHit() : same(false) { for(int i=0; i<20; ++i) hitpattern[i] = 0; }
   bool operator == ( const StringHit& p ) { for(int i=0; i<20; ++i) if( hitpattern[i] != p.hitpattern[i] ) return false; return true; }
   void mark(int i) { hitpattern[i>>3]|=(1<<(i&7)); }
};

bool check(char ch[102][102], int r, int c)
{
	// get every corner, try replace with /\.\/
	while(1)
	{
		int i,j;
		for(i=0; i<r; ++i)
		{
			for(j=0; j<c; ++j)
				if( ch[i][j]=='#' )
					break;
			if( j<c )
				break;
		}
		if( i==r )
			return true;
			
		if( i<r-1 && j<c-1 && ch[i][j+1]=='#' && ch[i+1][j]=='#' && ch[i+1][j+1]=='#' ) 
		{
			ch[i][j]='/';
			ch[i][j+1]='\\';
			ch[i+1][j]='\\';
			ch[i+1][j+1]='/';
			continue;
		}
		return false;
	}
	return true;
}

int main()
{
  int I,N,L,P;
  scanf("%d",&N);
  char ch[102][102];
  for(I=0; I<N; ++I)
  {
	  int i,j,r,c;
    scanf("%d%d",&r,&c);
	
	// read data
	for(i=0; i<r; ++i)
	{
		scanf("%s", ch[i]);
	}

	bool poss = check(ch, r, c);
	if(!poss)
	{
		for(int i = 0; i<r ; ++i)
		for(int j = 0; j<c ; ++j)
			if( ch[i][j] != '.' ) ch[i][j]='#';
	}
	
    printf("Case #%d:\n",I+1);
	if( !poss)
		printf("Impossible\n");
	else
	{
		for(i=0; i<r; ++i)
			printf("%s\n", ch[i] );
	}
		
  }
  return 1;
}
