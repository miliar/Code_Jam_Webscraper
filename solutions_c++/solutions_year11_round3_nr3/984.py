#include<iostream>
#include<string>
#include<vector>



using namespace std;


int main()
{
	freopen( "data_in.txt" , "r" , stdin );

	freopen( "data_out.txt" , "w" , stdout );


	int T;

	cin >> T;

	for( int t = 1 ; t <= T ; t ++ )
	{

		cout << "Case #" << t << ": ";

		
		int N , L , H;

		cin >> N >> L >> H;

		int* f = new int[ N ];

		for( int n = 0 ; n < N ; n ++ )
			cin >> f[ n ];

		bool flag = false;
		int vv;
		for( int v = L ; v <= H ; v ++ )
		{
			for( int n = 0 ; n < N ; n ++ )
			{
				if( f[ n ] % v == 0 || v % f[ n ] == 0 )
				{
					vv = v; 
					flag = true;
				}
				else
				{
					flag = false;
					break;
				}
			}
			if( flag )
				break;
		}
		if( !flag )
			cout << "NO\n";
		else
			cout << vv << "\n";
	}
	return 0;
}