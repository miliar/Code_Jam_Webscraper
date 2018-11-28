// CodeJamTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int p,q;
vector<int> pris;

int calc() {
	int total = 0;
	for(int i=0;i<q;i++) {
		int start = 0;
		int end = p - 1;
		for(int k=0;k<i;k++) {
			if (pris[k]<pris[i]) {
				start = max(start,pris[k]+1);
			}
			if (pris[k]>pris[i]) {
				end = min(end,pris[k]-1);
			}
		}
		total += end - start;
	}
	return total;
}

int main() {
	ifstream fin("C:\\input.txt");
	ofstream fout("C:\\output.txt");

  int n;
  fin >> n;
  for(int i=0;i<n;i++) {
	  fin >> p >> q;
	  pris.clear();
	  for(int k=0;k<q;k++) {
		  int x;
		  fin >> x;
		  pris.push_back(--x);
	  }
	  int ans = 1000000;
	  sort(pris.begin(),pris.end());
	  do {
		  ans = min(ans,calc());
		  //for(int k=0;k<q;k++)  cout << pris[k] << " ";
		  //cout << endl;
	  } while(next_permutation(pris.begin(),pris.end()));
	  fout << "Case #" << i+1 << ": " <<  ans << endl;
  }
  return 0;
}
