// codejam2009_r2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <tchar.h>
#include <vector>
#include <iostream>
#include <math.h>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <cstring>
#include <bitset> 
#include <ctype.h>
#include <fstream>
#include <climits>
#include <stdio.h>
#include <stdlib.h>
#include <cstdio> 
#include <cstdlib> 
#include <time.h>
#include <ctime>
#include <wchar.h>
#include <wctype.h>
#include <cwchar> 
#include <cwctype> 
#include <complex>
#include <deque>
#include <exception>
#include <list>
#include <map>
#include <iomanip> 
#include <set>
#include <sstream>
#include <stack>
using namespace std; 

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("D-small-attempt3.in","r",stdin);
	freopen("out.txt","w",stdout);

	int C;
	cin >> C;
	int N;
	double R;
	vector<int> x(3,0.0);
	vector<int> y(3,0.0);
	vector<int> r(3,0.0);
	
	for (int i = 1; i <= C; i++)
	{
		cin >> N;
		int xPos,yPos,radius;
		for (int j = 0; j < N; j++)
		{
			cin >> xPos >> yPos >> radius;
			x[j] = xPos;
			y[j] = yPos;
			r[j] = radius;
		}

		double d1,d2,d3;
		d1 = sqrt(pow(double(x[0]-x[1]),2)+pow(double(y[0]-y[1]),2)) + r[0] + r[1];
		d2 = sqrt(pow(double(x[0]-x[2]),2)+pow(double(y[0]-y[2]),2)) + r[0] + r[2];
		d3 = sqrt(pow(double(x[1]-x[2]),2)+pow(double(y[1]-y[2]),2)) + r[1] + r[2];
		double minimum;
		if ( N == 1)
		{
			R = r[0];
		}
		else if ( N == 2)
		{
			R = r[0] > r[1] ? r[0] : r[1];
		}
		else
		{
			double minimum = d1 < (d2 < d3 ? d2 : d3) ?d1 : (d2 < d3 ? d2 : d3);
			R = minimum/2.0;
		}

		printf("Case #%d: %f\n",i,R);

		for (int k = 0; k < N; k++)
		{
			x[k] = 0.0;
			y[k] = 0.0;
			r[k] = 0.0;
		}		
	}

	return 0;
}

