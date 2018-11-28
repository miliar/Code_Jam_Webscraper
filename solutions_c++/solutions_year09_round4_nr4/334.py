#include <iostream>
#include <vector>
#include <string>
#include <cmath>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;

double dis (double xa, double ya, double xb, double yb)
{
	double dx=xa-xb;
	double dy=ya-yb;
	return sqrt (dx*dx+dy*dy);
}

double mx(double a, double b)
{
	return a>b?a:b;
}

double calc ()
{
	int N;
	cin >> N;
	VI x(N);VI y(N);VI r(N);
	fi(N)
		cin >> x[i] >> y[i] >> r[i];
	if (N==1)
		return r[0];
	if (N==2)
		return max(r[0],r[1]);
	double resp=10000000000000.;
	fi (3) // i alone
	{
		VI vg;
		fj(3) 
			if (i!=j)
				vg.push_back(j);
		int a=vg[0];int b=vg[1];
		resp=min(resp,mx(r[i],(dis(x[a],y[a],x[b],y[b])+r[a]+r[b])/2.));
	} 
	return resp;
}

int main()
{
	int C;
	cin >> C;
	for (int caso=1;caso<=C;caso++)
	{
		cout << "Case #" << caso << ": " << calc() << endl;
	}
}
