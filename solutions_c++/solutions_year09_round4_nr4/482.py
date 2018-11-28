#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <math.h>
#include <queue>
#include <list>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <fstream>
using namespace std;

#define abs(A) (((A)>=0)?(A):(-(A)))
#define present(c,x) (find(c.begin(),c.end(),x) != (c).end())
#define pb push_back
template<class A, class B> A cvt(B x) { stringstream s; s<<x; A r; s>>r; return r; }
typedef long long int64;

int tests;
int n;
int t[50];

typedef struct {
	double x; double y; double r;
} point;

bool operator<(point p1, point p2) {
	return make_pair(p1.x,p1.y)<make_pair(p2.x,p2.y);
}

double dist(point p1, point p2) {
	double dx=p1.x-p2.x, dy=p1.y-p2.y;
	return sqrt(dx*dx+dy*dy);
}

int main() {
	ifstream fin("D-small-attempt1.in");
	FILE *fout=fopen("D-small-attempt1.out","w");
	//FILE *fout=stdout;
	fin >> tests;
	for (int test=1;test<=tests;test++) {
		fin >> n;
		fprintf(fout,"Case #%d: ",test);
		vector<point> p;
		int x,y,r;
		for (int i=0;i<n;i++) {
			fin >> x >> y >> r;
			p.push_back((point){x,y,r});
		}
		if (n==1) {
			fprintf(fout,"%.8lf\n",p[0].r);
		} else if (n==2) {
			fprintf(fout,"%.8lf\n",max(p[0].r,p[1].r));
		} else if (n==3) {
			//0,1
			double r1 = max((dist(p[0],p[1])+p[0].r+p[1].r)/2, 1.0*p[2].r);
			//0,2
			double r2 = max((dist(p[0],p[2])+p[0].r+p[2].r)/2, 1.0*p[1].r);
			//1,2
			double r3 = max((dist(p[1],p[2])+p[1].r+p[2].r)/2, 1.0*p[0].r);
			fprintf(fout,"%.8lf\n",min(r1,min(r2,r3)));
		}
	}
    return 0;
}
