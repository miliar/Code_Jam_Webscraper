//
//  main.cpp
//  GCJ
//
//  Created by Bryan Hooi on 14/4/12.
//  Copyright (c) 2012 Clinkle. All rights reserved.
//

#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;
typedef vector<int> vi;
int main (int argc, const char * argv[])
{
  ifstream fin("/Users/HOOI/Documents/CS/GCJ/GCJ/in.txt");
  ofstream fout("/Users/HOOI/Documents/CS/GCJ/GCJ/out.txt");
  int cases; fin>>cases;
  string junk; getline(fin, junk);
  string mp="ynficwlbkuomxsevzpdrjgthaq";
  for (int cs=1;cs<=cases;cs++){
    string text; getline(fin, text);
    for (int i=0;i<text.size();i++) if (isalpha(text[i])){
      text[i]='a'+mp.find(text[i]);
    }
    fout<<"Case #"<<cs<<": "<<text<<endl;
  }
  return 0;
}

