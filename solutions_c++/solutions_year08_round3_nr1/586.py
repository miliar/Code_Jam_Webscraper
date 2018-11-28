#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) 
{
  assert(argc == 2);
  string datafile = argv[1];
  string in = datafile + ".in";
  string out = datafile + ".out";
  ifstream infile(in.c_str());
  ofstream outfile(out.c_str());

  string aline("");
  int num;
  if (getline(infile,aline)) {
    num = atoi(aline.c_str());
  }

  for (int i = 1; i <= num; i++) {
    string::size_type index;
    string sub;
    int P, K, L;
    getline(infile,aline);
    index = aline.find(" ", 0);
    sub = aline.substr(0, index);
    aline = aline.substr(index+1, aline.length());
    P = atoi(sub.c_str());

    index = aline.find(" ", 0);
    sub = aline.substr(0, index);
    aline = aline.substr(index+1, aline.length());
    K = atoi(sub.c_str());
    
    L = atoi(aline.c_str());

    getline(infile,aline);
    vector<int> v;
    int tmp;
    for (int j = 1; j <= L; j++) {
       index = aline.find(" ", 0);
       sub = aline.substr(0, index);
       aline = aline.substr(index+1, aline.length());
       tmp = atoi(sub.c_str());
       v.push_back(tmp);
    }
    sort(v.begin(),v.end());
    reverse(v.begin(),v.end());

    long long sum=0;
    int tmpindex;
    for (int j = 0; j < P; j++) {
      tmpindex = j*K;
      if (tmpindex >= v.size()) break;
      for (int k = 0; k < K; k++) {
	tmpindex = j*K+k;
	if (tmpindex >=v.size()) break;
	sum += v[tmpindex]*(j+1);
      }
    }
    
    cout    << "Case #" << i << ": " << sum << endl;
    outfile << "Case #" << i << ": " << sum << endl;
  }

  outfile.close();
  infile.close();
  return 0;
}
