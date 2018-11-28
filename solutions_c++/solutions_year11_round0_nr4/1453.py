// my first program in C++

#include <iostream>
using namespace std;

int main()
{
	int k;
	cin >> k;
	for( int i=0; i<k; ++i ) {
		int n, correct=0;
		cin >> n;
		for( int j=0; j<n; ++j ) {
			int val;
			cin >> val;
			if( val == (j+1) ) correct++;
		}
		cout << "Case #" << (i+1) <<": "<<(n-correct)<<"\n";
		/* 		int sum=0, n, min=9999999, x=0;
				cin >> n;
				for( int j=0; j<n; ++j ) {
					int cur;
					cin >> cur;
					x ^= cur;
					sum += cur;
					if(min > cur) min = cur;
				}
				if(x == 0)cout << "Case #" << (i+1) <<": "<<(sum-min)<<"\n";
				else cout << "Case #" << (i+1) <<": NO\n"; */
	}
	return 0;
}
