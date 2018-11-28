#include <fstream>
#include <iostream>
#include <cstring>
#include <limits>

using namespace std;

ifstream input;
ofstream output;

struct triplet {
    int a;
    int b;
    int c;
    triplet() {
        this->a = 0;
        this->b = 0;
        this->c = 0;
    }

    triplet(int _a, int _b, int _c) {
        this->a = _a;
        this->b = _b;
        this->c = _c;
    }
};

int cases = 0;

void do_math(int score, int min_score, int &surprise) {
      int base = (int)(score / 3);

      switch (score % 3)
      {
        case 0:
        {
          if (base >= min_score)
          {
              cases++;
          }
          else
          {
            if (surprise > 0 && base > 0 && base + 1 >= min_score)
            {
              cases++;
              surprise--;
            }
          }
          break;
        }

        case 1:
        {
          if (base >= min_score || base + 1 >= min_score)
          {
              cases++;
          }
          else
          {
            if (surprise > 0 && base + 1 >= min_score)
            {
              cases++;
              surprise--;
            }
          }
          break;
        }

        case 2:
        {
          if (base + 1 >= min_score || base >= min_score)
          {
            cases++;
          }
          else
          {
            if (surprise > 0 && base + 2 >= min_score)
            {
              cases++;
              surprise--;
            }
          }
          break;
        }
      }
}

void solve(int k) {
    int N, S, p;
    int scores[100] = {0};
    cases = 0;
    input >> N >> S >> p;
    for(int i = 0; i < N; i++) {
        //cases = 0;
        int score;
        input >> score;
        do_math(score, p, S);
    }
    output << "Case #" << k << ": " << cases << endl;
}

int main() {
    input.open("second_input.txt");
    output.open("second_output.txt");
    int T;
    input >> T;
    for(int i = 0; i < T; i++) {
        solve(i + 1);
    }
    input.close();
    output.close();
    return 0;
}
