#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<map>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int T ; 
	scanf ( "%d",&T);
	int K = T ; 
	while(T--)
	{
		int N ; 
		scanf ( "%d",&N ) ;
		vector<pii> X;
		X.resize(N);
		for ( int i = 0; i < N ; i ++ ) cin>> X [ i].first  >> X  [i ].second ; 
		sort (X.begin () , X.end () ); 
		ll k = 0 ;
		for ( int i = 0 ; i < N ; i ++) 
		{
			for ( int j = i + 1; j < N ; j ++) 
			  if( X [ j ].second < X [ i ].second )  k ++ ; 
		}
		
		
		printf( "Case #%d: ",K-T);
		cout <<k<<"\n";
	}	

}
