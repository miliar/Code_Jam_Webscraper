#include <iostream>
#include <iomanip>
#include <cmath>
#include <cassert>

using namespace std;

double A[2][2], B[10][2];

double dist(double p, double q, double x, double y)
{
	return sqrt((x-p)*(x-p) + (y-q)*(y-q));
}

int main()
{
	int T,cn=1;
	cin >> T;
	while(T--)
	{
		int N, M;
		cin >> N >> M;
		assert(N==2);
		for(int i=0;i<N;i++) cin>>A[i][0]>>A[i][1];
		for(int i=0;i<M;i++) cin>>B[i][0]>>B[i][1];
		cout << "Case #" << cn << ":";
		double c = dist(A[0][0],A[0][1],A[1][0],A[1][1]);
		for(int i=0;i<M;i++)
		{
			double r0 = dist(A[0][0],A[0][1],B[i][0],B[i][1]),
				r1 = dist(A[1][0],A[1][1],B[i][0],B[i][1]);
			double CBD = 2.0*acos((r1*r1 + c*c - r0*r0)/(r1*c*2)),
				CAD = 2.0*acos((r0*r0 + c*c - r1*r1)/(r0*c*2));
			double ar = 0.5*CBD*r1*r1 - 0.5*r1*r1*sin(CBD)
				+ 0.5*CAD*r0*r0 - 0.5*r0*r0*sin(CAD);
			cout << " " << fixed << setprecision(8) << ar;
		}
		cout << endl;
		cn++;
	}
	return 0;
}
