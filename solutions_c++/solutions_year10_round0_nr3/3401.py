#include<iostream>

using namespace std;

typedef unsigned long long int uint;

uint theme( int R, int k, int N, uint *g ) {

	uint  euros  =0;
	uint  start  =0;
	uint  current=0;
	uint  load   =0;
	bool  allin  =false;

	uint  *data = new uint[N];
	uint  *next = new uint[N];
	
	for( int r = 0 ; r < R ; r++ )
	{

		if( data[start] == 0 )
		{
			while(!allin && load+g[current]<=k)
			{
				load   += g[current];
				current = (current + 1)%N;
				allin   = (current == start);
			}
			data[start] = load;
			next[start] = current;
		}
		else {
			load    = data[start];
			current = next[start];
		}

		euros += load;
		load   = 0;
		start  = current;
		allin  = false;

	}

	delete[] next;
	delete[] data;
	return euros;

}

int main() {
	
	int T   = 3;
	int R   = 5;
	int k   = 5;
	int N   = 10;
	uint *g  = NULL;

	cin  >> T;

	for( int c = 0 ; c < T ; c++ )
	{
		cin  >> R >> k >> N;
		g = new uint[N];

		for( int i = 0 ; i < N ; i++ )
			cin >> g[i];

		cout << "Case #" << c+1 << ": " << theme( R, k, N, g ) << endl;

		delete[] g;
	}

	return 0;
}

