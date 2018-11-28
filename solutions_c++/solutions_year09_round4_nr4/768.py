#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <cmath>
using namespace std;

ifstream fin("infile.in");
ofstream fout("outfile.out");

const int SIZE = 3;
double X[SIZE], Y[SIZE], R[SIZE];
const double INF = 1000.0*1000.0;



double getMinRadius(int p1, int p2) {
	double dx = X[p1]-X[p2];
	double dy = Y[p1]-Y[p2];
	double d = sqrt(dx*dx + dy*dy);

	d += R[p1]+R[p2];
	return d/2;
}


int main()
{
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int N; fin>>N;
		for(int i=0; i<N; i++)
			fin>>X[i]>>Y[i]>>R[i];
		
		double minRadius = INF;
		if(N==1)
			minRadius = R[0];
		else if(N==2) {
			minRadius = ((R[0]>R[1])?R[0]:R[1]);
		}
		else if(N==3) {
			int others[3][2] = { {1,2}, {0,2}, {0,1} };

			for(int lonePlant=0; lonePlant<N; lonePlant++) {
				double r = getMinRadius(others[lonePlant][0], others[lonePlant][1]);
				r = (r>R[lonePlant])?r:R[lonePlant];
				minRadius = (r<minRadius)?r:minRadius;
			}
		}
		else
			cout<<"N>3"<<endl;

		fout<<"Case #"<<t<<": "<<fixed<<setprecision(6)<<minRadius<<endl;
	}

	return 0;
}