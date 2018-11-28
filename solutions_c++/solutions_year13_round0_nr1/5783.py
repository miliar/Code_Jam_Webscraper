#include <iostream>
using namespace std;

static const char* results[4] = {
   "X won",
   "O won",
   "Draw",
   "Game has not completed"
};


int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   char inputs[4][4];
   for (unsigned t = 0; t < T; ++t) {
      unsigned result = 3;

      // read input
      char ch = 0;
      for (unsigned r = 0; r < 4; ++r) {
         for (unsigned c = 0; c < 4; ++c) {
            cin >> ch;
            switch (ch) {
               case 'O':
                  ch = 4;
                  break;

               case 'X':
                  ch = 0;
                  break;

               case 'T':
                  ch = 32;
                  break;

               default:
                  ch = 64;
                  break;
            }
            inputs[r][c] = ch;
         }
      }

      unsigned sum = 0;
      bool hasDot = false;
      // Check right.
      for (unsigned r = 0; r < 4; ++r) {
         sum =  inputs[r][0] +
                inputs[r][1] +
                inputs[r][2] +
                inputs[r][3];
         switch (sum) {
            case 0:
            case 32:
               result = 0;
               break;

            case 16:
            case 44:
               result = 1;
               break;
         }
         if (result < 2) {
            goto done;
         }
         hasDot = hasDot || sum >=64;
      }

      // Check down.
      for (unsigned c = 0; c < 4; ++c) {
         sum =  inputs[0][c] +
                inputs[1][c] +
                inputs[2][c] +
                inputs[3][c];
         switch (sum) {
            case 0:
            case 32:
               result = 0;
               break;

            case 16:
            case 44:
               result = 1;
               break;
         }
         if (result < 2) {
            goto done;
         }
         hasDot = hasDot || sum >=64;
      }

      // Check diag1.
      sum =  inputs[0][0] +
             inputs[1][1] +
             inputs[2][2] +
             inputs[3][3];
      switch (sum) {
         case 0:
         case 32:
            result = 0;
            break;

         case 16:
         case 44:
            result = 1;
            break;
      }
      if (result < 2) {
         goto done;
      }
      hasDot = hasDot || sum >=64;

      // Check diag2.
      sum =  inputs[0][3] +
             inputs[1][2] +
             inputs[2][1] +
             inputs[3][0];
      switch (sum) {
         case 0:
         case 32:
            result = 0;
            break;

         case 16:
         case 44:
            result = 1;
            break;
      }
      if (result < 2) {
         goto done;
      }
      hasDot = hasDot || sum >=64;

      if (!hasDot) {
         result = 2;
      }

      done:
      cout << "Case #" << t + 1 << ": " << results[result] << endl;
   }

   return 0;
}

