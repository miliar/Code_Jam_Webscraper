/*
 * SnapperChain.cpp
 *
 *  Created on: May 8, 2010
 *      Author: akshay
 */

#include <iostream>

using namespace std;

int main() {
	int N, K, T;
	int NMax;
	
	cin>>T;
	for(int t=0; t<T; t++) {
		cin>>N>>K;
		NMax = 1<<N;
		
		cout<<"Case #"<<(t+1)<<": ";
		if((K+1) % NMax == 0) {
			cout<<"ON"<<endl;
		} else {
			cout<<"OFF"<<endl;
		}
	}
}
