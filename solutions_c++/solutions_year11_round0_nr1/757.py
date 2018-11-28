#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int main ()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int t;
	cin >> t;

	for ( int tt = 1 ; tt <= t ; tt++)
	{
		// time, pos
		pair <int,int> o(0,1),b(0,1);
		//vector<pair<char, int> > moves;

		int n,pos;
		char ch;
		cin >> n;
		while (n--)
		{
			cin >> ch >> pos;
			if ( ch == 'O')
			{
				int dif = abs ( pos - o.second );
				int nt = o.first + dif;
				o.first = max ( nt, b.first) + 1;
				o.second = pos;
				//b.first = o.first;
			}
			else
			{
				int dif = abs ( pos - b.second );
				int nt = b.first + dif;
				b.first = max ( nt, o.first) +1;
				b.second = pos;
				//o.first = b.first;
			}
		}


		cout << "Case #"<<tt<<": "<< max (o.first,b.first) << endl;


	}
	return 0;
}
