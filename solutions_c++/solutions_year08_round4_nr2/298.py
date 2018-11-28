//CODEJAM - B

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

#define sqr(A) ((A)*(A))
#define rabs(A) ((A)<0.0 ? (-(A)) : (A))

int main()
{
	//vars
	ifstream f ("B-small.in");
	ofstream g ("B-small.out");
	int t,tt,n,m,x1,y1,x2,y2;
	double a,b,c,s,A,ar;
	//testcase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			//input
			f >> n >> m >> ar;
			ar/=2.0;
			//pre-output
			cout << "Case #" << t << ": ";
			g << "Case #" << t << ": ";
			//try all points =D
				for (x1=0; x1<=n; x1++)
					for (x2=0; x2<=n; x2++)
						for (y1=0; y1<=m; y1++)
							for (y2=0; y2<=m; y2++)
							{
								a=sqrt(sqr(x1)+sqr(y1));
								b=sqrt(sqr(x2)+sqr(y2));
								c=sqrt(sqr(x1-x2)+sqr(y1-y2));
								s=(a+b+c)/2.0;
									if ((s>a) && (s>b) && (s>c))
									{
										A=sqrt(s*(s-a)*(s-b)*(s-c));
											if (rabs(A-ar)<0.000000001)
											{
												cout << 0 << ' ' << 0 << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
												g << 0 << ' ' << 0 << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
												goto done;
											}
									}
							}
			//impossible :(
			cout << "IMPOSSIBLE" << endl;
			g << "IMPOSSIBLE" << endl;
done:
			a=a;
		}
	return(0);
}