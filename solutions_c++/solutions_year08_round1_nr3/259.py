#include<fstream>
#include<string>
#include<iostream>
#include<math.h>

using namespace std;

ifstream filein1("c.out");
ifstream filein("c.in");
ofstream fileout("c.out2");

int main(){
	double a = (pow(5.0,0.5)+1.0)/2;
	int i,t,k,n;
	__int64 j;
	double b = 2*(a+1);
	filein>>t;
	int ar[31];
	for(i = 1;i<31;i++)filein1>>ar[i];
	for(i = 0;i<t;i++){
		filein>>k;
		int j2=ar[k];
		if(j2<100 && j2>9) fileout<<"Case #"<<i+1<<": "<<'0'<<j2<<endl;
		else if(j2<10) fileout<<"Case #"<<i+1<<": "<<'0'<<'0'<<j2<<endl;
		else fileout<<"Case #"<<i+1<<": "<<j2<<endl;
	}
	return 0;
}