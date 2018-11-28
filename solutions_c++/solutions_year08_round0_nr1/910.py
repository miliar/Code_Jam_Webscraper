#include <iostream>
#include <fstream>
#include <vector>

#define LINE 128

using namespace std;

char line[LINE];
string strs[LINE];
int current = -1;

bool operateSet(string& s, int eng)
{
  for(int i = 0; i <= current; ++ i){
    if(s == strs[i]){
      return true;
    }
  }
  
  ++ current;
  if(current == eng - 1){
    current = 0;
    strs[current] = s;
    cout<<s<<endl;
    return false;
  }
  else{
    strs[current] = s;
    return true;
  }
}

int main(int argc, char* argv[])
{
  ifstream ifs("A-small.in");
  ofstream ofs("A-small.out");

  memset(line, 0, sizeof(line));
  ifs.getline(line, LINE);
  int numTest = atoi(line);
  
  cout<<numTest<<endl;

  for(int i = 0; i < numTest; ++ i){
    current = -1;
    memset(line, 0, sizeof(line));
    ifs.getline(line, LINE);
    int numEngine = atoi(line);
    for(int j = 0; j < numEngine; ++ j){
      memset(line, 0, sizeof(line));
      ifs.getline(line, LINE);
    }
    memset(line, 0, sizeof(line));
    ifs.getline(line, LINE);
    int numQueries = atoi(line);
    int switches = 0;
    
    for(int j = 0; j < numQueries; ++ j){
      memset(line, 0, sizeof(line));
      ifs.getline(line, LINE);
      string s(line);
      if(!operateSet(s, numEngine)){
	++ switches;
	cout<<j<<endl;
      }
    }
    
    ofs<<"Case #"<<i+1<<": "<<switches<<"\r\n";
    cout<<"Case #"<<i+1<<": "<<switches<<"\r\n";
  }

  return 0;
}
