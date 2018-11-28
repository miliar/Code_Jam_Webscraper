#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream f("c.in");
	ofstream f2("c.out");

	int T;
	f>>T;
	
	for(int testcase = 1; testcase <= T; ++testcase)
	{
		int nr;
		f>>nr;
		vector<long long> v;
		v.assign(nr, 0);
		
		for(int i = 0; i<nr; ++i)
		{
			f>>v[i];
		}

		long long minim = v[0];
		long long xor = v[0];
		long long sum = v[0];
		for(int i = 1; i<v.size(); ++i)
		{
			if(v[i] < minim)
				minim = v[i];
			xor ^= v[i];
			sum += v[i];
		}

		f2<<"Case #" << testcase << ": ";
		if(xor != 0)
			f2<<"NO\n";
		else
			f2<<sum - minim<<"\n";
	}

	return 0;
}