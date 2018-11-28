// gcj_3.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <set>

using namespace std;
int intlength(int d){
  char x[100];
  _snprintf(x, 100, "%d", d);
  return strlen(x);
}

int RotateRight (int n, int bits)
{
  
  int d;
  int start = n;
  do{
    d = n%10;
    n=n/10;

    n = pow(10.0, bits)*d + n;
  }while(d==0 && n>0 && n!=start);
  return n;
  
}

int main(int argc, char* argv[])
{
  ifstream in("C-small-attempt0.in");
  ofstream out("output.txt");

  int t;
  in>>t;
  int c = t;
  set<pair<int, int>> list;

  while(t--){
    list.clear();
    int m, n;
    in>>m;
    in>>n;

    int num=m;
    int start=num;
    int count=0;
    while(num<=n){
      int mlength = intlength(num);
      m = RotateRight(num, mlength-1);
      while(m!=num && intlength(m)==intlength(num)){

        char *x = new char[200];
        
        int small = m<num?m:num;
        int big = m>num?m:num;
        auto pr = pair<int, int>(small, big);
        if(list.find(pr) != list.end()){
          m = RotateRight(m, mlength-1);
          continue;
        }

        if(m<=n && m>=start && small<big){
          count++;
          list.insert(pr);
        }
        m = RotateRight(m, mlength-1);
      }
      num++;
    }
    out<<"Case #"<<c-t<<": "<<count<<endl;
  }

  return 0;
}

