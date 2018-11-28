#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

double dist(double x, double y, double x1, double y1, double r)
{
	return sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))+r;
}



int main()
{
	int v;
	cin>>v;
	for(int c=1;c<=v;c++)
	{
		int n;
		cin>>n;
		vector<int> xes;
		vector<int> yes;
		vector<int> res;
		double result;
		for(int i=0;i<n;i++)
		{
			int x,y,r;
			cin>>x>>y>>r;
			xes.push_back(x);
			yes.push_back(y);
			res.push_back(r);

		}
		if(xes.size()==1)
		{
			result = res[0];
		}
		else if(xes.size()==2)
		{
			result = max(res[0],res[1]);
		}
		else if(xes.size()==3)
		{
			double k1 = max<double>((dist(xes[0],yes[0],xes[1],yes[1],res[0])+res[1])/2,res[2]);
			double k2 = max<double>((dist(xes[0],yes[0],xes[2],yes[2],res[0])+res[2])/2,res[1]);
			double k3 = max<double>((dist(xes[1],yes[1],xes[2],yes[2],res[1])+res[2])/2,res[0]);
			
			result = min(k1,min(k2,k3));
		}
		cout<<"Case #"<<c<<": "<<result<<endl;
	}
}