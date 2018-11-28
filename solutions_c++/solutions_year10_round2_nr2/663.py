#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <iterator>
#include <stdlib.h>
#include <stdio.h>

using namespace std;



int main(int argc, char **argv) {
  ifstream ifile(argv[1]);
  ofstream ofile(argv[2]);
  vector<string> svec;
  copy (istream_iterator<string>(ifile),
	istream_iterator<string>(),
	back_inserter(svec));
  
  const int T = atoi(svec[0].c_str());
  int counter = 0;
  for (int i = 0; i < T; ++i) {
    const int N = atoi(svec[++counter].c_str());
    const int K = atoi(svec[++counter].c_str());
    const int B = atoi(svec[++counter].c_str());
    const int T = atoi(svec[++counter].c_str());
    
    vector<bool> passchicks;
    vector<int> xvec;
    vector<int> vvec;
    vector<int> swaps;
    typedef pair<int, int> time_loc;
    multimap<time_loc, int> fullmap;
    for (int j = 0; j < N; ++j) xvec.push_back(atoi(svec[++counter].c_str()));
    for (int j = 0; j < N; ++j) vvec.push_back(atoi(svec[++counter].c_str()));

    
    for (int j = 0; j < N; ++j) {
      int speed = vvec[j];
      int loca = xvec[j];
      
      long long unsigned int tmp = speed;
      tmp = tmp *T;
      if (loca + tmp < B) 
	passchicks.push_back(false);
      else 
	passchicks.push_back(true);
      
    } 

    if (passchicks.size() >= K) {
      
      for (int j =0; j < N; ++j) {

	if (passchicks[j] == false)
	  continue;
	
	int index = swaps.size();
	swaps.push_back(0);
	
	for (int k = 0; k < N; ++k) {
	  if (j == k)
	    continue;
	  if (passchicks[k] == true)
	    continue;
	  if (xvec[k] >= xvec[j])
	    swaps[index] = swaps[index] + 1;
	}

      }
    }
    
    sort(swaps.begin(), swaps.end());  
    ofile << "Case #" << i+1 << ": ";
    if (swaps.size() < K)
      ofile << "IMPOSSIBLE" << endl;
    else {
      unsigned int scount = 0;
      for (int j = 0; j < K; ++j) {
	scount += swaps[j];
      }
      ofile << scount << endl;
    }
	

  }
}
