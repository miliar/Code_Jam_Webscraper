// QR.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <vector>
using namespace std;



int main(int argc, char* argv[ ] )
{
	freopen( "A.in", "rt", stdin );
	freopen( "A.out", "wt", stdout );

	int T = 0;
	cin >> T;

	for( int ct = 0; ct < T; ++ct )
	{
		int N = 0, K = 0;
		cin >> N >> K;

		//while ( K > 0 )
		//{
		//	K -= ( 1 << N );
		//}

		int pn = 1 << N;


		cout << "Case #" << ct + 1 << ": ";

		if( K > 0 && ( K + 1 ) % pn == 0 )
		{
			cout << "ON";
		}
		else
		{
			cout << "OFF";
		}
		cout << endl;
	}
	
	return 0;
}

