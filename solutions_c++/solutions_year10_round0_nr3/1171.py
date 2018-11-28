#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set> 
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <list>
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
    int round,capity,groupNum;
    ss >> round;
    ss >> capity;
    ss >> groupNum;
    
    getline(ins,line);
    stringstream ss1(line);
    int groupSize;
    int trans[groupNum],value[groupNum], totalvalue[groupNum];
    int begin = 0, end = 0, curValue = 0;
    bool neverFull = false;
    for (int j = 0; j < groupNum; j++) {
      ss1>>groupSize;
      value[j] = groupSize;
    }
    while(curValue <= capity) {
      if (end == groupNum) {
	neverFull = true;
	end = 0;
	break;
      }
      curValue += value[end];
      end ++;
    }
    trans[0] = end - 1;
    if (neverFull) {
      totalvalue[0] = curValue;
      trans[0] = 0;
      for (int j = 1; j < groupNum; j++) {
	trans[j] = 0;
	totalvalue[j] = 0;
      }
    }
    else {
      totalvalue[0] = curValue - value[end - 1];
      for (int j = 1; j < groupNum; j++) {
        curValue -= value[j - 1];
        while(curValue <= capity) {
  	  if (end == groupNum)
	    end = 0;
          curValue += value[end];
          end ++;
        }
        trans[j] = end - 1;
        totalvalue[j] = curValue - value[end - 1];
      }
    }
    long long earn = 0;
    int start = 0;
    for (int j = 0; j < round; j++) {
      earn += totalvalue[start];
      start = trans[start];
    }
    ous<<"Case #"<< i + 1 << ": "<<earn<<endl;
    //getchar();
  }
}