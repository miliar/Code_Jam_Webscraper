#include <fstream>
#include <iostream>

bool test(unsigned K, unsigned N) {
	bool * snapchain = new bool[N] ;
	for(unsigned i=0;i<N;i++) snapchain[i] = false ;

	for(unsigned j=0;j<K;j++) {
		for(unsigned i=0;i<N;i++) {
			if( snapchain[i] ) snapchain[i] = false ;
			else { snapchain[i] = true; break; }
		}

	}

	for(unsigned i=0;i<N;i++) {
		if( !snapchain[i] ) return false ;
	}

	return true ;
}

int main(int argc, char **argv ) {
	using namespace std;

	fstream file(argv[1]) ;
	ofstream out("result.txt");

	unsigned number ;
	file.setf( file.skipws ) ;
	file >> number ;

	for(unsigned i=0;i<number;i++) {
		unsigned k,n ;
		file >> n >> k ;

//		cout << i << ":   k=" << k << "  n=" << n << endl ;
		out << "Case #" << i+1 << ": " << (test(k,n)?"ON":"OFF") << endl ;
	}

	system("pause");

	return 0;
}