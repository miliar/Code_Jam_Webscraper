#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

int n;

double S,R,time,X;

int W[110];

int main()
{
	int test,t,i,j;
	double start,end;

	int w;

	double answer;

	in >> test;

	for (t = 1; t <= test; ++t)
	{
		for (i = 0 ; i < 110; ++i)
			W[i] = 0;
		
		answer = 0.0;

		in >> X >> S >> R >> time >> n;

		/*double jamanak = 0.0;

		bool f = true;

		double gumar = 0;

		for (i = 0 ; i < n; ++i)
		{
			in >> start >> end >> w;
			gumar += (end - start);

			if (f)
			{
				double jam = jamanak;

				jamanak += (end - start)/(R + w);

				if (jamanak > time)
				{
					double U = (time - jam)*(R + w);
					jamanak = time + (end - start - U)/(S + w);
					f = false;
				}
			}
			else
			{
				jamanak += (end - start)/(S + w);
			}
		}

		gumar = X - gumar;


		if (f)
		{
			double jam = jamanak;

			jamanak += (gumar)/(R);

			if (jamanak > time)
			{
				double U = (time - jam)*(R);
				cout << gumar << " " << U << endl;
				jamanak = time + (gumar - U)/(S);
				f = false;
			}
		}
		else
		{
			jamanak += (gumar)/(S);
		}*/

		double gumar = 0.0;

		bool f = true;

		for (i = 0 ; i < n; ++i)
		{
			in >> start >> end >> w;
			gumar += (end - start);
			W[w] += (end - start);
		}

		gumar = X - gumar;

		W[0] += gumar;

		double jamanak = 0.0;

		for (i = 0; i < 110; ++i)
		{

			if (f)
			{
				double jam = jamanak;

				jamanak += (W[i])/(R + i);

				if (jamanak > time)
				{
					double U = (time - jam)*(R + i);
					jamanak = time + (W[i] - U)/(S + i);
					f = false;
				}
			}
			else
			{
				jamanak += (W[i])/(S + i);
			}

		}


		out << setiosflags(ios::fixed | ios::showpoint);
		out << "Case #" << t << ": " << setprecision(9) << jamanak << endl;
	}

	return 0;
}