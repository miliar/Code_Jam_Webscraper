#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

double width(int P[5000][2], double r[5000], int N, double y){
	double lo=-100000, hi=100000;
	for(int i=0; i<N; i++){
		if(y<=P[i][1]-r[i] || y>=P[i][1]+r[i])
			return 0;
		double dx=sqrt(r[i]*r[i]-(y-P[i][1])*(y-P[i][1]));
		double x1=P[i][0]-dx, x2=P[i][0]+dx;
		if(lo<x1)
			lo=x1;
		if(hi>x2)
			hi=x2;
		if(lo>=hi)
			return 0;
	}
	return hi-lo;
}

double integrate(int P[5000][2], double r[5000], int N, double ys, double ye){
	double w1=width(P, r, N, ys), w2=width(P, r, N, ye);
	double ym=(ys+ye)/2;
	if((w1>0 || w2>0) && ye-ys>.5)
		return integrate(P, r, N, ys, ym)+integrate(P, r, N, ym, ye);
	if(abs(w1-w2)*(ye-ys)<1e-8){
		return (w1+w2)/2*(ye-ys);
	}
	//debug(w1);
	//debug(w2);
	//debug(ys);
	//debug(ye);
	if(w1==0 || w2==0 || w1/w2>1.0001 || w1/w2<.9999)
		return integrate(P, r, N, ys, ym)+integrate(P, r, N, ym, ye);
	return (w1+w2)/2*(ye-ys);
}

void eval(){
	int N, M;
	cin>>N>>M;
	int P[5000][2], Q[1000][2];
	double A[1000];
	for(int i=0; i<N; i++)
		cin>>P[i][0]>>P[i][1];
	for(int i=0; i<M; i++)
		cin>>Q[i][0]>>Q[i][1];
	for(int w=0; w<M; w++){
		int qx=Q[w][0], qy=Q[w][1];
		double r[5000];
		for(int i=0; i<N; i++)
			r[i]=hypot(P[i][0]-qx, P[i][1]-qy);
		A[w]=0;
		for(int i=0; i<200; i++){
			A[w]+=integrate(P, r, N, qy+i*.005, qy+(i+1)*.005);
			A[w]+=integrate(P, r, N, qy-(i+1)*.005, qy-i*.005);
		}
		A[w]+=integrate(P, r, N, qy+1, 1000000);
		A[w]+=integrate(P, r, N, -1000000, qy-1);
	}
	for(int i=0; i<M; i++)
		printf("%.7lf ", A[i]);
	cout<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
