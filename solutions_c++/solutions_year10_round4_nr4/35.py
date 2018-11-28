#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

#define x first
#define y second

const double pi = 3.1415926535897932384626433832795;

pair<int,int> goat[2];
pair<int,int> buck[2];

double dist(pair<int,int> a, pair<int,int> b){
	double adx = a.x-b.x;
	double ady = a.y-b.y;
	return sqrt(adx*adx+ady*ady);
}

int main(){
	int n,m;
	int T;
	int testcase = 0;
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&T);
	while(T-- > 0 ){
		++testcase;
		scanf("%d%d",&n,&m);
		int i;
		for(i=0;i<n;i++){
			scanf("%d%d",&goat[i].x,&goat[i].y);
		}
		for(i=0;i<m;i++){
			scanf("%d%d",&buck[i].x,&buck[i].y);
		}

		printf("Case #%d:",testcase);
		for(i=0;i<m;i++){
			double r1 = dist(goat[0],buck[i]);
			double r2 = dist(goat[1],buck[i]);
			double r = dist(goat[0],goat[1]);
			if(fabs(r) < 1e-8){
				printf(" %.12lf\n",pi*r1*r1);
			}
			if(fabs(r1) < 1e-8){
				printf(" %.12lf\n",(double) 0.0);
			}
			if(fabs(r2) < 1e-8){
				printf(" %.12lf\n",(double) 0.0);
			}
			double c1 = (r*r+r1*r1-r2*r2)/(2*r*r1);
			double c2 = (r*r+r2*r2-r1*r1)/(2*r*r2);
			double a1 = acos(c1);
			double a2 = acos(c2);
			double A1 = r1*r1*a1 - r1*r1*c1*sin(a1);
			double A2 = r2*r2*a2 - r2*r2*c2*sin(a2);
			printf(" %.12lf",A1+A2);
		}
		printf("\n");
	}
	return 0;
}
