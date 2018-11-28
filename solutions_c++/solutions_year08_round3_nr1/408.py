
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long  ll;

ll RunTest(ifstream &in)
{
	vector<int> sets;
	ll p, k, l;
	ll res = 0;
	vector<ll> freq;
	vector<ll> assigned;
		
	in >> p >> k >> l;
	in.get();

//	cout << p << " " << k << " " << l << endl;

	assigned.resize(k);
	for(int i = 0; i < k; i++)
		assigned[i] = 0;

	freq.resize(l);
	for(int i = 0; i < l; i++)
		in >> freq[i];

	sort(freq.begin(), freq.end());
	for(int i = l - 1; i >= 0; i--)
	{
		assigned[0]++;
		if(assigned[0] > p)
			return -1;

		res += assigned[0]*freq[i];

		sort(assigned.begin(), assigned.end());

//		cout << freq[i] << " ";
	}
//	cout << endl;


	return res;
}

int main(int argc, char* argv[])
{
	if(argc != 2)	cout << "specify input file";
	ifstream in(argv[1]);

	ll n;
	in >> n;

	for(long long i = 0; i < n; i++)
	{
		ll res = RunTest(in);
		if(res > 0)
			cout << "Case #" << (i + 1) << ": " << res << endl;
		else
			cout << "Case #" << (i + 1) << ": " << "Impossible" << endl;
	}

	return 0;
}

