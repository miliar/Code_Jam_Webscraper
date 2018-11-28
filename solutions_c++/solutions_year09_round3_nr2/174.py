#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <math.h>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;

double dist(double x, double y, double z) {
	double x0 = double(x);
	double y0 = double(y);
	double z0 = double(z);
	return sqrt(x0*x0 + y0*y0 + z0*z0);
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("file.out");
	
	int T;
	fin >> T;
	fout.precision(8);
	for (int testCase = 1; testCase <= T; ++testCase) {
		fout << "Case #" << testCase << ": ";
		int N;
		fin >> N;
		ll x0 = 0,y0 = 0,z0 = 0,vx0 = 0,vy0 = 0,vz0 = 0;
		for (int i = 0; i < N; ++i) {
			ll tx,ty,tz,tvx,tvy,tvz;
			fin >> tx >> ty >> tz >> tvx >> tvy >> tvz;
			x0 += tx;
			y0 += ty;
			z0 += tz;
			vx0 += tvx;
			vy0 += tvy;
			vz0 += tvz;
		}
		double x = double(x0) / N;
		double y = double(y0) / N;
		double z = double(z0) / N;
		double vx = double(vx0) / N;
		double vy = double(vy0) / N;
		double vz = double(vz0) / N;
		double OA = dist(x, y, z);
		if (vx0*vx0 + vy0*vy0 + vz0*vz0 == 0) {
			fout << fixed << OA << ' ' << 0.0 << endl;
			continue;
		}
		double r = (-x * vx - y*vy - z*vz)/((double)(vx*vx+vy*vy+vz*vz));
		if (r < 0) {
			fout << fixed << OA << ' ' << 0.0 << endl;
		}
		else {
			fout << fixed << dist(x + r*vx, y + r*vy, z + r*vz) << ' ' << r << endl;
		}
	}
	return 0;
}
