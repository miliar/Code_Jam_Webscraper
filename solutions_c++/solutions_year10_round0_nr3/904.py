#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

typedef unsigned long long ll;

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	int T;
	fin >> T; 
	for (int z=1; z<=T; ++z)
	{
		ll R, k, N, tot(0), res(0);
		fin >> R >> k >> N;
		vector<ll> g((int)N);
		for (int i=0; i<N; ++i)
		{
			ll next; fin >> next;
			g[i] = next;
			tot += next;
		}
		if (tot <= k)
		{
			fout << "Case #" << z << ": " << (tot*R) << endl;
			continue;
		}

		bool usedMap = false;
		int loc = 0;
		map<int, pair<ll, ll>> mp;
		mp[0] = make_pair(0,0);
		for (ll j=1; j<=R; ++j)
		{
			tot = 0;
			while (g[loc] + tot <= k)
				tot += g[loc], loc = (loc+1)%N;
			res += tot;

			map<int, pair<ll, ll>>::const_iterator it = mp.find(loc);
			if (!usedMap && it != mp.end())
			{
				ll diff = res - it->second.second, time = j - it->second.first;
				ll toAdd = (R>=(1+j) ? R-1-j : 0) / time;
				res += diff * toAdd;
				j += time * toAdd;
				usedMap = true;
			}

			mp[loc] = make_pair(j, res);
		}

		fout << "Case #" << z << ": " << res << endl;
	}

	return 0;
}