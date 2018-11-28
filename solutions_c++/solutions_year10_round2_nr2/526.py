#include <iostream>
#include <vector>
#include <climits>

using namespace std;

unsigned int minswaps(const vector<unsigned int> &pos, const vector<unsigned int> &vel, unsigned int t, unsigned int b, unsigned int k)
{
	unsigned int swaps=0;
	unsigned int count=0;
	for (unsigned int i=pos.size()-1; k!=0 && i<pos.size(); --i)
	{
		if (pos[i]+vel[i]*t>=b)
		{
			--k;
			swaps+=count;
		}
		else
			++count;
	}
	if (k==0)
		return swaps;
	return UINT_MAX;
}

int main()
{
	unsigned int c;
	cin >> c;
	for (unsigned int i=1; i<=c; ++i)
	{
		unsigned int tmp;
		unsigned int n, k, b, t;
		cin >> n >> k >> b >> t;
		vector<unsigned int> pos, vel;
		for (unsigned int j=0; j<n; ++j)
		{
			cin >> tmp;
			pos.push_back(tmp);
		}
		for (unsigned int j=0; j<n; ++j)
		{
			cin >> tmp;
			vel.push_back(tmp);
		}
		tmp=minswaps(pos, vel, t, b, k);
		cout << "Case #" << i << ": ";
		if (tmp==UINT_MAX)
			cout << "IMPOSSIBLE";
		else
			cout << tmp;
		cout << endl;
	}
}
