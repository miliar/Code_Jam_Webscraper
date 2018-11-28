// b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

typedef long double LD;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
//#define EPS 1e-11

const LD EPS = 1e-11L;
const LD EPS2 = 1e-6L;

LD pow2(LD x)
{
	return x * x;
}

VI xs,ys,zs,vxs,vys,vzs;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	//freopen("2.in","r",stdin);
	int t;
	cin >> t;
	int caseId = 1;

	while(t--)
	{
		int n;
		LD x,y,z,vx,vy,vz;
		LD a1 = 0.0, b1 = 0.0, a2 = 0.0, b2 = 0.0, a3 = 0.0, b3 = 0.0;
		LD a,b,c;
		xs.clear();
		ys.clear();
		zs.clear();
		vxs.clear();
		vys.clear();
		vzs.clear();

		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> x >> y >> z >> vx >> vy >> vz;
			xs.push_back(x);
			ys.push_back(y);
			zs.push_back(z);
			vxs.push_back(vx);
			vys.push_back(vy);
			vzs.push_back(vz);
			a1 += x;
			b1 += vx;
			a2 += y;
			b2 += vy;
			a3 += z;
			b3 += vz;
		}
		a1 /= n;
		b1 /= n;
		a2 /= n;
		b2 /= n;
		a3 /= n;
		b3 /= n;

		c = pow2(a1) + pow2(a2) + pow2(a3);
		b = 2.0 * a1 * b1 + 2.0 * a2 * b2 + 2.0 * a3 * b3;
		a = pow2(b1) + pow2(b2) + pow2(b3);

		LD tt = EPS;
		LD dis = EPS;
		if (fabs(a) < EPS)
		{
			if (fabs(b) < EPS)
			{
				if (c < 0.0)
					dis = 0.0;
				else
					dis = sqrt(c);
				printf("Case #%d: %.8f %.8f\n",caseId++,dis,+tt);
				continue;
			}
			else
			{
				tt = -1.0 * c / b;
				if (fabs(tt) < EPS || tt < 0.0)
				{
					tt = 0.0;
					dis = b * tt + c;
				}
				dis = b * tt + c;
				
				printf("Case #%d: %.8f %.8f\n",caseId++,dis,+tt);
				continue;
			
			}
			/*printf("Case #%d: %.8f %.8f\n",caseId++,dis,+tt);
			continue;*/
		}

		tt = -1.0 * b / (2 * a);
		if (fabs(tt) < EPS || tt < 0.0)
			tt = 0.0;
		
		dis = a * pow2(tt) + b * tt + c;
		//cout << dis << endl;
		if (fabs(dis) < EPS2)
			dis = 0.0;
		dis = sqrt(dis);

		printf("Case #%d: %.8f %.8f\n",caseId++,dis,tt);
	}
	return 0;
}

