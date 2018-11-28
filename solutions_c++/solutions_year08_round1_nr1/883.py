//Compile Command:
//        g++ A.cpp -o A

#include <iostream>
#include <fstream>
#include <string>
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
  string::size_type index;
  int num;
  if (getline(infile,aline)) {
    num = atoi(aline.c_str());
  }
  int size;
  vector<int> v1, v2;
  int sum;
  string sub1, sub2;
  int i1, i2;
 
  for (int i = 1; i <= num; i++) {
    v1.clear(); v2.clear(); sum = 0;
    getline(infile,aline);
    size = atoi(aline.c_str());

    getline(infile,aline);
    index = aline.find(" ", 0);
    while (index != string::npos) {
      sub1 = aline.substr(0, index);
      sub2 = aline.substr(index+1, aline.length());
      i1 = atoi(sub1.c_str());
      v1.push_back(i1);
      aline = sub2;
      index = aline.find(" ", 0);
    }
    i1 = atoi(aline.c_str());
    v1.push_back(i1);

    getline(infile,aline);
    index = aline.find(" ", 0);
    while (index != string::npos) {
      sub1 = aline.substr(0, index);
      sub2 = aline.substr(index+1, aline.length());
      i2 = atoi(sub1.c_str());
      v2.push_back(i2);
      aline = sub2;
      index = aline.find(" ", 0);
    }
    i2 = atoi(aline.c_str());
    v2.push_back(i2);

    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());
    reverse(v2.begin(),v2.end());
    for (int j = 0; j < size; j++) {
      sum += v1[j] * v2[j];
    }

    cout    << "Case #" << i << ": " << sum << endl;
    outfile << "Case #" << i << ": " << sum << endl;
  }

  outfile.close();
  infile.close();
  return 0;
}
