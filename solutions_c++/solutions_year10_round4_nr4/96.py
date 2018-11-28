/*
 *  D.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۳/۱۵.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <iomanip>
#include <complex>
#define X real()
#define Y imag()
#define eq(a,b) (abs((a)-(b))<eps)
using namespace std;
typedef complex<double> Complex;

const int MaxN= 20;
const double eps= 1e-8;
Complex A, B, M;
double res[MaxN], AB, AM, BM;

double angle(Complex A, Complex M, Complex B){
	A-= M;
	B-= M;
	M-= M;
	B/= A;
	return arg(B);
}
/*********************************/
int main(){
	int test;
	cin >> test;
	cout << fixed << setprecision(7) ;
	for (int t=1 ; t<=test; t++){
		int n, m;
		cin >> n >> m;
		cin >> A.X >> A.Y >> B.X >> B.Y;
		AB= abs(A - B);
		for (int i=0 ; i<m ; i++){
			cin >> M.X >> M.Y;
			AM= abs(A-M);
			BM= abs(B-M);
			if (AM>BM){
				swap(AM, BM);
				swap(A, B);
			}
			if (abs(angle(B, A, M)) < (M_PI/2 - eps)){
				double alfa= abs(2* angle(A, B, M));
				double ghetaa= BM*BM * alfa /2;
				double tikke= ghetaa - (BM*BM * sin(alfa)/2);
				alfa= abs(2*angle(B, A, M));
				ghetaa= AM*AM*alfa/2;
				tikke+= ghetaa - (AM*AM*sin(alfa)/2);
				res[i]= tikke;
			}else if (eq(BM, AB+AM)){
				res[i]= AM*AM*M_PI;
			}else if (eq(abs(angle(B, A, M)), M_PI/2)){
				double alfa= abs(2*angle(A, B, M));
				double ghetaa= BM*BM * alfa/2;
				double tikke= ghetaa - (BM*BM*sin(alfa)/2);
				tikke+= AM*AM*M_PI/2;
				res[i]= tikke;
			}else{
				double alfa= abs(2*angle(B, A, M));
				double tikke= AM*AM*alfa/2;
				alfa= 2*M_PI - alfa;
				tikke+= AM*AM*sin(alfa)/2;
				alfa= abs(2*angle(A,B,M));
				double ghetaa= BM*BM*alfa/2;
				tikke+= ghetaa - (BM*BM*sin(alfa)/2);
				res[i]= tikke;
			}
		}
		printf("Case #%d: ", t);
		for (int i=0 ; i<m ; i++)
			cout << res[i] << ' ';
		cout << endl;
		
	}
	return 0;
}

