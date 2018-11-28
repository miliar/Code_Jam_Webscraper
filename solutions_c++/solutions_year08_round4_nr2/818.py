
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long  ll;

vector<ll> n;
string s;

double Dist(double lx, double ly, double px, double py, double len)
{
	return fabs(lx*(-py) - (-px)*ly)/len;
}

void RunTest(ifstream &in)
{
	vector<int> sets;	
	ll n, m, a;
	
	in >> n >> m >> a;	
	
	//cout << n <<  " " << m << " " << a << endl;
	//cout << endl;

	for(int j = 0; j <= m; j++)
		for(int i = 0; i <= n; i++)
		{
			double len = sqrt((double)i*i + j*j);
			if(!len)
				continue;
			double hDesired = (double)a*0.5/(len*0.5);
			//cout << len << " " << hDesired << endl;

			for(int j1 = 0; j1 <= m; j1++)
				for(int i1 = 0; i1 <= n; i1++)
				{
					double d = Dist(i, j, i1, j1, len);
					//cout << d << endl;

					if(hDesired == d)
					{
						cout << 0 << " " << 0 << " " << i << " " << j << " " << i1 << " " << j1;
						return;
					}

				}
		}
	cout << "IMPOSSIBLE";


}

int main(int argc, char* argv[])
{
	if(argc != 2)	cout << "specify input file";
	ifstream in(argv[1]);

	ll n;
	in >> n;

	for(long long i = 0; i < n; i++)
	{
		
		cout << "Case #" << (i + 1) << ": ";
		RunTest(in);
		cout << endl;
	}

	return 0;
}

