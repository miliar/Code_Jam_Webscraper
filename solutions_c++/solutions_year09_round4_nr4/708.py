// codejam.cpp : Defines the entry point for the console application.
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <math.h>



using namespace std;

typedef long long int64;
#define For(i,n) for (i=0;i<n;i++) 

int i,j,k,n,m,tests,t,kol;

string s;


string itos(int64 a) {stringstream s; s<<a; return s.str();}
int64 stoi(string a) {stringstream s; s<<a; int64 b; s>>b; return b;}
string dtos (double a){char buf[100]; sprintf(buf,"%.3",a); return string(buf);}
double stod(string a) {stringstream s; s<<a; double b; s>>b; return b;}


int gcd(int a, int b){
	while(true){
		if (a==0) return b;
		if (b==0) return a;
		if (a>b)
			a = a - b*(a/b);
		else
			b = b - a*(b/a);
	}
}


int main()
{

	ifstream inp("D-small-attempt0.in");
	ofstream out("D-small-attempt0.out");

	inp>>tests;
	For(t,tests){
		out<<"Case #"<<t+1<<": ";
		
		int X[3],Y[3],R[3];
		inp>>n;
		For(i,n)
			inp>>X[i]>>Y[i]>>R[i];
	
		if (n==1){
			out<<R[0]<<endl;
			continue;
		}
		if (n==2){
			out<<max(R[0],R[1])<<endl;
			continue;
		}
		
		int sumr=0;
		For(i,3) 
			sumr = sumr + R[i];
		
		double best = 1e10;

		For(i,3)
			for (j=i+1; j<3; j++){
				double r1 = R[i]+R[j]+ sqrt( (double)( (X[i]-X[j])*(X[i]-X[j]) + (Y[i]-Y[j])*(Y[i]-Y[j])));
				r1 = r1/2;
				double r2 = sumr-(R[i]+R[j]);
				best = min(best,max(r1,r2)); 
			}
		out.precision(11);
		out<<best<<endl;

	}


return 0;
}

