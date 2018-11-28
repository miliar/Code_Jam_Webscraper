#include<iostream>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<cmath>
using namespace std;

long long lopow(int a, int b) {
  long long ret = 1LL;
  for (int i = 0; i < b; i++) 
       ret *= a;
  return ret;
}
int main() {
  
  
  ifstream in("in.txt");
  ofstream out("out.txt");
  int N;
  in >> N;
  string a;
  long long base;
  string ret;
  set<char> S;
  map<char,char> M;
  char k,n;
  long long time;
  for (int i = 1; i <= N; i++) {
         time = 0LL;
         in >> a;
         S.clear();
         ret.clear();
         for (int j = 0; j < a.size(); j++) {
            S.insert(a[j]);
         }
         base = S.size();
         if (base == 1) {
            base++;
         }  
         k = '0';
         M[a[0]] = '1';
         ret += '1';
         for (int j = 1; j < a.size(); j++) {
            if (M[a[j]]) {
               ret += M[a[j]];
            }
            else {
              M[a[j]] = k;
              ret += k;
              k++;
              if ( k == '1') k++;
            }
         }
  
        M.clear();
        for (int j = 0; j < ret.size(); j++) {
            time += (ret[j] - '0')*lopow(base, ret.size() - j - 1);
        }
  
        out << "Case #"<<i<<": "<<time<<endl;
  }
}
            
         
         