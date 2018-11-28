#include <iostream>
#include <algorithm>
#include <string>
using namespace std ;

string m[200] ;
double wp[200],owp[200],oowp[200] ;
int n,t,i,j,k ;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> t ;
	for ( int tests = 1 ; tests <= t ; ++tests ) 
	{
		cin >> n ; 
		for ( int i = 0 ; i < n ; ++i ) cin >> m[i] ; 
		memset(wp,0,sizeof wp);
		memset(owp,0,sizeof owp);
		memset(oowp,0,sizeof oowp ) ;

		for ( int i = 0 ; i < n ; ++i ) 
		{
			int tot = 0 , win = 0 ;
			for ( int j = 0 ; j < n ; ++j ) 
			{
				if ( m[i][j]!='.' ) ++tot ;
				if ( m[i][j]=='1' ) ++win ;
			}
			wp[i] = double(win)/tot ;
		}
		for ( int i = 0 ; i < n ; ++i ) 
		{
			int tot = 0 ; double twp = 0 ;
			for ( int j = 0 ; j < n ; ++j ) if ( i!=j && m[i][j]!='.' ) 
			{
				++tot ;
				int tot2 = 0 , win2 = 0 ;
				for ( int k = 0 ; k < n ; ++k ) if ( k!=i && m[j][k]!='.') 
				{
					++tot2 ;
					win2 += ( m[j][k] =='1' ) ;
				}
				twp += double(win2)/tot2 ;
			}
			owp[i] = twp / tot ;
		}
		for ( int i = 0 ; i < n ; ++i ) 
		{
			int tot = 0 ; 
			for ( int j = 0 ; j < n ; ++j ) if ( m[i][j]!='.' ) 
			{
				++tot ;
				oowp[i] += owp[j] ;
			}
			oowp[i]/=tot ;
		}

		cout << "Case #" << tests << ":" << endl ;
		for ( int i = 0 ; i < n ; ++i ) cout << wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25 << endl ;
	}
}