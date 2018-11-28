# include <stdio.h>
# include <vector>
# include <stdlib.h>
using namespace std;

vector < pair < char , int > > v ;
vector < pair < char , int > > O ;
vector < pair < char , int > > B ;

int main ()
{
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int tc ; 
	scanf ("%d",&tc);
	for ( int k=1 ; k<=tc ; k++ )
	{
		int n ;
		scanf ("%d\n",&n);
		O.clear();
		v.clear();
		B.clear();
		for ( int i=0 ; i<n ; i++ )
		{
			char c ;
			int l ;
			scanf ("%c%d\n",&c,&l);
			v.push_back ( make_pair ( c, l ) ) ;
			if ( c == 'O' )
				O.push_back ( make_pair(c,l) ) ;
			else
				B.push_back ( make_pair(c,l) ) ;
		}
		int O_pos=1 , B_pos=1 , ret=0;
		for ( int i=0 ; i<v.size() ; i++ )
		{
			if ( v[i].first == 'O' )
			{
				int x = abs ( O[0].second - O_pos ) ;
				O_pos = O[0].second ;
				ret += (x+1) ;
				O.erase(O.begin()+0);
				if ( B.size() )
				{
					if ( abs (B[0].second - B_pos) <= x+1 )
						B_pos = B[0].second;
					else
						B_pos += B_pos>B[0].second? -(x+1) : x+1 ;
				}
			}
			else
			{
				int x = abs ( B[0].second - B_pos ) ;
				B_pos = B[0].second ;
				ret += (x+1) ;
				B.erase(B.begin()+0);
				if ( O.size() )
				{
					if ( abs (O[0].second - O_pos) <= x+1 )
						O_pos = O[0].second;
					else
						O_pos += O_pos>O[0].second? -(x+1) : x+1 ;
				}
			}
		}
		printf ("Case #%d: %d\n",k,ret);
	}
	//while(1);
}