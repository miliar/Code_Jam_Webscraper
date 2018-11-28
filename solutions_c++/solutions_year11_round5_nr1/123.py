//replace all commas to spaces
#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

vector<pair<double, double> > v1;
vector<pair<double, double> > v2;
double w;

double getSquare(vector<pair<double, double> > &v, double pos)
{
	double s = 0;
	for (int i=0;i + 1<(int)v.size();i++)
	{
		double len = min(v[i+1].first, pos) - v[i].first;
		if (len >= 0)
		{
			double y1 = v[i].second;
			double y2 = (v[i+1].second - v[i].second) / (v[i+1].first - v[i].first) * len + v[i].second;
			s += (y1 + y2) / 2 * len;
		}
	}
	return s;
}
double getSquare(double pos)
{
	return (getSquare(v2, pos) - getSquare(v1, pos)) / (getSquare(v2, w) - getSquare(v1, w));
}
double getPart(double val)
{
	double cur = 0;
	double len = w;
	while (len > 1e-20)
	{
		double test = cur + len;
		if (getSquare(test) < val)
			cur = test;
		len /= 2;
	}
	return cur;
}


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
		int l, u, g;
		cin>>w>>l>>u>>g;
		
		v1 = vector<pair<double, double> > (l);
		v2 = vector<pair<double, double> > (u);
		for (int i=0;i<l;i++)
			cin>>v1[i].first>>v1[i].second;
		for (int i=0;i<u;i++)
			cin>>v2[i].first>>v2[i].second;
		cout<<"Case #"<<aaa + 1<<": ";
		for (int i=1;i<g;i++)
			cout<<endl<<getPart(double(i) / g);
		cout<<endl;
	}
	
}