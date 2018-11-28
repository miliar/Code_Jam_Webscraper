/*
 * Round2_B.cpp
 *
 *  Created on: Jun 5, 2010
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

int P,N;
vector<int> M;
vector<int> matchCost[12];
int pow2[12];

int cost;

int getMinNumOfSkips(int begin, int end) {
	int min=P+1;
	for(int i=begin; i<end; i++)
		min = (M[i]<min) ? M[i] : min;
	return min;
}


void getMinCost(int level, int match) {
	if(level==P)
		return;

	int n = pow2[P-level];
	int begin = match*n;
	int end = (match+1)*n;

	int minNumOfSkips = getMinNumOfSkips(begin,end);
	if(minNumOfSkips < P-level) {
		cost++;
		getMinCost(level+1, 2*match);
		getMinCost(level+1, 2*match+1);
	}
}


void initPow2() {
	int factor=1;
	for(int i=0; i<=11; i++) {
		pow2[i]=factor;
		factor = factor<<1;
	}
}


int main() {
	initPow2();
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		fin>>P;
		M.clear();
		N=pow2[P];
		for(int i=0; i<N; i++) {
			int miss; fin>>miss;
			M.push_back(miss);
		}
		for(int level=P-1; level>=0; level--) {
			matchCost[level].clear();
			int numOfMatches = pow2[level];
			for(int i=0; i<numOfMatches; i++) {
				int ticket; fin>>ticket;
				matchCost[level].push_back(ticket);
			}
		}

		cost=0;
		getMinCost(0,0);

		fout << "Case #" << t << ": " << cost << endl;
	}

	return 0;
}
