#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <assert.h>
using namespace std;

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

typedef vector<int> Polygon ;

vector<Polygon> all_p;

bool recurse_colour(int* favour, vector<Polygon>& all_p, int max, int next, int v)
{
	if( v + 1 == next)
	{
		for( int i=0; i<all_p.size(); ++i )
		{
			int nsize = all_p[i].size();
			set<int> f;
			int k;
			for(k=0; k<max; ++k) f.insert(k+1);
			// check existing favour
			int uncolour = nsize;
			for(k=0; k<nsize; ++k)
			{
				if(favour[ all_p[i][k] ])
				{
					--uncolour;
					f.erase(favour[ all_p[i][k] ]);
				}
			}
			if( !f.empty() || uncolour )
				return false;
		}
		return true;
	}
	
	if( favour[next] )
	{

		for( int i=0; i<all_p.size(); ++i )
		{
			int nsize = all_p[i].size();
			set<int> f;
			int k;
			for(k=0; k<max; ++k) f.insert(k+1);
			// check existing favour
			int uncolour = nsize;
			for(k=0; k<nsize; ++k)
			{
				if(favour[ all_p[i][k] ])
				{
					--uncolour;
					f.erase(favour[ all_p[i][k] ]);
				}
			}
			if( !f.empty() && uncolour == 0 )
				return false;
		}
		return recurse_colour( favour, all_p, max, next+1, v );
	}

	for(int j = 1; j<= max; ++j )
	{
		favour[next]=j;
		int i;
		for(  i=0; i<all_p.size(); ++i )
		{
			int nsize = all_p[i].size();
			set<int> f;
			int k;
			for(k=0; k<max; ++k) f.insert(k+1);
			// check existing favour
			int uncolour = nsize;
			for(k=0; k<nsize; ++k)
			{
				if(favour[ all_p[i][k] ])
				{
					--uncolour;
					f.erase(favour[ all_p[i][k] ]);
				}
			}
			if( !f.empty() && uncolour == 0 )
				break;
		}
	
		if( all_p.size() == i )
			return recurse_colour(favour, all_p, max, next+1, v);
	}
	
	return false;
}

typedef long long i64;

i64 gcd(i64 a, i64 b)
{
	i64 r = a%b;
	if( r==0 ) return b;
	while( r!=0 )
	{
		a = b;
		b = r;
		r = a%b;
	}
	return b;
}

int main()
{
//	i64 tt = gcd(30,12), tu = gcd(12,30);;
	
//	printf("%d %d %d %d ", gcd(1,2), (int)tt, (int)tu, gcd(2,1) );
  int I,N,L,P;
  scanf("%d",&N);
  char ch[102][102];
  int ws[2000], we[2000];
  i64 all_notes[10000];
  for(I=0; I<N; ++I)
  {
	  int i,n,l,h;
    scanf("%d%d%d",&n,&l,&h);
	
	for(i=0; i<n; ++i)
	{
		scanf("%d",&all_notes[i]);
	}
	
	for(i=l; i<=h; ++i)
	{
		int j;
		for( j=0; j<n; ++j)
		{
			if( all_notes[j]%i == 0 || i%all_notes[j]==0 )
				continue;
			break;
		}
		if( j==n )
			break;
	}

	int answer = -1;
	if( i<=h ) answer = i;
/*	
	i64 answer = -1;
	if ( n==1 )
	{
		// whether there exists divisor or multiple between l and h
		if( l <= all_notes[0] && all_notes[0] <= h)
		{
			answer = all_notes[0];
		}
		else
		{
			if( l > all_notes[0] )
			{
				// any multiple ?
				i64 u = l + (all_notes[0]- l%all_notes[0]);
				if ( u <= h )
					answer = u;
			}
			else // l < node
			{
				for(int i=l; i<=h; ++i)
				{
					if( all_notes[0] % i == 0 )
					{
						answer = i;
						break;
					}
				}
			}
		}
//		if( l >  )
	}
	else
	{
		i64 low = gcd( all_notes[0], all_notes[1] );
		for( i=2; i <n ;++i)
		{
			low = gcd( low, all_notes[i] );
		}
		if( l <= low && low <= h)
			answer = low;
		else if( low < l )
		{
			// may not divide all
		}
		else  // l < low
		{
			//  L < Low , get divisor of Low between L and H
			for(int i=l ; i<=h ; ++i)
				if( low%i==0 )
				{
					answer = i;
					break;
				}
		}

	}
*/	
    printf("Case #%d: ",I+1);
	if( answer == -1 )
		printf( "NO\n" );
	else
		printf("%d\n", answer);
		
  }
  return 1;
}
