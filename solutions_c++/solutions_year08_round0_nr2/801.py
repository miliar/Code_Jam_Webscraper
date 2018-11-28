#include "stdafx.h"

#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

pair<int,int> solve(const vector<pair<int,int>>& as, const vector<pair<int,int>>& bs, int t)
{
	int na = as.size(), nb = bs.size();
	vector<pair<int,pair<int,int>>> v;
	vector<int> used(na+nb, 0);

	for (int i = 0; i < na; ++i) v.push_back(make_pair(as[i].first, make_pair(as[i].second,0)));
	for (int i = 0; i < nb; ++i) v.push_back(make_pair(bs[i].first, make_pair(bs[i].second,1)));

	sort(v.begin(), v.end());

	int ret[2] = {0};

	for (int i = 0; i < v.size(); ++i)
	{
		int curr = v[i].second.second;
		if (!used[i])
		{
			ret[curr]++;
		}
		int next = 1 - curr;
		for (int j = i+1; j < v.size(); ++j) if (!used[j] && v[j].second.second == next && v[i].second.first+t <= v[j].first)
		{
			used[j] = 1;
			break;
		}
	}

	return make_pair(ret[0], ret[1]);
}

int main()
{
	FILE* fin = fopen("B.in", "rt");
	FILE* fout = fopen("B.out", "wt");

	int numCase;
	fscanf(fin, "%d", &numCase);

	for (int caseNo = 1; caseNo <= numCase; ++caseNo)
	{
		int t;
		int na,nb;
		vector<pair<int,int>> as, bs;

		fscanf(fin, "%d%d%d", &t, &na,&nb);
		for (int i = 0; i < na; ++i)
		{
			int h0,h1,s0,s1;
			fscanf(fin, "%02d:%02d %02d:%02d", &h0, &s0, &h1, &s1);
			as.push_back(make_pair(h0*60+s0, h1*60+s1));
		}
		for (int i = 0; i < nb; ++i)
		{
			int h0,h1,s0,s1;
			fscanf(fin, "%02d:%02d %02d:%02d", &h0, &s0, &h1, &s1);
			bs.push_back(make_pair(h0*60+s0, h1*60+s1));
		}

		pair<int,int> p = solve(as, bs, t);
		fprintf(fout, "Case #%d: %d %d\n", caseNo, p.first, p.second);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
