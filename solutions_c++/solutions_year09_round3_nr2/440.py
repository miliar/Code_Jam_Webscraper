#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int L, D, N;

int main()
{
	FILE *streamIn;
	FILE *streamOut;

	//freopen_s(&streamIn, "data/test.in", "r", stdin);
	//freopen_s(&streamOut, "data/test.out", "w", stdout);
	//freopen_s(&streamIn, "data/B-small-attempt3.in", "r", stdin);
	//freopen_s(&streamOut, "data/B-small-attempt3.out", "w", stdout);
	freopen_s(&streamIn, "data/B-large.in", "r", stdin);
	freopen_s(&streamOut, "data/B-large.out", "w", stdout);
	
	int numTestCases;

	scanf_s("%d", &numTestCases);

	for (int caseId = 1; caseId <= numTestCases; caseId++)
	{
		int N;
		scanf_s("%d", &N);

		double x=0,y=0,z=0,vx=0,vy=0,vz=0;
		int ivx=0,ivy=0,ivz=0;

		for (int i=0;i<N;i++)
		{
			int a,b,c,d,e,f;
			scanf_s("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
			x+=(double)a;y+=(double)b;z+=(double)c;vx+=(double)d;vy+=(double)e;vz+=(double)f;

			ivx+=d;
			ivy+=e;
			ivz+=f;
		}
		
		x/=(double)N;y/=(double)N;z/=(double)N;vx/=(double)N;vy/=(double)N;vz/=(double)N;

		if (ivx==0&&ivy==0&&ivz==0)
		{
			printf("Case #%i: %9.8f %9.8f\n", caseId, sqrtf(x*x+y*y+z*z), 0.0f);
		}
		else
		{

			double t=-(x*vx+y*vy+z*vz)/(vx*vx+vy*vy+vz*vz);
			if (t<=0.0f) t=0.0f;

			double fx=x+t*vx;
			double fy=y+t*vy;
			double fz=z+t*vz;
			double dist=sqrtf(fx*fx+fy*fy+fz*fz);

			printf("Case #%i: %9.8f %9.8f\n", caseId, dist, t);
		}
	}

	fflush(stdout);
}
