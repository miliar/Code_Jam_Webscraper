//============================================================================
// Name        : RopeIntranet.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int A[1000];
int B[1000];

int main() {
	int ntc;
	cin >> ntc;
	for(int ci=0;ci<ntc;ci++){
		int N;
		cin >> N;
		for(int i=0;i<N;i++){
			cin >> A[i] >> B[i];
		}
		int res=0;
		for(int i=0;i<N;i++){
			for(int j=1;j<N;j++){
				if(A[i]>A[j] && B[i]<B[j])
					res++;
				if(A[i]<A[j] && B[i]>B[j])
					res++;
			}
		}
		cout << "Case #"<<ci+1<<": "<<res<<endl;
	}
	return 0;
}
