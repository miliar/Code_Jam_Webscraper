#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

vector<int> c;

int add(int a, int b) {

	int aBin[20], bBin[20];
	int sum = 0;
	
	for(int i = 19; i >= 0; i--) {
		if( a/pow(2,i) >= 1 ) {
			aBin[i] = 1;
			a -= pow(2,i);
		} else {
			aBin[i] = 0;
		}
		
		if( b/pow(2,i) >= 1 ) {
			bBin[i] = 1;
			b -= pow(2,i);
		} else {
			bBin[i] = 0;
		}
		
	}
	
	/*
	for(int i = 19; i >= 0; i--) {
		cout << aBin[i];
	}
	cout << endl;
	
	for(int i = 19; i >= 0; i--) {
		cout << bBin[i];
	}
	
	cout << endl;
	*/
	
	for(int i = 0; i < 20; i++) {
		if( (aBin[i] || bBin[i]) && !(aBin[i] && bBin[i]) ) {
			sum += pow(2,i);
		}
	}

	return sum;
}

int addSet(int start, int end) { // This will sum c[start .. end-1]

	int sum = 0;
	for(int i = start; i < end; i++) {
		
		
		sum = add(sum, c[i]);
		//cout << c[i];
		//if(i+1 < end) cout << " + ";
		//else cout << " = " << sum << endl;
	
	}

	
	
	return sum;

}

int sumup(int start, int end) {
	int sum = 0;
	
	for(int i = start; i < end; i++)
		sum += c[i];
		
	return sum;

}

bool rev (int i,int j) { return (i>j); }

int main() {
	
	int T, N, sum, tmp;
	int p1, p2, s1, s2, big;
	
	cin >> T;
	
	for(int x = 1; x <= T; x++) {
		
		cin >> N;
		sum = 0;
		big = 0;
		c.clear();
		
		for(int i = 0; i < N; i++) {
			cin >> tmp;
			c.push_back( tmp );
		}
		
		sort(c.begin(), c.end(), rev);
		
		for(int i = 1; i < N; i++) {
			p1 = addSet(0, i);
			p2 = addSet(i, N);
			//cout << endl;
			
			if(p1 == p2) {
				//cout << "p1 = " << sumup(0,i) << "\tp2 = " << sumup(i, N) << endl;
				s1 = sumup(0,i);
				s2 = sumup(i,N);
				
				if(max(s1, s2) > big)
					big = max(s1,s2);
				
			}
			
		}

		if(big) {
			cout << "Case #" << x << ": " << big << endl;
		} else {
			cout << "Case #" << x << ": NO" << endl;
		}
		
	}
return 0;
}









