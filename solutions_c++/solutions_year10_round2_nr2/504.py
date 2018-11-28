/*
 * Round1B10_B.cpp
 *
 *  Created on: May 22, 2010
 *      Author: Jad
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <stack>
#include <gmp.h>
using namespace std;

ifstream fin("GCJ2010/in");
ofstream fout("GCJ2010/out");


int N,K,B,T;
vector<int> dist, v;
vector<int> chicksAhead;

int compareT(int i, int j) {
	// compare to zero
	return (dist[i]*v[j] - dist[j]*v[i]);
}

bool canGetThere(int chick) {
	return (dist[chick]-T*v[chick])<=0;
}

int main() {
	int C; fin>>C;
	for(int c=1; c<=C; c++) {
		dist.clear();
		v.clear();
		chicksAhead.clear();

		fin>>N>>K>>B>>T;

		for(int i=0; i<N; i++) {
			int x; fin>>x;
			dist.push_back(B-x);
		}
		for(int i=0; i<N; i++) {
			int x; fin>>x;
			v.push_back(x);
		}
		for(int i=0; i<N; i++) {
			chicksAhead.push_back(0);
			if(!canGetThere(i))
				for(int chick=0; chick<i; chick++) {
					if(compareT(chick, i)<0)
						chicksAhead[chick]++;
				}
		}

		int numSwaps=0, numChicks=0;
		for(int chick=N-1; numChicks<K && chick>=0; chick--) {
			if(canGetThere(chick)) {
				numSwaps += chicksAhead[chick];
				numChicks++;
			}
		}

		fout<<"Case #"<<c<<": ";
		if(numChicks==K)
			fout<<numSwaps<<endl;
		else
			fout<<"IMPOSSIBLE"<<endl;
	}

	return 0;
}
