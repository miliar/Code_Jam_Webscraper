#include <stdio.h>
#include <iostream>
#include <fstream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>
#include <climits>

using namespace std;

struct Node {
	int index; 
	int distance; 
	Node(int i1, int i2) {
		index = i1; 
		distance = i2; 
	}
	bool operator< (const Node& node) {
		if (distance < node.distance)
			return true;
		else 
			return false;
	}
}; 

int main(int argc, char* argv[]) {
	fstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}
	string ln; 
	inf >> ln;
	int caseNum = atoi(ln.c_str());
	for (int cn = 0; cn<caseNum; cn++) {
		// read data
		inf >> ln;
		int L = atoi(ln.c_str());
		inf >> ln;
		int t = atoi(ln.c_str());
		inf >> ln;
		int N = atoi(ln.c_str());
		inf >> ln;
		int C = atoi(ln.c_str());
		 
		vector<int> a;
		for (int i=0; i<C; i++){
			inf >> ln;
			a.push_back(atoi(ln.c_str()));
		}
		int k = C;
		int ii = 0; 
		while (k<N) {
			k++;
			int i=a[ii++];
			a.push_back(i);
			if (ii == C) 
				ii = 0; 
		}

		// find solution
		int firstDistance = 0.5 * t;
		int cul = 0; 
		int starts = 0; 
		for (; starts<N; starts++) {
			cul += a[starts];
			if (cul > firstDistance) {
				break;
			}
		}
		vector<int> buildBooster; 
		for (int i=0; i<N; i++) {
			buildBooster.push_back(0);
		}
		vector<Node> distances; 
		if (starts == N) {
			// no booster
		}
		else {
			// booster on which starts?
			
			int temp = 0; 
			for (int i=0; i<starts; i++) {
				distances.push_back(Node(i,0));
			}
			
			distances.push_back(Node(starts, cul - firstDistance));
			for (int i=starts+1; i<N;  i++) {
				distances.push_back(Node(i, a[i]));
			}
			sort(distances.begin(), distances.end());
			
			for (int i=N-1; i>=0&&L>0; i--) {
				L--;
				buildBooster[distances[i].index] = 1;
			}
		}

		// calculate
		int time = 0; 
		for (int i=0; i<N; i++) {
			if (buildBooster[i] == 0) {
				time += a[i] / 0.5; 
			}
			else {
				for (int k=0; k<N; k++) {
					if (distances[k].index == i) {
						time += distances[k].distance / 1; 
						time += (a[i] - distances[k].distance) / 0.5;
						break;
					}
				}
			}
		}
		
		// output
		cout << "Case #" << cn+1 << ": " << time << endl;
	}
	return 0; 
}