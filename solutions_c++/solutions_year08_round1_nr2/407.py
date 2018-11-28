/*
2
5
3
1 1 1
2 1 0 2 0
1 5 0
1
2
1 1 0
1 1 1
*/
#include <iostream>
#include <vector>
#include <list>
#include <iterator>
#include <algorithm>
using namespace std;

typedef vector< pair<int,int> > one_taste_t;
typedef vector< vector< pair<int, int> > > taste_t;

bool satisfy(const taste_t& vt, int milk, int nflavor)
{
	//cout << "flavor " << nflavor << endl;
	int nc = vt.size();
	vector<int> good(nc);
	for(int i=0; i < nflavor; i++, milk /= 2)
	{
		int malt = milk % 2;
		for(int j=0; j < nc; j++)
		{
			if (good[j]) continue;
			if (find(vt[j].begin(), vt[j].end(), make_pair(i+1,malt)) != vt[j].end())
				good[j] = 1;
		}
	}
/*
	for(int i=0; i < good.size(); i++)
		cout << good[i] << " ";
	cout << endl;
*/
	int ret = 1;
	for(int i=0; i < good.size(); i++)
		ret *= good[i];
	return ret;
}

void print(taste_t vt)
{
	for(int i=0; i < vt.size(); i++)
	{
		for(int j=0; j < vt[i].size(); j++)
		{
			cout << "(" << vt[i][j].first << "," << vt[i][j].second << ") ";
		}
		cout << endl;
	}
}
int main()
{
	int ncase;
	cin >> ncase;
	taste_t vt;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << icase+1 << ": ";
		vt.clear();
		int nflavor, ncustomer;
		cin >> nflavor >> ncustomer;
		for(int i=0; i < ncustomer; i++)
		{
			int nt; cin >> nt;
			one_taste_t vv;
			for(int tt=0; tt < nt; tt++)
			{
				pair<int,int> p;
				cin >> p.first >> p.second;
				vv.push_back(p);
			}
			vt.push_back(vv);
		}
//		print(vt);
		// try all milkshake
		int min_milk = -1;
		for(int milk=0; milk < (1<<nflavor); milk++)
		{
			if (satisfy(vt, milk, nflavor))
			{ if (min_milk < 0 || min_milk > milk) min_milk = milk; }
		}
//		cout << min_milk << endl;
		if (min_milk < 0) { cout << "IMPOSSIBLE\n"; continue; }
		for(int i=0; i < nflavor-1; i++, min_milk /= 2)
		{
			cout << (min_milk % 2) << " ";
		}
		cout << (min_milk % 2) << "\n";
	}
}
