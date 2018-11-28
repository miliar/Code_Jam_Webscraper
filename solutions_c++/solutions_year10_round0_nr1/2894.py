#include <iostream>
#include <cmath>
#define fori(N) for(int i=0;i<N;i++)

using namespace std;

int main()
{
	int t;
	long x, y, a;

	cin >> t;

	fori(t)
	{
		cin >> x >> y;

		a=(int)pow(2.0,x)-1;

		cout << "Case #"<<i+1<<": ";

		if((y&a)==a)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl; 
	}

	return 0;
}