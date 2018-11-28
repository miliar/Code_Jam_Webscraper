#include<iostream>
#include<vector>
using namespace std;


int main(){
	int n;
	cin >> n;
	for( int i = 0; i< n; i++ ){
		int p,k,l;
		cin >> p >> k >> l;
		vector<int> v;
		int temp;
		for( int j=0; j<l; j++ ){
			cin >> temp;
			v.push_back(temp);
		}
		sort( v.begin(), v.end() );
		reverse( v.begin(), v.end() );
		
		long long int ans = 0;
		for( int j = 0;j < l; j++ ){
			ans += v[j] * (j/k + 1);
		}
		
		cout << "Case #" << (i+1) << ": " << ans << endl;
	}
}
