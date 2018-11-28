#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

int main(void) {
     ifstream IN("A0.txt");
     ifstream IN2("A0t.txt");
     int num_test;
     IN>>num_test;
     string S,S2;
     getline(IN,S);
     
     map<char,char> T;
     
     for (int test=1; test<=num_test; test++) {
          getline(IN,S);
          getline(IN2,S2);
          for (int i=0; i<S.size(); i++) T[S[i]]=S2[i];
//          IN>>S;
//          cout<<S<<"\n"<<S2<<"\n";
          }

     T['q']='z';
     T['z']='q';

     for (int i=0; i<26; i++) cout<<(char)('a'+i);
     cout<<"\n";
     for (int i=0; i<26; i++) cout<<T['a'+i];
     cout<<"\n";
          
     ifstream IN3("A1.in");
     ofstream OUT("A1.out");
     
     IN3>>num_test;
     getline(IN3,S);
     
     for (int test=1; test<=num_test; test++) {
          getline(IN3,S);
          S2=S;
          for (int i=0; i<S.size(); i++) S2[i]=T[S[i]];
          OUT<<"Case #"<<test<<": "<<S2<<"\n";
          }
          
     system("pause");
     return 0;
     }
