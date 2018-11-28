#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
#include <iomanip>

using namespace std;

int T;

struct FF
{
	int x,y,z;
	int vx,vy,vz;
};

vector<vector<FF>> tests;

int input_read(char * filename)
{
	ifstream ifs;
	ifs.open(filename, ios::in);
    
    ifs >> T;

	for(int i=0; i<T; ++i){
		int N;
		ifs >> N;
		vector<FF> ffs;
		for(int j=0; j<N; ++j){
			FF f;
			ifs >> f.x >> f.y >> f.z >> f.vx >> f.vy >> f.vz;
			ffs.push_back(f);
		}
		tests.push_back(ffs);
	}

	return 0;
}

struct result{double d,t;};

result solve(vector<FF> &ffs)
{
	double d=0,t=0;
	int len = ffs.size();

	double sum_x=0, sum_y=0, sum_z=0;
	double sum_vx=0, sum_vy=0, sum_vz=0;
	for(int i = 0; i < len; ++i){
		sum_x += ffs[i].x;
		sum_y += ffs[i].y;
		sum_z += ffs[i].z;
		sum_vx += ffs[i].vx;
		sum_vy += ffs[i].vy;
		sum_vz += ffs[i].vz;
	}

	double tL = sum_vx*sum_vx + sum_vy*sum_vy + sum_vz*sum_vz; 
	double tR = sum_x*sum_vx + sum_y*sum_vy + sum_z*sum_vz;

//	cout << "tLtR" << tL << " " << tR << endl; 
	if(-0.00000001<tL && tL<0.00000001){
		t=0;
	}else{
		t = -tR/tL;
		if(t<0){t=0.0;}
	}

	double d2=0.0;
	double sum_xt = 0;
	double sum_yt = 0;
	double sum_zt = 0;
	for(int i = 0; i < len; ++i){
		sum_xt += ffs[i].x + ffs[i].vx * t;
		sum_yt += ffs[i].y + ffs[i].vy * t;
		sum_zt += ffs[i].z + ffs[i].vz * t;
	}
	d2 = sum_xt*sum_xt + sum_yt*sum_yt + sum_zt*sum_zt;
	d = sqrt(d2 / (len*len));

	result r = {d,t};
	return r;
}

#define INFILE "B-large.in"

int main(){
	input_read(INFILE);
	ofstream o(INFILE ".out");

	int n = 0;
	char buf[1000];
//#define o cout
	for(vector<vector<FF>>::iterator i = tests.begin(), e = tests.end(); i != e; ++i){
		result r = solve(*i);
		sprintf(buf,"%.8f %.8f", r.d, r.t);
		o << "Case #" << ++n << ": " << buf << endl;
//		o << "Case #" << ++n << ": " << r.d << " " << r.t << endl;
	}
}
