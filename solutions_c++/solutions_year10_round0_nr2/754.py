/*
 * B.cpp
 *
 *  Created on: May 7, 2010
 *      Author: Ningfeng
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

unsigned long long gcd(unsigned long long A, unsigned long long B) {
	if(B == 0) return A;
	else return gcd(B, A%B);
}

int main() {
	int C, N;
	vector< unsigned long long int > a;
	unsigned long long g, y;
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	fin >> C;
	for(int i=1; i<=C; i++) {
		a.clear();
		g = INT_MAX;
		fin >> N;
		//cout << "Line #" << i << endl;
		//cout << "Number of Elements is: " << N << endl;
		unsigned long long int slarbo;
		for(int j=0; j<N; j++) {
			fin >> slarbo;
			//cout << "slarbo is: " << slarbo << endl;
			a.push_back(slarbo);
		}
		//cout << "a[0] is: " << a[0] << endl;
		sort(a.begin(), a.end());
		//cout << "a[0] is: " << a[0] << endl;
		unsigned long long int firstElement = a[0]; //Keep first element
		for(int p=0; p<N-1; p++)
			a[p] = a[p+1]-a[p];
		//cout << "a[0] is: " << a[0] << endl;
		if(N==2 && a[0] != 0)
			g = a[0];
		else if(N==2 && a[0] == 0)
			g = firstElement;
		else {
		for(int k=0; k<N-2; k++) {
			unsigned long long newgcd = gcd(a[k], a[k+1]);
			//if(k==0) g = newgcd;
			if(newgcd < g)
				g = newgcd;
		}
		}
		int t = 1;
		while(t*g<firstElement)
			t++;
		//	y = firstElement-t*g;

		//cout << "t is: " << t << endl;
		//cout << "g is: " << g << endl;
		//cout << "First element is: " << firstElement << endl;
		y = t*g-firstElement;
		fout << "Case #" << i << ": " << y << endl;
	}
	//cout << gcd(0, 5) << endl;
	return 0;
}
