#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define stoi(i,s) {istringstream is(s); is>>i;}

string intToStr(int k){
	ostringstream os;
	os << k;
	return os.str();
}


int main(int argc, char *argv[])
{
	int i,j,k;
	ifstream fin("B-large.in");
	string ss;
	getline(fin,ss);
	int T;
	int N;
	long long x,y,z,vx,vy,vz;
	long long sx,sy,sz,svx,svy,svz;
	long long a,b,c;
	double t,d,d2;
	stoi(T,ss);
	for(i=1;i<=T;i++){
		sx=0;sy=0;sz=0;svx=0;svy=0;svz=0;
		getline(fin,ss);
		stoi(N,ss);
		for(j=0;j<N;j++){
			getline(fin,ss);
			istringstream is(ss);
			is>>x>>y>>z>>vx>>vy>>vz;
			sx += x;
			sy += y;
			sz += z;
			svx += vx;
			svy += vy;
			svz += vz;
		}
		a = sx*sx+sy*sy+sz*sz;
		b = sx*svx+sy*svy+sz*svz;
		c = svx*svx+svy*svy+svz*svz;
		if(b>=0)
			t = 0;
		else
			t = -((double)b/(double)c);
		d2 = a+2*b*t+c*t*t+0.000000001;
		d = sqrt(d2)/N;
		printf("Case #%d: %.8f %.8f\n",i,d,t);
	}
    //system("PAUSE");
    return EXIT_SUCCESS;
}
