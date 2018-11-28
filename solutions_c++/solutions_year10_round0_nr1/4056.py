#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(){
	fstream inFile("A.in",fstream::in);
	fstream outFile("yyy",fstream::out);
	
	long long int T,N,K;
	inFile>>T;
	for (int i=0;i<T;i++){
		inFile>>N>>K;
		int m=pow(2,N);
		bool light= K%m==m-1;
		outFile<< "Case #"<<i+1<<": ";
		if (light)
			outFile<<"ON\n";
		else
			outFile<<"OFF\n";
	}
}
