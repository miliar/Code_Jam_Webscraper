#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
using namespace std;

int gcd(int x, int y)
{
while ( y != 0 ) {
	int z = x % y;
	x = y;
	y = z;
}
return x;
}


int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");

	int C, N;
	fin >> C; 
	for (int i=1; i<=C; ++i)
	{
		fin >> N;
		set<int> s;
		for (int j=0; j<N; ++j)
		{
			int x; fin >> x;
			s.insert(x);
		}

		int ans = 0;
		if (s.size() > 1)
		{
			vector<int> v(s.begin(), s.end());
			int diff1 = v[1]-v[0];
			int diff2 = v.size() > 2 ? v[2]-v[1] : diff1;

			int g = gcd(diff1, diff2);
			int rem = v[0] % g;
			ans = (g-rem)%g;
		}
		fout << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}