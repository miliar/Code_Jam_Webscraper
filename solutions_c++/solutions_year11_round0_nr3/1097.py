#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<cmath>
using namespace std;
void solve(string s, int values, int k);

int main(int argc, char* argv[]){
  /*unsigned int x=~0;
  unsigned short y=10; 
    cout << hex << x << endl;
    cout << hex << y << endl;
    cout << hex << (((~x)&y)|((x)&(~y)))<< endl;*/
  string s;
  ifstream in;
  if(argc == 2)
    in.open(argv[1]);
  else
    in.open("test.txt");

  getline(in,s);
  istringstream is(s);
  int n;
  is >> n ;

  
  for(int i = 0; i < n; i++){
    
    getline(in,s);
    istringstream iss(s);
    int values;
    iss >> values;
    getline(in,s);
    solve(s,values,i);
  } 
  in.close();   
}

void solve(string s, int values, int k){
  ofstream out;
  //out.open("output.txt");
  istringstream is(s);
  unsigned int sum = 0;
  unsigned long ans = 0;
  unsigned int mini = ~0;
  unsigned int n;
  for(int i = 0; i < values; i++){
    is >> n;
    sum = (((~sum)&n)|(sum &(~n)));
   
    ans = ans + n;
    if( n < mini)
      mini = n;
  }
  cout  << "Case #" << k+1 << ": ";
  //cout << sum << endl;
  if(sum != 0){
    cout << "NO" << endl;
    return;
  }
  cout << ans - mini << endl; 
  //out.close();
}
     
     
