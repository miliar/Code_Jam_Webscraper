#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <cstdlib>

using namespace std;

int main(void) {
     ifstream IN("C2.in");
     ofstream OUT("C2.out");
     
     int num_test;
     IN>>num_test;
     
     for (int test=1; test<=num_test; test++) {
          int A,B;
          IN>>A>>B;
          long long c=0;
          for (int i=A; i<=B; i++) {
               vector<int> v;
               int n=i;
               int k=1;
               int a=0;
               while (n>0) {
                    n/=10;
                    k*=10;
                    a++;
                    }
               k/=10;
               n=i;
               set <int> S;
               for (int j=0; j<a; j++) {
                    int nn=n/10+(n%10)*k;
                    n=nn;
                    if (n>i && n<=B) S.insert(n);
                    }
               c+=S.size();
               }
          OUT<<"Case #"<<test<<": "<<c<<"\n";
          }
          
     system("pause");
     return 0;
     }
