#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(unsigned int A = (unsigned int)I; A < (unsigned int)B; A++)

map<unsigned int, map<unsigned int, unsigned int> > v;
map<unsigned int, map<unsigned int, unsigned int> > c;

unsigned int solve(){
  unsigned int A,B;
  unsigned int count = 0;
  
  scanf("%d", &A);
  scanf("%d", &B);

  for(unsigned int N=A; N<B; N++){
      for(unsigned int M = N+1; M<B+1; M++){
          if (N/10 == 0 && M/10) break;
          if (N/100 == 0 && M/100) break;
          
          if (!v[N][M]){
            // do stuff
            stringstream out;
            out << N;
            string n = out.str();
            out.str(std::string());
            out << M;
            string m = out.str();

            //cout << "n: " << n << endl;
            //cout << "m: " << m << endl; 

            n += n;

            if (n.find(m) != string::npos) {
                c[N][M] = 1;
            }
            v[N][M] = 1;
          }
          
          count += c[N][M];
      }
  }

  return count;

}

int main()
{
  unsigned int t;
  scanf("%d", &t);
  FOR(testcase, 0, t){
    //do something
    unsigned int score = 0;

    score = solve();

    printf("Case #%d: %d\n", testcase + 1, score);
  }
  return 0;
}


