#include<iostream>
#include<vector>
#include<iomanip>
#include<math.h>
#include<fstream>


using namespace std;

int main(){
	ifstream ifile("input1.txt");
	ofstream ofile("out.txt");

	int t,i1=0;
	ifile>>t;
	while(i1++<t){
		int n;
		ifile>>n;
		vector<double> x,y,z,vx,vy,vz;
		for(int i = 0 ; i < n ; i++){
			double x1,y1,z1,vx1,vy1,vz1;
			ifile>>x1>>y1>>z1>>vx1>>vy1>>vz1;
			x.push_back(x1);
			y.push_back(y1);
			z.push_back(z1);
			vx.push_back(vx1);
			vy.push_back(vy1);
			vz.push_back(vz1);
		}

		double cx=0,cy=0,cz=0,cvx=0,cvy=0,cvz=0;
		for(int n = 0 ; n < x.size() ; n++){
				cx += x[n];
				cy += y[n];
				cz += z[n];
				cvx += vx[n];
				cvy += vy[n];
				cvz += vz[n];
			}
			cx /= (double)n;
			cy /= (double)n;
			cz /= (double)n;
			cvx /= (double)n;
			cvy /= (double)n;
			cvz /= (double)n;
			double t1;
			if((cvx*cvx + cvy*cvy + cvz*cvz) == 0) t1 = 0;
			else 
				t1 = -(double)(cx*cvx + cy*cvy + cz*cvz) / (double)(cvx*cvx + cvy*cvy + cvz*cvz);
			if(t1 <= 0) t1 = 0;

		double dis = sqrt( pow((cx + cvx*t1),2) + pow((cy + cvy*t1),2) + pow((cz + cvz*t1),2) );
		ofile<<setprecision(8)<<fixed;
		ofile<<"Case #"<<i1<<": "<<dis<<" "<<t1<<"\n";
	}
}