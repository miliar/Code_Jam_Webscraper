#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cassert>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

const int ON = 2;
const int OFF = 1;

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
  int T, N, K;
  int tcNo = 0;

  while(getline(inFile, line))
  {  
    if(isFirstLine){
      isFirstLine = false;
      T = str2int (line);
      continue;
    }

    char * cstr, *p;
    cstr = new char [line.size()+1];
    strcpy(cstr, line.c_str());
    p=strtok(cstr, " ");
    assert(p!=NULL);
    string tmp = p;
    N = str2int(tmp);  
    p=strtok(NULL, " ");
    assert(p!=NULL);
    tmp = p;
    K = str2int(tmp); 

    vector<int> steps; //of size (N+1)
    tcNo ++;
    
    if(K == 0){
      cout << "Case #"<< tcNo <<": OFF" << endl;
      continue;
    }
    
    steps.push_back(1); //steps[0]=1;
    for(int i=1; i<=N; i++){
      steps.push_back(2 * steps[i-1]); //steps[i] = 2 * steps[i-1];
    }
    if(K % steps[N] == steps[N]-1)
      cout << "Case #"<< tcNo <<": ON" << endl;
    else
      cout << "Case #"<< tcNo <<": OFF" << endl;
    
  }//while
  assert(tcNo == T);
  return 0;
    
    
}

