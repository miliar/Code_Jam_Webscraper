//============================================================================
// Name        : C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int t=0, T;
	cin >>T;
	while(t<T){
		t++;
		int min=2000000, res=0, sum=0, n=0,N,C;
		cin >> N;
		while(n<N){
			n++;
			cin >>C;
			res = res xor C;
			if(C < min) min=C;
			sum+=C;
		}
		cout << "Case #" << t << ": ";
		if(res==0)
			cout << sum-min << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}
