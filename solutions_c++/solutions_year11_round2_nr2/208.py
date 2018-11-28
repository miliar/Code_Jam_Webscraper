#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;

#define ll long long

bool canDo(const vector<ll>& pos, ll D, ll N)
{
	ll prev = pos[0] - N;
	for (size_t i=1; i<pos.size(); ++i)
	{
		ll idealLoc = prev + D;

		ll minPos = pos[i] - N;
		ll maxPos = pos[i] + N;

		if (idealLoc > maxPos)
			return false;

		prev = max(minPos, idealLoc);
	}

	return true;
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	fout << std::setprecision(20);
	unsigned int numberOfCases;
	fin >> numberOfCases;

	int C, P, V;
	ll D;

	vector<ll> loc;
	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		loc.clear();
		fin >> C;
		fin >> D;

		D *= 2;
		for (int i=0; i<C; ++i)
		{
			fin >> P >> V;
			loc.insert(loc.end(), V, P*2);
		}

		ll res = 0;
		while (!canDo(loc, D, res))
		{
			if (res > 0)
				res *= 2;
			else
				++res;			
		}

		if (res > 0)
		{
			ll lo = res/2;
			while (res - lo > 1)
			{
				ll test = (res+lo)/2;
				if (canDo(loc, D, test))
					res = test;
				else
					lo = test;
			}
		}
		
		double result = 0.5 * double(res);
		fout << "Case #" << zz << ": " << result << endl;
	}

	return 0;
}