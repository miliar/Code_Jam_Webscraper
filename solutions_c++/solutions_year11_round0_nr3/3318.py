#include <iostream>
using namespace std;
#include <vector>

int main(){

	int n;
	cin >> n;
	for( int i =0 ; i < n ; i++){
		int max = 0;
		int m;
		cin>> m;
		vector< int> cvalues;
		cvalues.clear();
		for( int i1 =0 ; i1 < m ; i1++){
			 int k;
			cin >> k;
			cvalues.push_back(k);
		}
		for( int num = 1; num< (1<<m)-1; num++){
			 int childadd1 = 0;
			 int childadd2 = 0;
			for(int i1 = 0 ; i1 < m; i1++)
				if( num&(1<<i1) )
					childadd1 ^= cvalues[i1];
				else
					childadd2 ^= cvalues[i1];
			if (childadd1 == childadd2){
				int realadd1=0;
				int realadd2=0;
				for(int i1 = 0 ; i1 < m; i1++)
					if( num&(1<<i1) )
						realadd1 += cvalues[i1];
					else
						realadd2 += cvalues[i1];
				if( realadd1 > max ) max = realadd1;
				if( realadd2 > max ) max = realadd2;
			}

		}
		cout << "Case #" << i+1 << ": ";
		if( max > 0 )
			cout << max << endl;
		else
			cout << " NO" << endl;
	}

}
