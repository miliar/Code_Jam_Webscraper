#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cassert>
#include <list>
#include <algorithm>

using namespace std;

int str2int (const string &str) {
stringstream ss(str);
int n;
ss >> n;
return n;
}

string int2str (int n) {
stringstream ss;
ss << n;
return ss.str();
}

int main(int argc, char *argv[])
{
  assert(argc == 2);  //!!!!
  ifstream inFile(argv[1], ifstream::in);
  string line;
  bool isFirstLine = true;
  int T, R, k, N;
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
    R = str2int(tmp);
    //cout << R << endl;
    
    p=strtok(NULL," ");
    assert(p!=NULL);
    tmp = p;
    k = str2int(tmp);
    //cout << k << endl;
    
    p=strtok(NULL," ");
    assert(p!=NULL);
    tmp = p;
    N = str2int(tmp);
    //cout << N << endl;
    delete[] cstr;  

    getline(inFile, line); //!
    list<int> groups;
    cstr = new char [line.size()+1];
    strcpy(cstr, line.c_str());
    p=strtok(cstr, " ");
    while(p!=NULL){
      string tmp = p; 
      groups.push_back(str2int(tmp));
      //cout << str2int(tmp) << " ";
      p=strtok(NULL," ");
    }
    //cout << endl;
    assert(groups.size() == N);
    delete[] cstr;  
    
    tcNo ++;
    
    int money = 0;
    for(int i = 0; i < R; i ++){ //R runs per day
      //cout << "Round " << i << endl;
      int sum = 0; int num = 0;
      int head = groups.front();
      sum += head; num ++;
      while(sum <= k){
        groups.push_back(head);
        groups.pop_front();
        //cout << head << " ";
        if(num < N){
          head = groups.front();
          sum += head;
          num ++;
        }
        else
          break;
      }//while
      if(sum > k) sum -= head;
      //cout << endl;
      //cout << "sum: " << sum << endl;
      money += sum;
    }//for
    
    cout << "Case #"<< tcNo <<": " << money << endl;
    groups.clear();
    
  } //while(getline(inFile, line))
    
  assert(tcNo == T);
  return 0;
    
    
}


