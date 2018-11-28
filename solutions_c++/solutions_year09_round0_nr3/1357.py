#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main() {
  
  int N,sum;
  ifstream IN("in.txt");
  ofstream OUT("out.txt");
  IN >> N;
  char a1,a2;
  string text;
  getline(IN,text);
  string Google = "welcome to code jam";
  for (int j = 1; j <= N; j++) {
    getline(IN,text);
    vector<int>  V(text.size(),0);
    for (int i = 0; i < text.size(); i++) 
      if (text[i] == 'm') V[i]++;
    for (int m = Google.size() - 2; m >= 0; m--) {
      a1 = Google[m+1];
      a2 = Google[m];
      for (int i = 0; i < text.size(); i++) {
        if (text[i] == a2) {
          for (int k = i; k < text.size(); k++) {
            if(text[k] == a1) V[i] = (V[i] + V[k]) % 10000;
          }
        }
      } 
      for (int i = 0; i < text.size(); i++)
        if (text[i] == a1) V[i] = 0;
   
    }
    sum = 0;
    for (int i = 0; i < text.size(); i++) 
      if (text[i] == 'w')  {
        sum = (sum+V[i]) % 10000;
      }

    OUT<<"Case #"<<j<<": ";
    if (sum / 1000 > 0) OUT<<sum<<endl;
    else 
    if (sum / 100 > 0) OUT<<"0"<<sum<<endl;
    else 
    if (sum / 10 > 0) OUT<<"00"<<sum<<endl;
    else OUT<<"000"<<sum<<endl;
    for (int i = 0; i < V.size(); i++) V[i] = 0;
  }
}
    
  