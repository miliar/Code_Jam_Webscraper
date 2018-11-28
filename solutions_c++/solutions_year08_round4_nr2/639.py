#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <memory.h>

using namespace std;

#define LL              	long long
#define pb              	push_back
#define mp              	make_pair
typedef vector <int> 		vi;
typedef vector <string> 	vs;
typedef pair   <int,int>    pii;

int n,m,a;
int rx1,ry1,rx2,ry2,rx3,ry3;

void process()
{
	int i,j,u,v;
	double s,p,x,y,z;
	
	rx1 = -1;

	for (i=1; i<=n; i++) if (a%i==0)
	{
		j = a/i;
		if (0<=j && j<=m) { rx1=ry1=0; rx2=i; ry2=0; rx3=0; ry3=j; return;}
	}

	for (i=0; i<=n; i++) for (j=0; j<=m; j++) if (!(i==0 && j==0))
	{
		for (u=i; u<=n; u++) for (v=0; v<=m; v++) if (!(u==i && v==j))
		{
			x = sqrt(1.0*(i*i+j*j));
			y = sqrt(1.0*(u*u+v*v));
			z = sqrt(1.0*((i-u)*(i-u)+(j-v)*(j-v)));

			p = (x+y+z)/2;
			s = 2*sqrt(p*(p-x)*(p-y)*(p-z));
			if (fabs(s-a)<1e-9) { rx1=ry1=0; rx2=i; ry2=j; rx3=u; ry3=v; return; }
		}
	}
}

int main()
{
	int numtest;
	cin >> numtest;
	for (int i=1; i<=numtest; i++)
	{
		cin >> n >> m >> a;
		process();

		cout << "Case #" << i << ": ";
		if (rx1 == -1) { cout << "IMPOSSIBLE" << endl; continue; }
		cout << rx1 << " " << ry1 << " " << rx2 << " " << ry2 << " " << rx3 << " " << ry3 << endl;
	}

	return 0;
}
