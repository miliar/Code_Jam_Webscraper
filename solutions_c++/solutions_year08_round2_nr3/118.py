#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <cmath>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifs("c.in");
	ofstream ofs("c.out");
	int t;
	ifs >> t;
	for (int l = 0; l < t; ++l)
	{
		int n, k;
		ifs >> n >> k;

		vector<int> d(k, 0);
		for (int i = 0; i < k; ++i)
			ifs >> d[i];
		vector<int> pos(n, 0);
		for (int i= 0; i < n; ++i)
			pos[i] = i;
		vector<int> o(n, 0);
		int p = 0;
		for (int i = 0; i < n; ++i)
		{
			int nextp = (p+i) % pos.size();
			o[pos[nextp]] = i;
			pos.erase(pos.begin()+nextp);
			p = nextp;
		}
		ofs << "Case #" << l+1 << ":";  
		for (int i= 0; i < k; ++i)
			ofs << ' ' << o[d[i]-1]+1;
		ofs << endl;

	}

  	return 0;
}
