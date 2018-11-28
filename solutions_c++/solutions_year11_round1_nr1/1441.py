#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

#define MAX_STR_LEN 110
#define MAX_ARR_LEN 1010

int gcd (int a, int b) {
  int t;
  while (b) {
    t=b;
    b=a % b;
    a=t;
  }
  return a;
}

int main () {
    char filename[MAX_STR_LEN];
    char filename1[MAX_STR_LEN];
  cin>>filename;
  cin>>filename1;
  
  

  ifstream in(strcat(filename, ".in"));
  if (!in.is_open()) cout<<"OH NO"<<endl;

  ofstream out(filename1);
  if (!out.is_open()) cout<<"OH NO"<<endl;


    int n, d, g;
    int c;
    int many;
    
    in>>many;
    
    for (int i=0;i<many; i++) {
      in>>n>>d>>g;
    c=100/gcd(d,100);
    if (d!=0&&g==0 || d!=100&&g==100 || c>n) {
      out<<"Case #"<<i+1<<": Broken"<<endl;
      }
      else
      out<<"Case #"<<i+1<<": Possible"<<endl;
  }
  
  
}
    
