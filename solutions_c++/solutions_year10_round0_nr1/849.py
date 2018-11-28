#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;  cin >> T;

	for ( int t=1; t<=T; t++ )
	{
		int N, K;
		cin >> N >> K;

		//vector<bool> snap( N );

		//for ( int k=0; k<K; k++ )
		//{
		//	for ( int i=0; i<N; i++ )
		//	{
		//		snap[i] = ! snap[i];

		//		if ( snap[i] )
		//			break;
		//	}

		//	for ( int i=0; i<N; i++ )
		//		cout << ( snap[i] ? "o" : "x" );
		//	cout << endl;
		//}

		//bool f = true;
		//for ( int i=0; i<N; i++ )
		//	if ( ! snap[i] )
		//		f = false;

		//cout << "Case #" << t << ": " << ( f ? "ON" : "OFF" ) << endl;

		int f = ( 1 << N ) - 1;

		cout <<
			"Case #" << t << ": " <<
			( (K&f) == f ? "ON" : "OFF" ) << endl;
	}

	return 0;
}




