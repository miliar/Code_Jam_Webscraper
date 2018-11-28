#include <iostream>
#include <vector>
#include <string>
using std::string;
using std::cout;
using std::cin;
using std::cerr;
using std::vector;

typedef vector<char> VI;
typedef vector<VI> VVI;

typedef vector<double> VVD;

int n;

double ws(int x, const VVI & a)
{
	double gp = 0, w = 0;
	for(int i =0; i < n; i++)
	{
		if(a[x][i] != '.')
		{
			gp++;
			w += (a[x][i] == '1');
		}
	}
	return w/gp;
}

double ews(int x, int ex, const VVI & a)
{
//	cerr << x<< '-' << ex << "\n";
	double gp = 0, w = 0;
	for(int i =0; i < n; i++)
	{
		if(i == ex)
			continue;
		if(a[x][i] != '.')
		{
			gp++;
			w += (a[x][i] == '1');
		}
	}
	return w/gp;
}

double os(int x, const VVI & a, VVD & cache)
{
	if(cache[x] < 0)
	{
		double wp = 0, gp=0;
		for(int i =0; i < n; i++)
		{
			if(a[x][i] == '.')
				continue;

			gp++;
			double t =  ews(i, x, a);
	//		cerr << x << ": " << t << "\n";
			wp += t;
		}
		cache[x] = wp/gp;
	}
	return cache[x];
}

double oos(int x, const VVI & a, VVD & cache)
{
	double wp = 0, gp=0;
	for(int i =0; i < n; i++)
	{
		if(a[x][i] == '.')
			continue;

		gp++;
		wp += os(i, a, cache);
	}
	return wp/gp;
}

int main()
{
	cout.precision(15);
	int tc_count;
	cin >> tc_count;
	for(int tc_index=1; tc_index <= tc_count; tc_index++)
	{
//		cerr << "-------------------------------\n\n\n";
		cin >> n;
	
		VVI a(n, VI(n));

		for(int i =0; i < n; i++)
			for(int j =0; j < n; j++)
			{
				cin >> a[i][j];
			}

		 VVD os_cache(n, -1.0);


		cout << "Case #" << tc_index <<  ":\n";
		for(int i =0; i < n; i++)
		{
			double WP = ws(i, a);
			double OWP = os(i, a, os_cache);
			double OOWP = oos(i, a, os_cache);
//			double OOWP = 0;
//			cerr << "\n" << WP << " -- " << OWP << " -- " << OOWP << "\n";
			double ans = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
			cout <<  ans << "\n";
		}
	}
	return 0;
}
