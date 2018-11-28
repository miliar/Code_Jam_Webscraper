#include <cstdio>
#include <string.h>
#include <stack>
#include <vector>

// diamond inheritance

#define DEBUG(...)
//#define DEBUG(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

int T;

int N;

vector<int> S[1001]; // superclass list of each class

void readInput() {
   scanf("%d", &N);
   for (int i=1; i<=N; ++i) {
      int n;
      scanf("%d", &n);
      S[i].clear();
      for (int j=0; j<n; ++j) {
         int s;
         scanf("%d", &s);
         S[i].push_back(s);
      }
   }
}



void solve() {
   for (int start=0; start<N; ++start) {
      bool V[1001];
      for (int i=1; i<=N; ++i) V[i] = false;
      stack<int> st;
      st.push(start);
      while (!st.empty()) {
         int n = st.top();
         st.pop();
         for (unsigned int i=0; i<S[n].size(); ++i) {
            if (V[S[n][i]]) {
               printf("Yes");
               return;
            } else {
               V[S[n][i]] = true;
               st.push(S[n][i]);
            }
         }
      }
   }  
   printf("No");
}



int main() {
   scanf("%d ", &T);
   for (int i=1; i<=T; ++i) {
      readInput();
      printf("Case #%d: ", i);
      solve();
      printf("\n");
   }
   return 0;
}

