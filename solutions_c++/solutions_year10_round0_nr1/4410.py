#include <iostream>

using namespace std;

int main()
	{
	int t;
	cin >> t;
	for(int c = 1 ; c <=t;++c)
	{
		int n , k;
		cin >> n >> k;
		bool *snap = new bool[n];
		for(int i=0;i<n;++i)
			snap[i] = false;
		//snap[0] = !snap[0];
		
		//if(!snap[0]
	for(int flip =0; flip<k;++flip)
{
		for( int m =0 ; m<n;++m)
		{
			if(snap[m])
				snap[m] = !snap[m];
			else
			{
				snap[m] = !snap[m];
				break;
			}
		}
}
		bool on=true;;
		for(int i=0;i<n;++i)
			if(!snap[i])
				on = false;
		if(on)
			cout << "Case #" << c << ": " << "ON" << endl;
		else
			cout << "Case #" << c << ": " << "OFF" << endl;
	}
}
