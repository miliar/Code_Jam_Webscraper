#include <iostream>
#include <cstdio>
#include <cstring>
#include <math.h>
using namespace std;

int main(){
	int i;
	int T;
	int N,K;
	long m;
	
	cin >> T;

	for (i = 1; i <= T; i++){
		cin >> N;
		cin >> K;
		
		cout << "Case #" << i << ": ";
//		m = pow(2,N);
//		printf(((K%m) ^ (m-1)) ? "OFF\n" : "ON\n");
		
		m = pow(2,N)-1;
		printf( ((K & m) == m) ? "ON\n" : "OFF\n");
	}

}
