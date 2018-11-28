#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

typedef long long ll;
int C, A, N, M;

ifstream fin("b1.in");
ofstream fout("b1.out");

void _solve(){
	
	for (int x1=0; x1<=N; ++x1)
	for (int y1=0; y1<=M; ++y1){
		double a = sqrt(x1*x1+y1*y1);
		for (int x2=0; x2<=N; ++x2)
		for (int y2=0; y2<=M; ++y2){
			double b = sqrt(x2*x2+y2*y2);
			double c = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
			
			double s = (a+b+c)/2;
			
			s = sqrt(s*(s-a)*(s-b)*(s-c)) * 2;
			
			if (abs(s-A)<1e-4){
				fout<<"0 0 "<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<endl;
				return;
			}
		}
	}
	
	fout<<"IMPOSSIBLE"<<endl;
}

int main(){
	
	fin>>C;
	for (int Case=1; Case<=C; ++Case){
		fin>>N>>M>>A;
		
		fout<<"Case #"<<Case<<": ";
		_solve();				
	}
}
