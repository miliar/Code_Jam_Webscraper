#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int gcd(unsigned int a,unsigned int b )
{
	unsigned temp = a;
	if( a < b ) 
	{
		a = b;
		b = temp;
	}
	if( !(a % b) ) return b;
	else gcd(b, a%b);
}
int main()
{
	vector < unsigned int > a;
	set <unsigned int > s;
	unsigned int input;
	int t, n;
	unsigned int result = 0;

//	FILE *fin = freopen("a.in", "r", stdin);
//	FILE *fout = fopen("a.out", "w");
	cin >> t;

	for(int i=1; i<= t; ++i )
	{
		cin >> n;

		for( int j=0; j<n;++j)
		{
			cin >> input;
			if( s.find(input) == s.end() )
			{
				a.push_back(input);
				s.insert(input);
			}
		}

		sort(a.begin(), a.end());

		unsigned int ngcd;
		if( a.size() == 2 )
			ngcd = a[1] - a[0];
		else
			ngcd = gcd(a[1]-a[0], a[2] - a[1] );

		for( int m = 1;; ++m )
		{
			result = m*ngcd;
			if( result >= a[0] )
				break;
		}

		result -= a[0];
		cout << "Case #" << i << ": " << result << endl;

	//	fprintf(fout, "Case #%d: %u\n", i, result);

		a.clear(); s.clear();
	}
	return 0;
}