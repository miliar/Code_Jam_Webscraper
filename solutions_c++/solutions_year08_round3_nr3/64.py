#include <iostream>
#include <vector>
using namespace std;
vector < long long > v;
long long coun[1005] ;
long long solve()
{
	int i , j;
		for( i = 0; i < v.size() ; i ++ )
		coun[i] = 1 ;
		for( i = 0; i < v.size() ; i ++ )
		{
			for( j = i+1;j<v.size();j ++)
			{
				if( v[i] < v[j] ) coun[j] = ( coun[i] + coun[j] ) % 1000000007 ;
			}
		}
		long long sum = 0ll ;
		for( i = 0 ; i < v.size() ; i ++ )
		{
			sum = ( sum + coun[i] ) % 1000000007 ;
		}
		return sum;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	long long i  ,n , m , X , Y , Z, input[1005] , cas , test = 1;
	cin >> cas;
	while( cas-- )
	{
		v.clear();
		cin >> n >> m >> X >> Y >> Z ;
		for( i = 0; i<m; i++ ) cin>>input[i];
		for( i = 0 ; i < n ; i++ )
		{
			v.push_back ( input[i%m] ) ;
			input [ i % m ] = ( X * input[i%m] + Y * (i + 1) ) % Z;
		}
		cout<< "Case #" << test ++ << ": " << solve() << endl;
	}
	return 0;
}

