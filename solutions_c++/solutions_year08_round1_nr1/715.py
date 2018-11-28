#include<iostream>
#include<vector>
using namespace std;

int main(){
	int t;
	cin >> t;
	for( int m=0; m<t; m++ ){
		int n;
		cin >> n;

		vector<int> v1;
		for( int i = 0; i < n; i++ ){
			int temp;
			cin >> temp;
			v1.push_back(temp);
		}
		vector<int> v2;
		for( int i = 0; i < n; i++ ){
			int temp;
			cin >> temp;
			v2.push_back(temp);
		}

		sort( v1.begin(), v1.end() );
		sort( v2.begin(), v2.end() );
		reverse( v1.begin(), v1.end() );

		long long product = 0;
		for( int i = 0; i < n; i++ ){
			product += v1[i] * v2[i];
		}

		cout << "Case #" << (m+1) << ": " << product << endl;
	}
}
