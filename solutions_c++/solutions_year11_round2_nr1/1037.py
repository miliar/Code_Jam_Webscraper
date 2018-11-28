// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

void solve(string sFileIn, string sFileOut)
{
	char buf[1024];
	int N, T;
	ifstream fi(sFileIn.c_str());
	ofstream fo(sFileOut.c_str());
	fi >> T;
	for (int i=0;i<T;i++)
	{
		vector<string> dt;
		fi >> N;
		fi.getline(buf, 1024);
		for (int j=0;j<N;j++)
		{
			fi.getline(buf, 1024);
			dt.push_back(buf);
		}
		
		vector<double> tot(N, 0.0);
		vector<double> WP(N, 0.0);
		vector<double> OWP(N, 0.0);
		vector<double> OOWP(N, 0.0);
		vector<int> tel(N, 0);
		for (int j=0;j<N;j++)
		{
			for (int k=0;k<N;k++)
			{
				if (dt[j][k]=='1')
				{
					tot[j] += 1.0;
					tel[j]++;
				} else if (dt[j][k]=='0')
				{
					tel[j]++;
				}
			}
			WP[j] = tot[j] / tel[j];
		}
		for (int j=0;j<N;j++)
		{
			double d = 0;
			int t = 0;
			for (int k=0;k<N;k++)
			{
				if (dt[j][k]!='.')
				{
					double owp = tot[k];
					if (dt[k][j]=='1')
						owp -= 1.0;
					d += owp / (tel[k]-1);
					t++;
				}
			}
			OWP[j] = d / t;
		}
		for (int j=0;j<N;j++)
		{
			double d = 0;
			int t = 0;
			for (int k=0;k<N;k++)
			{
				if (dt[j][k]!='.')
				{
					d += OWP[k];
					t++;
				}
			}
			OOWP[j] = d / t;
		}

		fo << "Case #" << (i+1) << ":"  << endl;
		for (int j=0;j<N;j++)
		{
			//cout << WP[j] << " " << OWP[j] << " " << OOWP[j] << endl;
			double d = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
			sprintf(buf,"%.12lf",d);
			fo << buf << endl;
		}
	}
	fi.close();
	fo.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	//solve("test.in", "test.out");
	//solve("A0.in", "A0.out");
	solve("A1.in", "A1.out");

	return 0;
}

