#include <iostream>
#include <string>

int
main()
{
  enum color { RED, BLUE, EMPTY };
  color data[50][50];
  int T;
  std::cin >> T;
  for (int t(1); t <= T; ++t) {
    int N;
    int K;
    std::cin >> N >> K;
    for (int i(0); i < N; ++i) {
      for (int j(0); j < N; ++j) {
        data[i][j] = EMPTY;
      }
    }
    bool ok_r(false);
    bool ok_b(false);
// STAGE 1
    for (int i(0); i < N; ++i) {
      std::string str;
      std::cin >> str;
      color cur(EMPTY);
      int num(0);
      for (int j(N - 1), p(0); j >= 0; --j) {
        switch (str[j]) {
        case 'R':
          if (cur == RED) {
            if (++num >= K) {
              ok_r = true;
            }
          } else {
            cur = RED;
            num = 1;
          }
          data[i][p++] = RED;
          break;
        case 'B':
          if (cur == BLUE) {
            if (++num >= K) {
              ok_b = true;
            }
          } else {
            cur = BLUE;
            num = 1;
          }
          data[i][p++] = BLUE;
          break;
        case '.':
          break;
        }
      }
    }
    if (ok_r && ok_b) {
      std::cout << "Case #" << t << ": Both\n";
      continue;
    }
    std::cerr << "1\n";
// STAGE 2
    for (int i(0); i < N; ++i) {
      color cur(EMPTY);
      int num(0);
      for (int j(0); j < N; ++j) {
        switch (data[j][i]) {
        case RED:
          if (cur == RED) {
            if (++num >= K) {
              ok_r = true;
            }
          } else {
            cur = RED;
            num = 1;
          }
          break;
        case BLUE:
          if (cur == BLUE) {
            if (++num >= K) {
              ok_b = true;
            }
          } else {
            cur = BLUE;
            num = 1;
          }
          break;
        case EMPTY:
          cur = EMPTY;
          num = 0;
          break;
        }
      }
    }
    if (ok_r && ok_b) {
      std::cout << "Case #" << t << ": Both\n";
      continue;
    }
    std::cerr << "2\n";
// STAGE 3
    for (int i(0); i < N; ++i) {
      color cur(EMPTY);
      int num(0);
      for (int j(0); j <= i; ++j) {
        switch (data[i - j][j]) {
        case RED:
          if (cur == RED) {
            if (++num >= K) {
              ok_r = true;
            }
          } else {
            cur = RED;
            num = 1;
          }
          break;
        case BLUE:
          if (cur == BLUE) {
            if (++num >= K) {
              ok_b = true;
            }
          } else {
            cur = BLUE;
            num = 1;
          }
          break;
        case EMPTY:
          cur = EMPTY;
          num = 0;
          break;
        }
      }
    }
    if (ok_r && ok_b) {
      std::cout << "Case #" << t << ": Both\n";
      continue;
    }
    std::cerr << "3\n";
// STAGE 4
    for (int i(1); i < N; ++i) {
      color cur(EMPTY);
      int num(0);
      for (int j(0); j < N - i; ++j) {
        switch (data[i + j][N - 1 - j]) {
        case RED:
          if (cur == RED) {
            if (++num >= K) {
              ok_r = true;
            }
          } else {
            cur = RED;
            num = 1;
          }
          break;
        case BLUE:
          if (cur == BLUE) {
            if (++num >= K) {
              ok_b = true;
            }
          } else {
            cur = BLUE;
            num = 1;
          }
          break;
        case EMPTY:
          cur = EMPTY;
          num = 0;
          break;
        }
      }
    }
    if (ok_r && ok_b) {
      std::cout << "Case #" << t << ": Both\n";
      continue;
    }
    std::cerr << "4\n";
// STAGE 5
    for (int i(0); i < N; ++i) {
      color cur(EMPTY);
      int num(0);
      for (int j(0); j <= i; ++j) {
        switch (data[i - j][N - 1 - j]) {
        case RED:
          if (cur == RED) {
            if (++num >= K) {
              ok_r = true;
            }
          } else {
            cur = RED;
            num = 1;
          }
          break;
        case BLUE:
          if (cur == BLUE) {
            if (++num >= K) {
              ok_b = true;
            }
          } else {
            cur = BLUE;
            num = 1;
          }
          break;
        case EMPTY:
          cur = EMPTY;
          num = 0;
          break;
        }
      }
    }
    if (ok_r && ok_b) {
      std::cout << "Case #" << t << ": Both\n";
      continue;
    }
    std::cerr << "5\n";
// STAGE 6
    for (int i(1); i < N; ++i) {
      color cur(EMPTY);
      int num(0);
      for (int j(0); j < N - i; ++j) {
        switch (data[i + j][j]) {
        case RED:
          if (cur == RED) {
            if (++num >= K) {
              ok_r = true;
            }
          } else {
            cur = RED;
            num = 1;
          }
          break;
        case BLUE:
          if (cur == BLUE) {
            if (++num >= K) {
              ok_b = true;
            }
          } else {
            cur = BLUE;
            num = 1;
          }
          break;
        case EMPTY:
          cur = EMPTY;
          num = 0;
          break;
        }
      }
    }
    if (ok_r && ok_b) {
      std::cout << "Case #" << t << ": Both\n";
    } else if (ok_r) {
      std::cout << "Case #" << t << ": Red\n";
    } else if (ok_b) {
      std::cout << "Case #" << t << ": Blue\n";
    } else {
      std::cout << "Case #" << t << ": Neither\n";
    }
  }
  return 0;
}
