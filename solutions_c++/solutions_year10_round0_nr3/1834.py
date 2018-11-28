#include <iostream>
#include <fstream>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

template <typename T>
void convertStoT(T &value, string &str) {
  istringstream istr(str);
  istr >> value;
}

int main(int argc, char **argv) {
  using namespace std;
  ifstream ifile(argv[1]);
  ofstream ofile(argv[2]);
  
  vector<string> svec;
  copy(istream_iterator<string>(ifile),
       istream_iterator<string>(),
       back_inserter(svec));
  
  const int T = atoi(svec[0].c_str());
  int counter = 0;
  for (int i = 0; i < T; ++i) {
    long long unsigned int R;
    convertStoT(R, svec[++counter]);
    long long unsigned int K;
    convertStoT(K, svec[++counter]);
    const int N = atoi(svec[++counter].c_str());
    
    long long unsigned int gi[1000];
    long long unsigned int tsum = 0;
    for (int j = 0; j < N; ++j) {
      convertStoT(gi[j], svec[++counter]);
      tsum += gi[j];
    }
    long long unsigned int earned = 0;
    if (tsum <= K) {
      earned = tsum * R;
      ofile << "Case #" << i+1 <<": " << earned << endl;
      continue;
    }
      
  
    
    set<int> starter;
    vector<int> ipos;
    vector<long long unsigned int> earnpos;
    int start = 0;
    starter.insert(0);
    ipos.push_back(0);
    bool done = false; 
    for (long long unsigned int j = 0; j < R; ++j) {
      long long unsigned sum = 0;
      
      if (true == done)
	break;
      for (int k = start; ;++k) {
	k = k % N;
	if (sum + gi[k] <= K) {
	  sum += gi[k];
	}
	else {
	  start = k;
	  earned += sum;
	  break;
	}
      }
      earnpos.push_back(sum);
      if (starter.end() == starter.find(start)) {
	starter.insert(start);
	ipos.push_back(start);
      }
      else {
	long long unsigned int remain = R - j - 1;
	long long unsigned int repeat = 0;
	long long unsigned int earns = 0;
	long long unsigned int pos = 0;
	bool found = false;
	for (int l = 0; l < ipos.size(); ++l) {
	  if (ipos[l] == start) {
	    repeat = ipos.size() - l;
	    found = true;
	    pos = l;
	  }
	  if (true == found)
	    earns += earnpos[l];
	}
	earned += (remain/repeat)*earns;
	long long unsigned int remainder = remain%repeat;
 	for (int l = pos; l < (pos + remainder); ++l) {
	  earned += earnpos[l];
	}
	done = true;
      }
	
    }
    ofile << "Case #" << i+1 << ": " << earned << endl;
    
  }
}
