/*
 * Round1C_A.cpp
 *
 *  Created on: 2010/05/23
 *      Author: haru
 */

#include "Round1C_A.h"

#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;

typedef vector<int> VI;

Round1C_A::Round1C_A() {
	// TODO Auto-generated constructor stub
	int T;
	cin >> T;
	for(int i=1;i<=T;i++){
		int N;
		cin >> N;
		VI A(N), B(N);

		for(int j=0;j<N;j++){
			cin >> A[j] >> B[j];
		}

		int ans = 0;
		for(int j=0;j<N;j++){
			for(int k=j+1;k<N;k++){
				if( (A[j] < A[k] && B[j] > B[k]) ||
					(A[j] > A[k] && B[j] < B[k])  ){
					ans++;
				}
			}
		}

		cout << "Case #" << i << ": ";
		cout << ans;
		cout << endl;
	}
}

Round1C_A::~Round1C_A() {
	// TODO Auto-generated destructor stub
}
