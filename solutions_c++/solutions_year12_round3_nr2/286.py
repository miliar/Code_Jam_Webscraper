//============================================================================
// Name        : car.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <math.h>
#include <iomanip>
using namespace std;
//N=2
int main() {
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
	double D; int N,A;
	cin>>D>>N>>A;

	vector<long double> x(N), t(N), a(A);
	for(int in=0;in<N;in++)
	{cin>>t[in]>>x[in];}
	for(int ia=0;ia<A;ia++)
		cin>>a[ia];
	cout<<"Case #"<<i+1<<":"<<endl;
	for(int ia=0;ia<A;ia++)
	{
		long double tc=sqrt(2.0*D/a[ia]);
		long double tcar;
		if (N==1) tcar=tc;
		else{
		long double Vx=(x[1]-x[0])/(t[1]-t[0]);
		if(D<=x[0]+(Vx)*tc)
			tcar=tc;
		else tcar=(D-x[0])/Vx;}
	cout<<fixed<<setprecision(7)<<tcar<<endl;
	}

	}
	return 0;
}
