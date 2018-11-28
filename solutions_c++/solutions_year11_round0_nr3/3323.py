#include <iostream>
using namespace std;
#include <vector>

bool checkBin1( unsigned int num, int no){
	unsigned int checker = ( 1<< no);
	return (num&checker);
}

int main(){

	int n;
	cin >> n;
	for( int i =0 ; i < n ; i++){
		int max = 0;
		int m;
		cin>> m;
		vector<unsigned int> candy;
		candy.clear();
		for( int i1 =0 ; i1 < m ; i1++){
			unsigned int k;
			cin >> k;
			candy.push_back(k);
		}
		for(unsigned int num = 1; num< (1<<m)-1; num++){
			unsigned int sum1 = 0;
			unsigned int sum2 = 0;
			for(int i1 = 0 ; i1 < m; i1++)
				if( checkBin1(num,i1) )
					sum1 ^= candy[i1];
				else
					sum2 ^= candy[i1];
			if (sum1 == sum2){
				int realsum1=0;
				int realsum2=0;
				for(int i1 = 0 ; i1 < m; i1++)
					if( checkBin1(num,i1) )
						realsum1 += candy[i1];
					else
						realsum2 += candy[i1];
				if( realsum1 > max ) max = realsum1;
				if( realsum2 > max ) max = realsum2;
			}

		}
		cout << "Case #" << i+1 << ": ";
		if( max > 0 )
			cout << max << endl;
		else
			cout << " NO" << endl;
	}

}
