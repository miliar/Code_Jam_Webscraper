#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;


struct seg
{
	double start;
	double end;
	double speed;
	bool operator < (const seg& s) const
	{
		return start < s.start;
	}
};

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int taa;
	cin>>taa;
	cout.setf(ios_base::fixed);
	cout.precision(20);
	for (int aaa = 0; aaa < taa; aaa++)
	{
		double x;
		cin>>x;
		double s,r,t;
		cin>>s>>r>>t;
		double dv = r - s;
		int n;
		cin>>n;
		vector<seg> v(n);
		for (int i=0;i<n;i++)
		{
			cin>>v[i].start>>v[i].end>>v[i].speed;
			v[i].speed += s;
		}

		sort(v.begin(),v.end());
		vector<pair< double, double> > reg;
		if (v.size())
			reg.push_back(make_pair(s, v[0].start));
		for (int i=0;i<(int)v.size();i++)
		{
			double pn = x;
			if (i + 1 < v.size())
				pn = v[i+1].start;
			reg.push_back(make_pair(v[i].speed, v[i].end - v[i].start));
			reg.push_back(make_pair(s, pn - v[i].end));
		}
		sort(reg.begin(),reg.end());

		double tres = 0;
		for (int i=0;i<(int)reg.size();i++)
		{
			double tc = reg[i].second / (reg[i].first + dv);
			double tsplit = min(t, tc);
			tres += tsplit;
			t -= tsplit;
			reg[i].second -= (reg[i].first + dv) * tsplit;
			tres += reg[i].second / (reg[i].first);
		}

		cout<<"Case #"<<aaa + 1<<": ";
		cout<<tres;
		cout<<endl;
	}
	
}