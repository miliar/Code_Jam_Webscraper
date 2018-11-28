#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;
ifstream fin("C:\\Users\\Edward\\C-large.in");
ofstream fout("C:\\Users\\Edward\\A-small-attempt1.out");
 
#define cin fin
#define cout fout
int main()
{
	int t , n;
	int i , a , sum , _min;
	int ans , num;
	cin>>t;
	num = 0;
	while( t-- )
	{
		++num;
		cin>>n;
		sum = 0;
		_min = 9999999;
		ans = 0;
		for( i = 0 ; i < n ; ++i )
		{ 
			cin>>a; sum += a; if( _min > a ){ _min = a; } 
			ans ^= a;
		}
		if( ans ){ cout<<"Case #"<<num<<": NO"<<endl; }
		else
		{
			cout<<"Case #"<<num<<": "<<sum - _min<<endl;
		}
		
	}
	return 0;
}