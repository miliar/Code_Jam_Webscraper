#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for( int j = 1; j <= t; j++ ){
	cout<<"Case #"<<j<<": ";
	int n;
	int x = 0;
	cin>>n;
	int a[ n ];
	for( int i = 0; i < n; i++ )
	cin>>a[ i ];
	//for( int i = 0; i < n; i++ )
	//cout<<a[ i ]<<"\t";
	//cout<<endl;
	for( int i = 0; i < n; i++ )
	x = (x ^ a[ i ]);
	if( x != 0 )
	cout<<"NO"<<endl;
	else
	{
		int min = a[ 0 ];
		int sum = 0;
		for( int i = 0; i < n; i++ )
		{
			if( a[ i ] < min )
			min = a[ i ];
			sum = sum + a[ i ];
		}
		sum = sum - min;
		cout<<sum<<endl;
	}
	}
	return 0;
}
