#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

int main(void) {
     ifstream IN("B2.in");
     ofstream OUT("B2.out");
     
     int num_test;
     IN>>num_test;
     
     for (int test=1; test<=num_test; test++) {
          int N,S,p,a;
          IN>>N>>S>>p;
          int c=0;
          for (int i=0; i<N; i++) {
               IN>>a;
               if (a==0) {
                    if (p==0) c++;
                    }
               else if (a%3==0) {
                    if (a/3>=p) c++;
                    else if (a/3+1==p && S>0) {S--; c++;} 
                    }
               else if (a%3==1) {
                    if (a/3+1>=p) c++;
                    }
               else if (a%3==2) {
                    if (a/3+1>=p) c++;
                    else if (a/3+2==p && S>0) {S--; c++;}
                    }
               }
          OUT<<"Case #"<<test<<": "<<c<<"\n";
          }
          
     system("pause");
     return 0;
     }
