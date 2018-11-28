#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define myfor(i,c,d) for( int i=(c); i<=(d); ++i )
bool seekeof( istream &fin = cin )
{
	int t;  while( (t=fin.peek())!=EOF && t<=' ' ) fin.get();
	return t==EOF ;
}

const int MAXN = 1000 ;

vector<int> a1 ;
vector<int> a2 ;

void readin()
{
	int n, x;
	
	cin>>n;

	a1.clear() ; 
	myfor( i, 1, n )
	{
		cin>>x ; 
		a1.push_back( x ) ;
	}

	a2.clear();
	myfor( i, 1, n )
	{
		cin>>x ; 
		a2.push_back( x ) ;
	}

	sort( a1.begin() , a1.end() ) ;
	sort( a2.begin() , a2.end() ) ;
}

	

void work()
{
	int ans = 0 ;
	
	while( !a1.empty() )
	{
		int end1 = a1[ a1.size()-1 ] ;
		int end2 = a2[ a2.size()-1 ] ;
		
		if( (end1) * (*a2.begin()) < 0 )
		{
			ans += (end1) * (*a2.begin()) ;
			a1.erase( a1.end()-1 ) ;
			a2.erase( a2.begin() ) ;
		}
		else if( (end2) * (*a1.begin()) < 0 )
		{
			ans += (end2) * (*a1.begin()) ;
			a2.erase( a2.end()-1 ) ;
			a1.erase( a1.begin() ) ;
		}
		else
		{
			ans += (*a1.begin()) * (end2) ;
			a1.erase( a1.begin() ) ;
			a2.erase( a2.end()-1 ) ;
		}
	}

	cout<<ans<<endl;
}


int main()
{
	freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "A-small-attempt0.out", "w", stdout );
	//freopen( "d-small.in", "r", stdin ); freopen( "d-small.out", "w", stdout );
	//freopen( "in.txt", "r", stdin );
	//freopen( "out.txt", "w", stdout );

	int test ; cin>>test ;

	myfor( i, 1, test )
	{
		cout<<"Case #"<<i<<": ";

		readin() ;
		work() ;

	}

	if( !seekeof( cin ) ) cout<<("wrong")<<endl;
	
	fclose( stdin ); fclose( stdout );
	return 0;
}
