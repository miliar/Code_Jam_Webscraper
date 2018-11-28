#include <iostream>
#include <cmath>

using namespace std;

typedef unsigned long long uint64;

int main(){
	int cases = 0;
	cin>>cases;
	for(int i = 0; i < cases; i++){
		uint64 N = 0, K = 0;
		cin>>N>>K;		
		uint64 stepSize = uint64(pow(long double(2), long double(N)));
		uint64 startingPoint = stepSize - 1;		
		uint64 difference = K - startingPoint;
		if(difference % stepSize == 0)	cout<<"Case #"<<i+1<<": "<<"ON"<<endl;
		else	cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;		
	}
	return 0;
}
