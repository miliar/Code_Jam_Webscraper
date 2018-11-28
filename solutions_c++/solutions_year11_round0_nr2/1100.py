#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<cmath>
#include<vector>
using namespace std;
string solve(string s);

int main(int argc, char* argv[]){
  string s;
  ifstream in;
  if(argc == 2)
    in.open(argv[1]);
  else
    in.open("test.txt");

  getline(in,s);
  istringstream is(s);
  int cases;
  is >> cases ;

  ofstream out("output.txt");
  for(int i = 0; i < cases; i++){
    
    getline(in,s);
    out << "Case #" << i+1 << ": [" << solve(s) << "]" << endl;
  } 
  in.close();   
}

string solve(string s){
  istringstream is(s);
  int n;
  is >> n;
  char triple[3];
  char combine[26][26];
  for(int i = 0; i < 26; i++)
    for(int j = 0; j < 26; j++)
       combine[i][j] = '0';

  
  for(int i = 0; i < n; i++){
    is >> triple[0] >> triple[1] >> triple[2];
    combine[triple[0]-65][triple[1]-65] = triple[2];
    combine[triple[1]-65][triple[0]-65] = triple[2];
  }
 
  
  
   
  
  bool oppose[26][26];
  for(int i = 0; i < 26; i++)
    for(int j = 0; j < 26; j++)
      oppose[i][j] = false;
  is >> n;
  char dble[2];
  for(int i = 0; i < n; i++){
    is >> dble[0] >> dble[1];
    oppose[dble[0]-65][dble[1]-65] = true;
    oppose[dble[1]-65][dble[0]-65] = true;
  }
  
  is >> n;
  
  vector<char> result;
  char c;

  for(int i = 0; i < n; i++){
    is >> c;
    if(result.empty()){
        result.push_back(c);
        continue;
    }
   
    int last = result.size()-1;
    if(combine[result[last]-65][c-65] != '0')
      result[last] = combine[result[last]-65][c-65];
    else{
      for(int k = 0; k < result.size(); k++){
	if(oppose[c-65][result[k]-65] == true){
	  result.clear();
          break;
	}
      }
      if(!result.empty())
        result.push_back(c);
    }

    
   }
  

  if(result.empty())
    return "";
     
string r;
for(int i = 0; i < result.size()-1; i++){
  r = r + result[i] + ", ";
 }

r = r + result.back();

   
      
  return r;
}
     
     
