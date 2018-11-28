#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	
	for ( int testCase = 1; testCase <= T; testCase += 1 ) {
		string number;
		cin >> number;
		
		bool ok = next_permutation( number.begin(), number.end() );
		
		if ( ok )
			cout << "Case #" << testCase << ": " << number << endl;
		else
		{
			int i = 0;
			while ( number[i] == '0' )
				i += 1;
			
			char tmp = number[i];
			number[i] = '0';
			number[0] = tmp;
			number.insert(1, "0");
			
			cout << "Case #" << testCase << ": " << number << endl;
		}
	}
}

