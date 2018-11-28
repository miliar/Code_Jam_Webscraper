#include <cstdio>
#include <iostream>

using namespace std;

template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

int gcd(int a, int b)
{
	while ( b != 0 )
	{
		int t = b;
		b = a%b;
		a = t;
	}
	return  a;
}

// 1: win
// 0: lose
int detpos(int a, int b)
{
	if ( a > b )
		return  detpos(b, a);

	if ( a == 0 )
		return  1;

	if ( b > a*2 )
		return  1;

	return  1-detpos(b-a, a);
}

bool iswinpos(int a, int b)
{
	int  d = gcd(a, b);	
	a = a/d;
	b = b/d;

	//cout << "a=" << a << " b=" << b << endl;

	int r = detpos(a, b);
	if ( r == 1 )
		return  true;

	return  false;
}


int main()
{
	int  ncase;

	cin >> ncase;
	for(int nc=0; nc<ncase; nc++)
	{
		int  A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;

		int  sum = 0;
		for(int i=A1; i<=A2; i++)
			for(int j=B1; j<=B2; j++)
				if ( iswinpos(i,j) )
					sum ++;

		cout << "Case #" << nc+1 << ": " << sum << endl;
	}
}
