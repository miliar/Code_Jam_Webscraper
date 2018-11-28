#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	long long T, L, C, P;
	fin >> T; 
	for (int z=1; z<=T; ++z)
	{
		fin >> L >> P >> C;

		int ans = 0;
		if (L*C >= P)
			ans = 0;
		else if (L*C*C >= P)
			ans = 1;
		else
		{
			int locs = 0;
			while (L*C < P)
			{
				L *= C;
				++locs;
			}
			ans = 1;
			long long maxNum = 2;
			while (locs >= maxNum)
			{
				maxNum *= 2;
				++ans;
			}
		}
		
		fout << "Case #" << z << ": " << ans << endl;
	}

	return 0;
}