#include <iostream>
#include <fstream>
#include <stdint.h>

using namespace std;

uint32_t split( int n, uint32_t * a ){
	uint32_t b1 = 0, small=a[0], total=0;
	for( int i = 0; i < n; i++) {
		b1 ^= a[i];
		total += a[i];
		if (small > a[i])
			small = a[i];
	}
	if (b1 != 0)
		return -1;

	return total - small;
}

int main(int argc, char * argv [] ) {
	if (argc < 2) {
		cout << "Enter input name" <<endl;
		return 0;
	}

	ifstream input(argv[1]);
	int problem_count;
	input >> problem_count;

	for (int p = 1; p <= problem_count; p++){
		int bag_count;
		input >> bag_count;
		uint32_t * bag = new uint32_t[bag_count];

		for (int i = 0; i < bag_count; i++)
			input >> bag[i] ;

		int32_t ans = split( bag_count, bag );
		
		cout <<"Case #" << p <<": ";
		if ( ans == -1 )
			cout << "NO\n";
		else
			cout << ans << "\n";

		delete [] bag;
	}

	input.close();
	return 0;
}



