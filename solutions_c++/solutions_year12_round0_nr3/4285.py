#include <stdio.h>

#include <map>
#include <set>
using namespace std;

typedef set<int> SmallSet;
typedef map<int, SmallSet > BigMap;
BigMap gmap;

void preproc()
{
	for(int i=10; i<1000; ++i)
	{
		int lg = 10, loop = 1;
		     if( i>=1000000 ) { lg = 1000000; loop = 6; }
		else if( i>=100000 ) { lg = 100000; loop = 5; }
		else if( i>=10000 ) { lg = 10000; loop = 4; }
		else if( i>=1000 ) { lg = 1000; loop = 3; }
		else if( i>=100 ) { lg = 100; loop = 2; }
		int t= i;
		while(loop-->0)
		{
			t = t/10 + (t%10) * lg;
			if( t > i )
			{
//				printf("%d->%d\n", i, t );
				BigMap::iterator it = gmap.find(i);
				if( it == gmap.end() )
				{
					SmallSet s;
					s.insert(t);
					gmap.insert( BigMap::value_type(i, s) );
				}
				else
				{
					it->second.insert(t);
				}
			}
		}
	}
}

int main(int argc, char* argv[])
{
	preproc();

	int N;
	scanf("%d",&N);
	char ch[1025];
	gets(ch);
	for(int I=0; I<N; ++I)
	{
		int A, B;
		int x = 0;
		scanf("%d%d",&A,&B);
		for( BigMap::iterator min = gmap.lower_bound(A); min != gmap.end(); ++min )
		{
			if( min->first > B )
				break;
			for( SmallSet::iterator it = min->second.begin(); it != min->second.end(); ++it )
			{
				if( *it > B )
					break;
				++x;
			}
		}
		printf("Case #%d: %d\n", I+1, x);
	}
	return 0;
}


