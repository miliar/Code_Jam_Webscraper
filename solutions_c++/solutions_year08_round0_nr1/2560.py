#include <iostream>
#include <string>
#include <queue>        
using namespace std;

bool isWhite() {
     return cin.peek() == ' ' ||
          cin.peek() == '\t' ||
          cin.peek() == '\r' ||
          cin.peek() == '\n';
}

void eatWhite() {
     while(isWhite()) cin.get();
}

string readLine() {
     string s = "";
     while(cin.peek() != '\n' && cin.peek() != '\r') s += cin.get();
     eatWhite();
     return s;
}

int main() {
     int N;
     cin >> N;
     for(int z=1; z<=N; z++) {
          int S,Q;
          cin >> S;
          string search[S];
          eatWhite();
          for(int i=0; i<S; i++) search[i] = readLine();
          
          cin >> Q;
          string query[Q];
          eatWhite();

          for(int i=0; i<Q; i++) query[i] = readLine();

          int c[S][Q];
          for(int i=0; i<S; i++) for(int j=0; j<Q; j++) c[i][j] = 0;

          int counter = 0;
          int steps = 0;
          int startPosition = 0;
          do {
               int max = 0;
               for(int i=0; i<S; i++) {
                    int maxSeq = 0;
                    for(int j=startPosition; j<Q; j++) {
                         if(search[i] == query[j]) break;
                         maxSeq++;
                    }
                    if(maxSeq > max ) max = maxSeq;
               }
               startPosition += max;
          } while( startPosition < Q && ++steps);

          cout << "Case #" << z << ": " << steps << endl;
     }
     return 0;
}
