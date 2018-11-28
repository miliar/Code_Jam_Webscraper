#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<cmath>
#include<iomanip>
using namespace std;
void solve(string s, int values, int k);

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

  
  for(int i = 0; i < cases; i++){
    
    getline(in,s);
    istringstream iss(s);
    int n;
    iss >> n;
    getline(in,s);
    solve(s,n,i);
  } 
  in.close();   
}

void solve(string s, int n, int k){
  //ofstream out;
  //out.open("output.txt");
  istringstream is(s);
  int j;
  double count = 0;
  for(int i = 1; i <= n; i++){
    is >> j;
    if(i != j)
      count++;
  }
  cout << fixed;
  cout  << "Case #" << k+1 << ": " << setprecision(6) << count << endl;
}
     
     
