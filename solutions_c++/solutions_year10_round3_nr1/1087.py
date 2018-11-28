#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <limits>

using namespace std;

int str2int (const string &str) {
  stringstream ss(str);
  int n;
  ss >> n;
  return n;
}



int main(int argc, char *argv[])
{
  assert(argc == 2);  //!!!!
  ifstream inFile(argv[1], ifstream::in);
  string line;
  bool isFirstLine = true;
  int T;
  int tcNo = 0;

  while(getline(inFile, line))
  {  
    if(isFirstLine){
      isFirstLine = false;
      T = str2int (line);  //T
      //cout << T << endl;
      continue;
    } 
    
    int N = str2int (line); 
    int A[1001]; int B[1001]; //int idx[1001]
    for(int i = 0; i < N; i ++){
      getline(inFile, line);
      char * cstr, *p;
      cstr = new char [line.size()+1];
      strcpy(cstr, line.c_str());
      p = strtok(cstr, " "); 
      assert(p!=NULL);
      string tmp = p;
      A[i] = str2int(tmp);
      p = strtok(NULL, " "); 
      assert(p!=NULL);
      tmp = p;
      B[i] = str2int(tmp);
      //idx[i] = i;
      delete[] cstr;
    }
    
    for(int i = 0; i < N-1; i ++){
      for(int j = i+1; j < N; j ++){
        if(A[i] > A[j]){
          int tmp = A[i];
          A[i] = A[j];
          A[j] = tmp;
          
          tmp = B[i];
          B[i] = B[j];
          B[j] = tmp;
        }
      }//for
    }//for
    
    int num = 0;
    for(int i = 1; i <= N-1; i ++){
      for(int j = 0; j < i; j ++){
        if( B[i] < B[j] ) num ++;
      }
    }
    
    //num /= 2;  //????
    
    tcNo ++;
    cout << "Case #" << tcNo << ": " << num << endl;
    
 } //while(getline(inFile, line))  
    
  assert(tcNo == T);
  return 0;    
}
