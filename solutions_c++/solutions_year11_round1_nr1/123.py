#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int gcd(int a, int b);

int main(){
	ofstream fout ("g11r1aa.out");
	ifstream fin ("g11r1aa.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		double n;
		int pd, pg;
		bool good=true;
		fin>>n>>pd>>pg;
		if((pg==100 && pd!=100) || (pg==0 && pd!=0) || (100/gcd(100, pd)>n))
			good=false;
		fout<<"Case #"<<caseNum+1<<": ";
		if(good)
			fout<<"Possible"<<endl;
		else
			fout<<"Broken"<<endl;
	}
	return 0;
}

int gcd(int a, int b){
	if(a<b)
		return gcd(b, a);
	if(b==0)
		return a;
	return gcd(b, a%b);
}
