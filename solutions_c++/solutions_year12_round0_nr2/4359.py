#include <iostream>
#include <stdio.h>
#include <map>
#include <sstream>
using namespace std;

void decode (int i, string ss) {
   int N, S, p;
   stringstream s (stringstream::in | stringstream::out);
   s << ss;
   cout << "Case #" << i << ": ";
   s >> N >> S >> p;

   int t = 0;
   for(int i = 0; i < N; i++) {
      int score;
      s >> score;
      int best_score = score / 3;
      if(best_score >= p) {
         t++;
      } else if(score % 3 == 0) {
         if(score > 0 && best_score + 1 >= p && S > 0) {
            t++;
            S--;
         }
      } else {
         if(score >= 1 && best_score + 1 >= p) {
            t++;
         } else if((score % 3 == 2) && score >= 2 && best_score + 2 >= p && S > 0) {
            t++;
            S--;
         }
      }
   }
   cout << t << "\n";
}

int main(int argc, char** argv) {
   char buff[512];
   int T;

   scanf("%d\n", &T);
   for(int i = 0; i < T; i++) {
      string s;
      getline(cin, s);
      decode((i+1), s);
   }
}
