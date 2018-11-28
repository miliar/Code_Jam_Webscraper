#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

#define PI 2*acos(0.0)
#define eps 1e-8
#define eps2 1e-8

double area(double x1, double y1, double x2, double y2, double r)
{
	//cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
	if ((x2-x1)*(y2-y1) < eps2) return 0;
	double rr = r*r;
	bool a = x1*x1+y1*y1 <= rr+eps;
	bool b = x1*x1+y2*y2 <= rr+eps;
	bool c = x2*x2+y1*y1 <= rr+eps;
	bool d = x2*x2+y2*y2 <= rr+eps;

	if (a&&b&&c&&d) return (x2-x1)*(y2-y1);
	if (!a&&!b&&!c&&!d) return 0;

	return area(x1,y1,(x2+x1)/2,(y2+y1)/2, r) + area((x2+x1)/2,y1,x2,(y2+y1)/2, r) +
		area(x1,(y2+y1)/2,(x2+x1)/2,y2, r) + area((x2+x1)/2,(y2+y1)/2,x2,y2, r);
}

double area2(double x1, double y1, double x2, double y2, double r)
{
	//cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
	double rr = r*r;
	bool a = x1*x1+y1*y1 <= rr+eps;
	bool b = x1*x1+y2*y2 <= rr+eps;
	bool c = x2*x2+y1*y1 <= rr+eps;
	bool d = x2*x2+y2*y2 <= rr+eps;

	if (a&&b&&c&&d) return (x2-x1)*(y2-y1);
	else if (!a&&!b&&!c&&!d) return 0;

	else if (a&&!b&&!c&&!d) {
		double yy = sqrt(rr-x1*x1);
		double xx = sqrt(rr-y1*y1);
		double l = sqrt( (yy-y1)*(yy-y1) + (xx-x1)*(xx-x1));
		double ang = acos(1-l*l/(2*r*r));
		double sa = sin(ang);
		//cout << "a " << 0.5*(yy-y1)*(xx-x1) + (0.5*rr*(ang-sa)) << endl;
		return 0.5*(yy-y1)*(xx-x1) + (0.5*rr*(ang-sa));
	}
	else if (a&&!b&&c&&!d) {
		double yy1 = sqrt(rr-x1*x1);
		double yy2 = sqrt(rr-x2*x2);
		double l = sqrt( (yy1-yy2)*(yy1-yy2) + (x2-x1)*(x2-x1));
		double ang = acos(1-l*l/(2*r*r));
		double sa = sin(ang);
		//cout << "b " << 0.5*(yy1+yy2-y1-y1)*(x2-x1) + (0.5*rr*(ang-sa)) << endl;
		return 0.5*(yy1+yy2-y1-y1)*(x2-x1) + (0.5*rr*(ang-sa));
	}
	else if (a&&b&&!c&&!d) {
		double xx1 = sqrt(rr-y1*y1);
		double xx2 = sqrt(rr-y2*y2);
		double l = sqrt( (y1-y2)*(y1-y2) + (xx2-xx1)*(xx2-xx1));
		double ang = acos(1-l*l/(2*r*r));
		double sa = sin(ang);
		//cout << "c " << 0.5*(xx1+xx2-x1-x1)*(y2-y1) + (0.5*rr*(ang-sa)) << endl;
		return 0.5*(xx1+xx2-x1-x1)*(y2-y1) + (0.5*rr*(ang-sa));
	}
	else if (a&&b&&c&&!d) {
		double yy = sqrt(rr-x2*x2);
		double xx = sqrt(rr-y2*y2);
		double l = sqrt( (yy-y2)*(yy-y2) + (xx-x2)*(xx-x2));
		double ang = acos(1-l*l/(2*r*r));
		double sa = sin(ang);
		//cout << "d " << (y2-y1)*(x2-x1) - 0.5*(yy-y2)*(xx-x2) + (0.5*rr*(ang-sa)) << endl;
		return (y2-y1)*(x2-x1) - 0.5*(yy-y2)*(xx-x2) + (0.5*rr*(ang-sa));
	}

	return 0;
}



int main()
{
	int N;
	double f, R, t, r, g;

	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	//ifstream fin("C-large.in");
	//ofstream fout("C-large.out");


	fin >> N;

	for (int tc = 1; tc <= N; ++tc)
	{
		fin >> f >> R >> t >> r >> g;

		double res = 0, S = PI*R*R;
		if (R-t-f < eps || g-2*f < eps) 
			res = 0;
		else {
			double x = r+f, y = r+f, dif = g-f-f;

			while (x*x+y*y < (R-t-f)*(R-t-f)+eps)
			{
				while (x*x+y*y < (R-t-f)*(R-t-f)+eps)
				{
					//double z = area(x, y, x+dif, y+dif, R-t-f), zz = area2(x, y, x+dif, y+dif, R-t-f);;
					res += 4*area2(x, y, x+dif, y+dif, R-t-f);
					x += g + r + r;
				}
				x = r+f;
				y += g + r + r;
			}
		}

		fout << "Case #" << tc << ": " << 1-(res/S) << endl;
	}

	fin.close();

	return 0;
}