#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

ifstream fin("a-small-in.txt");
ofstream fout("a-small-out.txt");
long long players;
vector <long long> v(players, 0);


bool freq(long long a, vector <long long>& v){
     //fout <<a<<":"<<endl;
     for (long long i = 0; i<players; i++){
         //fout <<v[i]<<" : "<<a%v[i]<<" "<<v[i]%a<<endl;
         if (a%v[i]!=0 and v[i]%a!=0) return false; 
     }
     return true;
}

int main(){
    long long x;
    while (fin >>x){
          for (long long c = 0; c < x; c++){
              
              long long ini, fi;
              fin >>players>>ini>>fi;
              
              v = vector <long long> (players, 0);
              for (long long i = 0; i < players; i++) fin >>v[i];
              
              int res = -1;
              for (int i = ini; i <= fi; i++) {
                  if (freq(i, v)) {res = i; break;}
              }
              //fout <<ini<<endl;
              fout <<"Case #"<<c+1<<": ";
              if (res!=-1) fout <<res<<endl;
              else fout <<"NO"<<endl;
              
          }
    }
}
