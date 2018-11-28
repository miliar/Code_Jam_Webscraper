/*
 *  snapper.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 10/05/08.
 *  Copyright 2010 University of Michigan. All rights reserved.
 *
 */
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T, N, K;
	
	cin >> T;
	
	for (int i=0; i<T; ++i) {
		
		cin >> N >> K;
		
		//int period = pow(double(2), N-1);
		
		//int div = K/period;
		
		cout << "Case #"<<i+1<<": ";
		
		//if(div % 2)
		
		int period = pow(double(2), N);
		
		if(!((K+1)%period))
			cout << "ON";
		else {
			cout << "OFF";
		}
		
		cout << endl;
	}
}


