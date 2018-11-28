#include <iostream>
#include <vector>
#include <map>
#include <assert.h>
using namespace std;

class CSolver {
public:
	CSolver() { n = 0; periodSize = 0; }
	CSolver( int n );
	bool IsLightOn( int k );
private:
	int n;
	int periodSize;
	void initialize();
};

bool CSolver::IsLightOn( int k )
{
	assert( periodSize > 0 );
	return k % periodSize == periodSize - 1;
}

CSolver::CSolver( int _n ) :
	n( _n )
{
	vector<bool> snappers( n, false );
	int iteration = 0;
	int lastPowered = 0; // index of last powered snapper
	do {
		iteration++;
		lastPowered = 0;
		while( lastPowered < n && snappers[lastPowered] ) {
			snappers[lastPowered] = false;
			lastPowered++;
		}
		if( lastPowered < n ) {
			snappers[lastPowered] = true;
		}
	} while( lastPowered < n );
	periodSize = iteration;
	assert( periodSize > 0 );
}

int main()
{
	int nCases = 0;
	map<int, CSolver> solvers;

	cin >> nCases;
	vector<bool> results;
	for( int i = 0; i < nCases; i++ ) {
		long int n, k;
		cin >> n >> k;
		if( solvers.find( n ) == solvers.end() ) {
			solvers[n] = CSolver( n );
		}
		results.push_back( solvers[n].IsLightOn( k ) );
	}
	for( int i = 0; i < nCases; i++ ) {
		if( results[i] ) {
			cout << "Case #" << i + 1 << ": ON" << endl;
		} else {
			cout << "Case #" << i + 1 << ": OFF" << endl;
		}
	}
}