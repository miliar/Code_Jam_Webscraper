#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>
#include<set>
#include<cmath>
#define pi 3.141592653589793238462643383279502884

using namespace std;
double dist(int x1, int y1, int x2, int y2){
	double res=sqrt(double(x1-x2)*(x1-x2)+double(y1-y2)*(y1-y2));
	return res;
}
double ar(int x1, int y1, int x2, int y2, int x, int y){
	double res=0;
	if((x==x1 && y==y1) || (x==x2 && y==y2))return 0;
	double tri = fabs(0.5*(-(double)x2*y1+x*y1+x1*y2-x*y2-x1*y+x2*y));
	double s1 = dist(x,y,x2,y2);
	double s2 = dist(x,y,x1,y1);
	double s3 = dist(x1,y1,x2,y2);
	double a1 = asin(2*tri/s2/s3) *s2*s2/2;
	double a2 = asin(2*tri/s1/s3) *s1*s1/2;
	double c1 =((s2*s2+s3*s3-s1*s1)/2/s2/s3);
	double c2 =((s1*s1+s3*s3-s2*s2)/2/s1/s3);
//cout<<c1<<" "<<c2<<"\n";
	if(c1<0)a1 = pi*s2*s2/2-a1;
	if(c2<0)a2 = pi*s1*s1/2-a2;
	res=2*(a2+a1-tri);
	return res;
}
int main(){
	int C, N, M;
	cin>>C;
	for(int i=0; i<C; i++){
		//cin>>wrds[i]; 
		cin>>N>>M;
		vector<int> xg(N), yg(N), xb(M), yb(M);

		for(int j=0; j<N; j++){
			cin>>xg[j]>>yg[j];

		}
		for(int j=0; j<M; j++){
			cin>>xb[j]>>yb[j];

		}
		vector<double> res(M);
//cout<<M;
		for(int j=0; j<M; j++){
			res[j] = ar(xg[0],yg[0],xg[1],yg[1], xb[j],yb[j]);
		}
		cout.precision(15);
		cout<<"Case #"<<i+1<<": "<<fixed ;
		for(int j=0; j<M; j++){
			cout<<res[j]<<" ";
		}
		cout<<"\n";
	}
	
}
