/*
 * Theme Park.cpp
 *
 *  Created on: 2010-05-08
 *      Author: phobos
 */

#include <iostream>

using namespace std;

int main(int argc, char** argv) {
	int T = 0;
	cin>>T;

	int* R = new int[T];
	int* k = new int[T];
	int* N = new int[T];
	int* euro = new int[T];
	int** g = new int*[T];

	for (int i = 0; i < T; i++) {
		cin>>R[i]>>k[i]>>N[i];

		g[i] = new int[N[i]];

		for (int j = 0; j < N[i]; j++) {
			cin>>g[i][j];
		}
	}

	int index;
	for (int i = 0; i < T; i++) {
		index = 0;
		euro[i] = 0;

		for (int j = 0; j < R[i]; j++) {
			for(int z = 0,  person = 0; person + g[i][index] <= k[i] && z < N[i]; z++ ) {
				person += g[i][index];
				euro[i] += g[i][index];
				index = (index + 1) % N[i];
			}
		}
	}

	for (int i = 0; i < T; i++) {
		cout<<"Case #"<<i+1<<": "<<euro[i]<<endl;
	}

	return 0;
}
