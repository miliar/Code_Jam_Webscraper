#include <iostream>
#include <set>
#include <fstream>
using namespace std;

int t10[8], test, cnt = 1, A, B;
ifstream fin( "C.in" );
ofstream fout( "C.out" );
#define cin fin
#define cout fout

int main()
{
	t10[0] = 1;
	for( int i = 1; i < 8; i++ )
		t10[i] = 10 * t10[i - 1];
	for( cin >> test; test--; ){
		cin >> A >> B;
		int res = 0;
		for( int num = A; num < B; num++ ){
			int dig[8] = {0}, ptr = 7, temp = num, right = 0, left = num;
			set< int > st;
			while( temp )
				dig[ptr--] = temp % 10, temp /= 10;
			for( int i = 7; i > ptr; i-- ){
				right += dig[i] * t10[7 - i];
				left /= 10;
				if( dig[i] == 0 )
					continue;
				//cout<< left << ' ' << right << endl;
				int nnum = right * t10[i - ptr - 1] + left;
				//cout << "HERE " << num << ' ' << nnum << endl;
				if( nnum > num && nnum <= B && !st.count( nnum ) )
					res++, st.insert( nnum );
			}
		}
		cout << "Case #" << cnt++ << ": " << res << endl;
	}
	return 0;
}