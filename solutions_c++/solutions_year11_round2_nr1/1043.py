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

int main()
{
  int I,N,L,P;
  scanf("%d",&N);
  char ch[102][102];
  for(I=0; I<N; ++I)
  {
	  int i,n;
    scanf("%d",&n);
	
	// read data
	for(i=0; i<n; ++i)
	{
		scanf("%s", ch[i]);
	}
	
	double wp[100], owp[100], oowp[100];
	for(i=0; i<n; ++i)
	{
		int win=0,lose=0;
		{
			for(int j=0; j<n; ++j) if(ch[i][j]=='1') ++win; else if( ch[i][j]=='0' ) ++lose;
			wp[i]= win/ (double)(win+lose);
		}
	}
	for(i=0; i<n; ++i)
	{
		int team =0;
		double total =0;
		for(int j=0; j<n; ++j)
		{
			if(ch[i][j]=='.') continue;
			++ team;
			int win=0,lose=0;
			for(int k=0; k<n; ++k) 
			{
				if( k==i ) continue;
				if(ch[j][k]=='1') ++win; else if( ch[j][k]=='0' ) ++lose;
				
			}
			total +=  win/ (double)(win+lose);
//			printf("\nowp[%d][%d]= %d/(%d+%d) ", i,j,win,win,lose);
		}
		if( team ) { owp[i] = total / team; }
		else owp[i]=0;
		
//		printf("\nowp[%d]=%lf ", i, owp[i]);
	}
	for(i=0; i<n; ++i)
	{
		int team =0;
		double total =0;
		for(int j=0; j<n; ++j)
		{
			if(ch[i][j]=='.') continue;
			++ team;
			total +=  owp[j];
		}
		if( team ) { oowp[i] = total / team; }
		else oowp[i]=0;
	}

    printf("Case #%d:\n",I+1);
	for(i=0; i<n; ++i)

		printf("%.10lf\n",  0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		
  }
  return 1;
}
