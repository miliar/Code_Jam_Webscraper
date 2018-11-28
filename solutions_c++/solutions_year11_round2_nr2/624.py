#include <iostream>
#include <vector>
#include <iomanip>
#include<algorithm>
#include<fstream>

using namespace std;

double foo( const vector<double> &x, double T )
{
	if (x.size() < 2)
	{
		return 0.;
	}
	double dmin = 0.0;
	double dmax = x.size() * T;
	double D = 0.;
	while(dmax - dmin > 1e-8)
	{
		D = (dmax + dmin) / 2.0;
		double nextBorder = T + x[0] - D;
		size_t i;
		for(i = 1; i < x.size(); i++)
		{
			if (nextBorder > x[i] + D)
			{
				dmin = D;
				break;
			}
			nextBorder = T + max<double>(nextBorder, x[i] - D);
		}
		if(i == x.size())
		{
			dmax = D;
		}
	}
	return D;
}

int main()
{
     freopen("ag.in","r",stdin);
    freopen("ag.out","w",stdout);
	int t;
	cin>>t;int cn=0;
	//cout << setiosflags(ios::fixed) << setprecision(100);
	while(t--)
	{cn++;
		int n;
		double T;
		cin >> n >> T;int a,b;
		vector<int>dum;
        for(int x=0;x<n;x++)
        {
            cin>>a>>b;
            for(int y=0;y<b;y++)dum.push_back(a);
        }
        int N=dum.size();
		vector<double> x(dum.begin(),dum.end());
		sort(x.begin(),x.end());
		cout << "Case #"<<cn<<": "<<foo(x, T) << endl;
	}
	return 0;
}
