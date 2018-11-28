#include<set>
#include<map>
#include<cstdio>
#include<vector>
#include<string>
#include<fstream>
#include<iostream>
using namespace std;

ifstream in("plik.in");
ofstream out("plik.out");

typedef long long ll;
#define PII pair<int,int>
#define FI first
#define SE second
#define MP make_pair

int R;

set<PII> area;

set<PII> toRem, toAdd;
set<PII> toRe2, toAd2;

int lecim()
{
	area.clear();
	toRem.clear();
	toAdd.clear();

	in >> R;
	for(int i = 0; i < R; ++i)
	{
		int xa, ya, xb, yb;
		in >> xa >> ya >> xb >> yb;

		for(int j = xa; j <= xb; ++j)
			for(int k = ya; k <= yb; ++k)
			{
				area.insert(MP(j, k));
			}
	}

	for(set<PII>::iterator it = area.begin(); it != area.end(); ++it)
	{
		PII po = *it;

		if(!area.count(MP(po.first - 1, po.second)) && !area.count(MP(po.first, po.second - 1)))
		{
			toRem.insert(po);
		}


		po.first++;
		if(area.count(MP(po.first - 1, po.second)) && area.count(MP(po.first, po.second - 1)))
		{
			toAdd.insert(po);
		}

		po.first--;
		po.second++;
		if(area.count(MP(po.first - 1, po.second)) && area.count(MP(po.first, po.second - 1)))
		{
			toAdd.insert(po);
		}
	}

	int ret = 0;

	while (!area.empty())
	{
		for(set<PII>::iterator it = toRem.begin(); it != toRem.end(); ++it)
		{
			PII po = *it;
			area.erase(area.find(po));
		}
		for(set<PII>::iterator it = toAdd.begin(); it != toAdd.end(); ++it)
		{
			PII po = *it;
			area.insert(po);
		}

		toRe2.clear();
		toAd2.clear();

		for(set<PII>::iterator it = toRem.begin(); it != toRem.end(); ++it)
		{
			PII po = *it;
			po.first++;
			if(area.count(po) && !area.count(MP(po.first - 1, po.second)) && !area.count(MP(po.first, po.second - 1)))
			{
				toRe2.insert(po);
			}
			po.first--;

			po.second++;
			if(area.count(po) && !area.count(MP(po.first - 1, po.second)) && !area.count(MP(po.first, po.second - 1)))
			{
				toRe2.insert(po);
			}
		}
		for(set<PII>::iterator it = toAdd.begin(); it != toAdd.end(); ++it)
		{
			PII po = *it;
			po.first++;
			if(!area.count(po) && area.count(MP(po.first - 1, po.second)) && area.count(MP(po.first, po.second - 1)))
			{
				toAd2.insert(po);
			}

			po.first--;
			po.second++;
			if(!area.count(po) && area.count(MP(po.first - 1, po.second)) && area.count(MP(po.first, po.second - 1)))
			{
				toAd2.insert(po);
			}
		}

		toAdd = toAd2;
		toRem = toRe2;

		++ret;
	}

	return ret;
}

int main()
{
	int t;
	in >> t;

	for(int i = 1; i <= t; ++i)
	{
		cout << i << "\n";
		out << "Case #" << i << ": " << lecim() << "\n";
	}
	in.close();
	out.close();
	cin >> t;
	return 0;
}