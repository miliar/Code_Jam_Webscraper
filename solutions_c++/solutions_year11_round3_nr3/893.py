#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int main (){
    int T;
    ifstream fin ("C-small.in");
    ofstream fout ("C-small.out");
    fin >>T;
    for (int cas=1; cas<=T; cas++){
      int n,l,h;
      fin >>n>>l>>h;
      vector <int> v (n);
      for (int i=0; i<n; i++){
          fin >>v[i];
      }
      int fet=0;
      int so=-1;
      for (int t=l; t<=h; t++){
          fet=0;
          for (int i=0; i<n; i++){
              if (t%v[i]==0 or v[i]%t==0) fet++;
          }
          if (fet==n){
             so=t;
             t=h+1;
          }
      }
      fout <<"Case #"<<cas<<": ";
      if (fet==n) fout <<so<<endl;
      else fout <<"NO"<<endl;
    }
}
