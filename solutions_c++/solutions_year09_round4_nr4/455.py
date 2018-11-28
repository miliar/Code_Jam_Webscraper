// ProbD.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;

void solve()
{
	int T;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		vector<double> X;
		vector<double> Y;
		vector<double> R;
		int N;
		cin >> N;
		X.resize(N);
		Y.resize(N);
		R.resize(N);
		for (int i=0;i<N;i++)
		{
			cin >> X[i] >> Y[i] >> R[i];
		}
		double radi = 0;
		if (N==1)
		{
			radi = R[0];
		}
		else if (N==2)
		{
			radi = max(R[0], R[1]);
		}
		else if (N==3)
		{
			for (int i1=0;i1<3;i1++)
			{
				int i2 = (i1+1)%3;
				int i3 = (i1+2)%3;
				double dist = sqrt( (X[i2]-X[i3])*(X[i2]-X[i3]) + (Y[i2]-Y[i3])*(Y[i2]-Y[i3]) ) + R[i2] + R[i3];
				dist *= 0.5;
				double dradi = max(dist, R[i1]);
				if (i1==0)
				{
					radi = dradi;
				}
				else if (dradi<radi)
				{
					radi = dradi;
				}
			}

		}

		cout << "Case #" << (t+1) << ": " << radi << endl;
	}

}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

