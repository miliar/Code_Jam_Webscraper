#include<iostream>
#include<cmath>
#include<map>
#include<vector>
#include<sstream>
using namespace std;

struct PLANT
{
	int x,y,r;
	PLANT(int X, int Y, int R) : x(X), y(Y), r(R) {};
};
int main()
{
	int T;
	cin >> T;
	string line;
	getline( cin, line );
	for( int t = 0; t < T; t++ )
	{
		int N;
		cin >> N;
		vector<PLANT> v;
		for( int n = 0; n < N; n++ )
		{
			int X, Y, R;
			cin >> X >> Y >> R;
			v.push_back(PLANT(X,Y,R)); 
		}

		long long c = 1;
		for( int n = 0; n < N; n++ )
		{
			c <<= 1;
		}

		/*
		vector<PLANT> s1;
		vector<PLANT> s2;
		for( int i = 0; i < c; i++ )
		{
			for( int n = 0; n < N; n++ )
			{
				if( ((i >> n) & 0x1) == 0x01 )
				{
					s1.push_back(v[n]);
				}
				else
				{
					s2.push_back(v[n]);
				}
			}
		}
		*/
		double ans = 0;
		if( N == 1 )
		{
			ans = v[0].r;
		}
		else if ( N == 2 )
		{
			ans = v[1].r > v[0].r ? v[1].r : v[0].r;
		}
		else if( N == 3 )
		{
			vector<double> w;
			ans = 1e100;
#define A(X,Y) ((sqrt( (v[X].x - v[Y].x) * (v[X].x - v[Y].x) + (v[X].y - v[Y].y) * (v[X].y - v[Y].y) ) + v[X].r + v[Y].r )/2)
			w.push_back( A(0,1) );
			w.push_back( A(1,2) );
			w.push_back( A(0,2) );
			for( int i = 0; i < 3; i++ )
			{
				ans = ans < w[i] ? ans : w[i];
			}
		}
		else
		{
			cout << "error!" << endl;
		}
		printf( "Case #%d: %.7lf\n", (t+1), ans );
	}
}
