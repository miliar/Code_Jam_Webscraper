#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

double dist(double x1, double x2, double y1, double y2){
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main() {
	ofstream fout ("google2d.out");
	ifstream fin ("google2d.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int length;
		fin>>length;
		double xs[3], ys[3], rs[3];
		fout.precision(10);
		for(int n=0; n<length; n++)
			fin>>xs[n]>>ys[n]>>rs[n];
		if(length==1)
			fout<<"Case #"<<caseNum+1<<": "<<rs[0]<<endl;
		if(length==2)
			fout<<"Case #"<<caseNum+1<<": "<<max(rs[0],rs[1])<<endl;
		if(length==3){
			double minDist=min((rs[0]+rs[1])/2+dist(xs[0], xs[1], ys[0], ys[1])/2, (rs[0]+rs[2])/2+dist(xs[0], xs[2], ys[0], ys[2])/2);
			minDist=min(minDist, (rs[2]+rs[1])/2+dist(xs[2], xs[1], ys[2], ys[1])/2);
			if(minDist<rs[0])
				minDist=rs[0];
			if(minDist<rs[1])
				minDist=rs[1];
			if(minDist<rs[2])
				minDist=rs[2];
			fout<<"Case #"<<caseNum+1<<": "<<minDist<<endl;
		}
	}
	return 0;
}
