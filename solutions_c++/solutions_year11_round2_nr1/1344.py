
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

ifstream fin("in.txt");
#define cin fin

ofstream fout("out.txt");
#define cout fout


int main()
{
	int t, i;
	cin>>t;
	for(i=0; i<t; i++)
	{
		cout<<"Case #"<<i+1<<":"<<endl;
		int n, j, k, m;
		cin>>n;
		vector<string> v(n);
		for(j=0; j<n; j++)
		{
			cin>>v[j];
		}

		vector<int> p(n, 0);
		vector<int> w(n, 0);
		vector<double> wp(n, 1.0);
		vector<double> owp(n, 0.0);
		vector<double> oowp(n, 0.0);

		for(j=0; j<n; j++)
		{
			for(k=0; k<n; k++)
			{
				if(v[j][k] != '.')
				{
					p[j]++;
					if(v[j][k] == '1')
					{
						w[j]++;
					}
				}
			}
		}
		for(j=0; j<n; j++)
		{
			wp[j] = (double)w[j] / (double)p[j];
		}
		for(j=0; j<n; j++)
		{
			int q = 0;
			for(k=0; k<n; k++)
			{
				if(v[j][k] != '.')
				{
					int ww = w[k];
					int pp = p[k];
					if(v[k][j] == '1')
					{
						ww--;
					}
					pp--;
					owp[j] += (double)ww / (double)pp;
					q++;
				}
			}
			owp[j] /= (double)q;
		}
		for(j=0; j<n; j++)
		{
			int q = 0;
			for(k=0; k<n; k++)
			{
				if(v[j][k] != '.')
				{
					oowp[j] += owp[k];
					q++;
				}
			}
			oowp[j] /= (double)q;

			double res = 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j];
			cout<<res<<endl;
		}
	}
	return 0;
}