#include <iostream>

using namespace std;

int main() {
   int total;
   cin >> total;
   for (int totalcount = 0; totalcount < total; ++totalcount) {
      int N, S, P, r = 0;
      cin >> N >> S >> P;
      int score[N], max = -1;
      for (int i = 0; i < N; ++i) {
         cin >> score[i];
         if (score[i] > max) {
            max = score[i];
         }
      }
      if (max != 0 && max % 10 == 0) {
         --max;
      }
//      for (int judgeNum = max / 10 + 1; ; ++judgeNum) {
      for (int judgeNum = 3; ; ++judgeNum) {

         int tmp_s = 0;
         for (int j = 0; j < N; ++j) {
            if (judgeNum == 1) {
               break;
            }
            if (score[j] < 2 || score[j] > judgeNum * 10 - 2) {
               continue;
            }
            if (judgeNum == 2 && score[j] % 2 == 1) {
               continue;
            }
            ++tmp_s;
         }
#ifndef RELEASE
         cout << judgeNum << " " << tmp_s << endl;
#endif
         int use_s = S;
         if (tmp_s >= S) {
            for (int j = 0; j < N; ++j) {
               int base = score[j] / judgeNum;
               // judgeNum == 1 no surprise
               if (base >= P) {
                  ++r;
               } else if (base == P - 1) {
                  if (score[j] % judgeNum == 0) {
                     if (use_s != 0) {
                        if (score[j] < 2 || score[j] > judgeNum * 10 - 2) {
                           continue;
                        }
                        if (judgeNum == 2 && score[j] % 2 == 1) {
                           continue;
                        }
                        ++r;
                        --use_s;
                     }
                  } else {
                     ++r;
                  }
               } else if (base == P - 2 && (score[j] % judgeNum >= 2) && use_s != 0) {
                  if (score[j] < 2) {
                     continue;
                  }
                  ++r;
                  --use_s;
               }
            }
            break;
         }
      }
      cout << "Case #" << totalcount + 1 << ": " << r << endl;
   }
   return 0;
}
