#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	int number;
	cin >> n;
	vector<int> v;
	int temp;
	int val;
	
	for ( int i = 0 ; i < n ; i++ ) {
	
		vector<int> a(1001);
		vector<int> b(1001);
		vector<int> c(1001);
		bool check = false;
		
		cin >> number;
		for ( int  j = 0 ; j < number ; j++ ) {
			cin >> temp;
			v.push_back( temp );
		}
		
		sort( v.begin(), v.end() );
		
		val = 0; 
		for ( int k = 0 ; k < number-1 ; k++ ) {
			a[k+1] = a[k] ^ v[k];
		}
		
		val = 0;
		
		for ( int k = number-1; k > 0 ; k-- ) {
			b[k-1] =  b[k] ^ v[k];
			c[k-1] = c[k] + v[k];
		}
		
		for ( int k = 0 ; k < number-1 ; k++ ) {
			if ( b[k] == a[k+1] ) {
				cout << "Case #"<< i+1 <<": "<< c[k] << endl;
				check = true;
				break;
			}
		}
		if ( check == false ) {
			cout << "Case #"<<i+1<<": NO"<< endl;
		}
		
		v.erase ( v.begin(), v.end() );
	}
				
	return 0;
}			
				
				
				
				
				
	
