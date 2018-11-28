#include <iostream>
#include <cstdio>

using namespace std;

int f(int x)
{
	if ( x < 100 )
		return 10;
	else if ( x < 1000 )
		return 100;
	else return 1000;
}

int func(int x,int y)
{
	if ( y < 10 )
		return 0;
	else 
	{
		int count = 0;
		for ( int i = x ; i <= y ; ++i )
		{
			int number = i;
			int end = number % 10;
			number = end * f(number) + number/10;

			if ( number > i && number <= y ) ++count;

			number = i;
			end = number % 100;
			number = end * (f(number) / 10) + number / 100;
			if ( number > i && number <= y ) ++count;

			number = i;
			end = number % 1000;
			number = end * (f(number) / 100) + number / 1000;

			if ( number > i && number <= y ) ++count;
		}
		return count;
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int t; cin >> t;

	for ( int i = 0 ; i < t ; ++i )
	{
		int a,b; cin >> a >> b;
		cout << "Case #" << i + 1 << ": " << func(a,b) << endl;
	}

	return 0;
}
