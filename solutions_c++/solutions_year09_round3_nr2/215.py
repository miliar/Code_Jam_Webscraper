/*
 *  CentreOfMass.cpp
 * 
 *  Note the spelling, yanks
 *
 *  Created by Josh Deprez on 13/09/09.
 *
 * This code was probably compiled using llvm-g++. The LLVM compiler infrastructure is freely 
 * available at http://llvm.org/
 */

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;
#define S(x) ({double __t=x; __t*__t;})

int main()
{
	
	int T;
	cin >> T;
	
	for(int t=0; t<T; ++t)
	{
		int N;
		cin >> N;
		double b[6] = {0,0,0,0,0,0};
		double dmin,tmin;
		double a[6];
		for (int i=0; i<N; ++i)
		{
			for (int j=0; j<6; ++j)
			{
				cin >> a[j];
				b[j] += a[j];
			}
		}
		for (int j=0; j<6; ++j)
		{
			b[j] /= N;
		}
		
		double denom = b[3]*b[3]+b[4]*b[4]+b[5]*b[5];
		tmin = 0.0;
		if (denom > 0.0) 
			tmin = -1.0 * (b[0]*b[3]+b[1]*b[4]+b[2]*b[5]) / denom;
		if (tmin > 0.0)
		{
			dmin=sqrt(S(b[0]+tmin*b[3])+S(b[1]+tmin*b[4])+S(b[2]+tmin*b[5]));
		} else {
			tmin = 0.0;
			dmin = sqrt(b[0]*b[0]+b[1]*b[1]+b[2]*b[2]);
		}
		
		cout.precision(10);
		cout << "Case #" << (t+1) << ": " << fixed << dmin << " " << tmin << endl;
	}
	 
	return 0;
}

