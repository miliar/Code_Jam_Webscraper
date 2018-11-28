#include <iostream>
#include <vector>
using std::cerr;
using std::cout;
using std::cin;
using std::vector;

typedef vector<int> VI;
int sean(int mask, const VI & a)
{
	int r = 0;
	for(int i =0 ; i < a.size(); i++)
	{
		if( (1<<i) & mask) 
			r+= a[i];
	}
	return r;
}

int pat(int mask, const VI & a, bool t)
{
	int r = 0;
	for(int i =a.size()-1 ; i >=0; i--)
	{
		cerr << t << " pat  " << r << ' ' <<  a[i] << '\n';
		int lmask = 1<<i;
		cerr << mask << ' ' << lmask << "\n";
		if(t)
		{
			if( lmask & mask)
			{
				cerr << "adding " << a[i] << " => ";
				r^= a[i];
			}
		}
		else
		{
			if( ! (lmask & mask) )
			{
				cerr << "adding " << a[i] << " => ";
				r^= a[i];
			}
		}
		cerr << r << "\n";
	}
	return r;
}

int work(int mask, const VI & a)
{
	int x = pat(mask, a, true);
	int y = pat(mask, a, false);
	int z = -1;
	if((x == y) && (x !=0 ))
	{
		z = sean(mask, a);
	}
	cerr << "## " << mask << ' ' << x << ' ' << y << ' ' << z << "\n";
	return z;
}


int main()
{
	int tc_count;
	cin >> tc_count;
	for(int tc_index=1; tc_index <= tc_count; tc_index++)
	{
		cerr << "------------------\n";
		int n;
		cin >> n;

		VI a(n);
		for(int i =0; i < n; i++)
		{
			cin >> a[i];
		}

		int r  = -1;
		for(int i =0; i < (1<<n); i++)
		{
			int t = work(i, a);
			if(t > r)
				r = t;
		}

		if(r != -1)
		cout << "Case #" << tc_index <<  ": " 
		<< r
		<< "\n";
		else
		cout << "Case #" << tc_index <<  ": " 
		<< "NO"
		<< "\n";
	}
	return 0;
}
