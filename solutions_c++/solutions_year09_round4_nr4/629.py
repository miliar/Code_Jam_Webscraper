#include<iostream>
#include<fstream>
#include<cmath>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
using namespace std;
double x[50];
double y[50];
double r[50];

double computeTwo(int a, int b){
	double d=sqrt((x[a]-x[b])*(x[a]-x[b]) + (y[a]-y[b])*(y[a]-y[b]));
	d+=r[a]+r[b];
	return d/2;
}


int main(){
	freopen("C.out", "w", stdout);
	int ca,n;
	cin>>ca;
	
	for(int cas=1; cas<=ca; ++cas){
		cin>>n;
		for(int i=0; i<n; ++i){
			cin>>x[i]>>y[i]>>r[i];
		}
		if(n==1){
			printf("Case #%d: %.6f\n", cas, r[0]);
		}
		if(n==2){
			printf("Case #%d: %.6f\n", cas, MAX(r[0], r[1]));
		}
		if(n==3){
			double min=(double)(1<<30);
			min=MIN(min, MAX(r[0], computeTwo(1,2)));
			min=MIN(min, MAX(r[1], computeTwo(2,0)));
			min=MIN(min, MAX(r[2], computeTwo(0,1)));
			printf("Case #%d: %.6f\n", cas, min);
		}
	}
}
