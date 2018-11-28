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

void dosplit(const string &tmp, vector<string> &svec) {
  string splits = "/";
  for (int i  = 1; i < tmp.size(); ++i) {
    if (tmp[i] == '/')
      svec.push_back(splits);
    splits += tmp[i];
  }
  svec.push_back(splits);
}

void putin(set<string> & present, const string &tmp) {
  vector<string> splited;
  dosplit(tmp, splited);
  for (int i = 0; i < splited.size(); ++i)
    present.insert(splited[i]);
}

int addin(vector<string> &splited, set<string> &present) {
  int addcnt = 0;
  for (int i = 0; i < splited.size(); ++i) {
    if (present.find(splited[i]) == present.end()) {
      addcnt++;
      present.insert(splited[i]);
    }	
  }
  return addcnt;
}

int main(int argc, char **argv) {
  ifstream ifile(argv[1]);
  ofstream ofile(argv[2]);
  vector<string> svec;
  copy(istream_iterator<string>(ifile),
       istream_iterator<string>(),
       back_inserter(svec));

  const int T = atoi(svec[0].c_str());
  int counter = 0;
  for (int i = 0; i < T ; ++i) {
    const int N = atoi(svec[++counter].c_str());
    const int M = atoi(svec[++counter].c_str());
    set<string> present;
    vector<string> todo;
    for (int j = 0; j < N; ++j) putin(present, svec[++counter]);
    int newadd = 0;
    for (int j = 0; j < M; ++j) {
      const string tmp = svec[++counter];
      if (present.find(tmp) != present.end())
	continue;
      
      vector<string> splited;
      dosplit(tmp, splited);
      newadd += addin(splited, present);
    }
    ofile << "Case #" << i+1 << ": " << newadd <<  endl;
  }
}
