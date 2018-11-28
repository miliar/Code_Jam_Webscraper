#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;


int main()
{
	int N;
	cin >> N;

	for(int c=0;
		c<N;
		++c)
	{
		int P, K, L, f;
		cin >> P >> K >> L;

		map<long, long> freq;
		map<long, long> depth;
		vector<pair<long, long> > sf;

		long currchar='a';
		for(int i=0; i<L; ++i, ++currchar)
		{
			cin >> f;
			freq[currchar]=f;
		}

		//// check impossible
		//if(L > P*K)
		//{
		//	cout << "Case #" << c+1 << ": " << "Impossible" << '\n';
		//	continue;
		//}

		unsigned long presses = 0;

		for(map<long, long>::const_iterator it = freq.begin(); it != freq.end(); ++it)
		{
			sf.push_back(make_pair(it->second, it->first));
		}

		sort(sf.begin(), sf.end(), greater<pair<long, long> >());

		//vector<vector<long> > phone;
		vector<long> keydepth;
		keydepth.resize(K);

		long cK=0;
		for(vector<pair<long, long> >::iterator it = sf.begin(); it != sf.end(); ++it)
		{
			++keydepth[cK];
			depth[it->second]=keydepth[cK];
			cK = (cK+1) % K;
		}

		unsigned long long res=0;
		for(map<long, long>::iterator it = depth.begin(); it != depth.end(); ++it)
		{
			res+=freq[it->first]*it->second;
		}

		cout << "Case #" << c+1 << ": " << res << '\n';
	}

	return 0;
}
