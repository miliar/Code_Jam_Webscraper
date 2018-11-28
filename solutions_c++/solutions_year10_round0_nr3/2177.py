#include <iostream>
#include <vector>

using namespace std;

typedef unsigned int uint;

int main(){
	uint t,  r, k, n, tmp, sum, total;
	cin >> t;
	for (uint i=1; i<=t; i++){
		cin >> r >> k >> n;
		vector<uint> g;
		total = 0;
		for (uint j=0; j<n; j++){
			cin >> tmp;
			g.push_back( tmp );
		}
		uint a=0;
		for (uint j=0; j<r; j++){
			uint sum = 0;
			for (uint b=0;  b<n && sum + g[a] <= k; a=(a+1)%n, b++ ){
				sum += g[a];
			}
			//cout << "sum: " << sum << " ";
			total += sum;
		}
		cout << "Case #" << i << ": " << total << endl;
	}
}
