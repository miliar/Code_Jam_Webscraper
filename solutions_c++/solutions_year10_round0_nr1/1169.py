#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set> 
#include <vector>
#include <sstream>
#include <stdlib.h>
using namespace std;

int main()
{
  ifstream ins("testcase");
  ofstream ous("result");
  string line;
  getline(ins,line);
  int caseNum = atoi(line.c_str());
  for (int i = 0 ; i < caseNum; i++) {
    getline(ins,line);
    stringstream ss(line);
    int n,k, nn = 1;
    string result;
    ss>>n;
    ss>>k;
    for (int j = 0; j < n; j ++) {
      nn = 2 * nn;
    }
    if ((k + 1)%nn == 0) {
      result = "ON";
    }
    else result = "OFF";
    ous<<"Case #"<< i + 1 << ": "<<result<<endl;
    //getchar();
  }
}