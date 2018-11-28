#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

ifstream inp("in.txt");
ofstream outp("out.txt");

int main()
{
	int t;
	inp >> t;
	for (int i=0; i<t; ++i)
	{
		int n;
		inp>>n;
		vector<double> ans(n);
		vector<double> tw(n);
		vector<double> tt(n);

		vector<double> wp(n);
		vector<double> owp(n);
		vector<double> oowp(n);
		
		
		vector<vector<char> > a(n,vector<char>(n));
		for (int j=0; j<n; ++j)
		{
		double t(0),w(0);
		for (int k=0; k<n; ++k)
			{
			inp>>a[j][k];
			if (a[j][k]=='1')
				{
					tw[j]+=1;
					tt[j]+=1;
				}
			if (a[j][k]=='0')
				{
					tt[j]+=1;
				}
			}
		if (tt[j]!=0) wp[j]=tw[j]/tt[j];
		inp.ignore(1);
		}
		
		for (int l=0; l<n; l++)
		{
			double t(0),w(0);
			int x(0);
			for (int j=0; j<n; ++j)
			if (l!=j)
			{
				if (a[l][j]!='.')
				{
					++x;
					if (tt[j]>1)
						if (a[j][l]=='1')
						owp[l]+=(tw[j]-1)/(tt[j]-1);
						else
						owp[l]+=(tw[j])/(tt[j]-1);
				}	
			}
			if (x!=0)
			owp[l]=owp[l]/x;
		}

		for (int l=0; l<n; l++)
		{
			double t(0),w(0);
			int x(0);
			for (int j=0; j<n; ++j)
			if (l!=j)
			{
				if (a[l][j]!='.')
				{
					++x;
					oowp[l]+=owp[j];
				}	
			}
			if (x!=0)
			oowp[l]=oowp[l]/x;
		}

		for (int j=0; j<n; j++)
			ans[j]=wp[j]*0.25+owp[j]*0.5+oowp[j]*0.25;
		outp<<"Case #"<<i+1<<":"<<endl;
		for (int j=0; j<n; j++)
			outp<<ans[j]<<endl;
	}
	return 0;
}