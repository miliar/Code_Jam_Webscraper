#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;
#define EPS 1e-9
#define MAXT 1e+20
#define LL long long
LL p[200], v[200];
int main(){
	int t;
	ifstream fin("B-large.in");
	ofstream fout("b2.out");
	fin >> t;
	for(int i = 0; i < t; i++){
		int c;
		LL d;
		fin >> c >> d;
		for(int i = 0; i < c; i++)
			fin >> p[i] >> v[i];
		double l = 0, h = MAXT;
		for(int i = 0; i < 200; i++){
			double mid = (l + h) / 2.;
			double p1 = p[0] - mid;
			int fl = 0;
			for(int i = 0; i < c && !fl; i++){
				p1 = max(p1, (double)p[i] - mid);
				double p2 = p1 + (v[i] - 1) * d;
				if(fabs(p2 - p[i]) > (mid + EPS)){
					fl = 1;
				}
				p1 = p2 + d;
			}
			if(!fl)
				h = mid;
			else
				l = mid;
		}
		fout.flags(ios::fixed);
		fout.precision(8);
		fout << "Case #" << i + 1 << ": ";
		fout << l << endl;
	}
	return 0;
}