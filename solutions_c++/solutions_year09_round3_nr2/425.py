#include <iostream>
#include <string>
#include <cmath>
#include<iomanip>

using namespace std;

#define MAX 100

int T;
int x[MAX];
int y[MAX];
int z[MAX];
int vx[MAX];
int vy[MAX];
int vz[MAX];

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);


	cin >> T;

	for (int I = 0 ; I < T; I++)
	{
		double dmin, tmin; 
		int N;
		cin >> N;
		for (int i = 0 ; i < N; i++)
			cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
		double q1 = 0, q2 = 0, q3 = 0;
		double w1 = 0, w2 = 0, w3 = 0;
		for (int i  = 0 ; i < N; i++)
		{
			q1 += x[i];
			q2 += y[i];
			q3 += z[i];
			w1 += vx[i];
			w2 += vy[i];
			w3 += vz[i];
		}
		q1 /= N;
		q2 /= N;
		q3 /= N;
		w1 /= N;
		w2 /= N;
		w3 /= N;
		double A = 0, B = 0, C = 0;
		C = q1 * q1 + q2 * q2 + q3 * q3;
		B = q1 * w1 + q2 * w2 + q3 * w3;
		B *= 2;
		A = w1 * w1 + w2 * w2 + w3 * w3;
		if (A < 0.00000000001)
		{
			dmin = sqrt(C); tmin = 0;
		}
		else
		{
			/*tmin = - B / A;
			tmin /= 2;
			if (tmin < 0)
			{
				tmin = 0; dist = sqrt(C);
			}
			else
			{
				dmin = - B * B / (4 * A) + C;
				if (dmin < 0)
				{
					double r1 = 0, r2 = 0, D = 0;
					D = B * B - 4 * A * C;
				}
				else dmin =  sqrt(dmin);
			}*/
			double r1 = 0, r2 = 0, D = 0;
			D = B * B - 4 * A * C;
			if (D < 0)
			{
				tmin = - B / A;
				tmin /= 2;
				if (tmin  < 0)
				{
					tmin = 0;
					dmin = sqrt(C);
				}
				else
				{
					dmin = sqrt(- B * B / (4 * A) + C);
				}
			}
			else
			{
				r1 = - B - sqrt (D);
				r2 = - B + sqrt (D);
				r1 /= (2 * A);
				r2 /= (2 * A);
				if (r1 > 0)
				{
					tmin = r1;
					dmin = 0;
				}
				else if (r2 > 0)
				{
					tmin = r2;
					dmin = 0;
				}
				else
				{
					tmin = 0;
					dmin = sqrt(C);
				}
			}
		}
		cout << "Case #" << I+1 << ": ";
		printf("%.6lf %.6lf", dmin, tmin);
		cout << endl;
	}

	return 0;
}