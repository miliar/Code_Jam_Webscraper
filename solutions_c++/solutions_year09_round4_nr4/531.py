#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
using namespace std;

vector<double> rad;
vector<double> x;
vector<double> y;

double dist(double x1, double y1, double x2, double y2){
	double a=x1-x2;
	double b=y1-y2;
	return hypot(a,b);
}

main(){
	ofstream fout ("D-small.out");
	ifstream fin ("D-small.in");
	int C;
	fin>>C;
	for (int k=0;k<C;k++){
		int N;
		fin>>N;
		rad.clear();
		rad.resize(N,0);
		y.clear();
		y.resize(N,0);
		x.clear();
		x.resize(N,0);
		for(int i=0;i<N;i++){
			fin>>x[i]>>y[i]>>rad[i];
		}

		if (N==1){
			fout<<"Case #"<<k+1<<": "<<rad[0]<<endl;
		}
		else if (N==2){
			fout<<"Case #"<<k+1<<": "<<max(rad[0],rad[1])<<endl;
		}
		else{
			double min=10000;
			
			double pom;
			pom=(dist(x[0],y[0],x[1],y[1])+rad[0]+rad[1])/2;
			pom=max(pom,rad[2]);
			if (pom<min) min=pom;

			pom=(dist(x[0],y[0],x[2],y[2])+rad[0]+rad[2])/2;
			pom=max(pom,rad[1]);
			if (pom<min) min=pom;

			pom=(dist(x[2],y[2],x[1],y[1])+rad[2]+rad[1])/2;
			pom=max(pom,rad[0]);
			if (pom<min) min=pom;

			fout<<"Case #"<<k+1<<": "<<min<<endl;
		}
	}
	fout.close();
}
