#include <iostream>
#include <cmath>

using namespace std;

bool check( int A, int B )
{
	if ( A > B )
		swap( A, B );
	for ( int k=1; A*k<B; k++ )
		if ( ! check( A, B-k*A ) )
			return true;

	return false;
}

int main()
{
	int T;  cin >> T;
	for ( int t=0; t<T; t++ )
	{
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;

		long long y = 0;
		for ( int a=A1; a<=A2; a++ )
		{
			int b1 = (int)(a/(1+sqrt(5.0))*2)+1;
			int b2 = (int)(a*(1+sqrt(5.0))/2);

			y += (B2-B1+1) - max( 0, min(b2,B2) - max(b1,B1) + 1 );
		}

		cout << "Case #" << (t+1) << ": " << y << endl;
	}

	//for ( int a=1; a<=6; a++ )
	//{
	//	for ( int b=1; b<=6; b++ )
	//		//cout << "(" << a << "," << b << ")" << (check(a,b)?"o":"x") << " " << endl;
	//		cout << (check(a,b)?"o":"x");

	//	cout << " " << (int)(a/(1+sqrt(5.0))*2)+1 << "," << (int)(a*(1+sqrt(5.0))/2);
	//	cout << endl;

	//	//int b;
	//	//for ( b=1; ; b++ )
	//	//	if ( ! check(a,b) )
	//	//		break;
	//	////cout << a << "," << b-1 << endl;

	//	////b = (int)(a*(1+sqrt(5.0))/2)+1;
	//	////b = (int)(a/(1+sqrt(5.0))*2)+1;

	//	//cout<< " " << b;

	//}

	return 0;
}