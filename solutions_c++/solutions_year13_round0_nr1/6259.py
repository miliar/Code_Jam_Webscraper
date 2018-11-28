#include <iostream>
#include <map>
#include <utility>

using namespace std;

bool charOrT(char c, const char symbol) {
  return c == symbol || c == 'T';
}

pair<int, int> p(int i, int j) {
  return pair<int, int>(i, j);
}

int main(void) {
  int cases;
  cin >> cases;
  char c; int i, j, k;
  for(int current = 0; current < cases; ++current) {
    map<pair<int, int>, char> board;
    for(i = 0; i < 4; ++i) {
      for(j = 0; j < 4; ++j) {
        cin >> c;
        board.insert(pair<pair<int, int>, char>(p(i, j), c));
      }
    }

    bool breakOut = false;

    for(i = 3; i < 4; ++i) {
      for(j = 0; j < 4; ++j) {
        char s = board[p(i, j)];
        if(charOrT(s, '.')) {
          continue;
        }
        for(k = 0; k < 4; ++k) {
          if(!charOrT(board[p(i-k,j)], s)) {
            breakOut = true;
            break;
          }
        }
        if(!breakOut) {
          cout << "Case #" << (current + 1) << ": " << s << " won" << endl;
          breakOut = true;
          break;
        } else {
          breakOut = false;
        }
      }
      if(breakOut) {
        break;
      }
    }
    if(breakOut) continue;

    for(i = 0; i < 1; ++i) {
      for(j = 0; j < 4; ++j) {
        char s = board[p(i, j)];
        if(charOrT(s, '.')) {
          continue;
        }
        for(k = 0; k < 4; ++k) {
          if(!charOrT(board[p(i+k,j)], s)) {
            breakOut = true;
            break;
          }
        }
        if(!breakOut) {
          cout << "Case #" << (current + 1) << ": " << s << " won" << endl;
          breakOut = true;
          break;
        } else {
          breakOut = false;
        }
      }
      if(breakOut) {
        break;
      }
    }
    if(breakOut) continue;

    for(i = 0; i < 4; ++i) {
      for(j = 3; j < 4; ++j) {
        char s = board[p(i, j)];
        if(charOrT(s, '.')) {
          continue;
        }
        for(k = 0; k < 4; ++k) {
          if(!charOrT(board[p(i,j - k)], s)) {
            breakOut = true;
            break;
          }
        }
        if(!breakOut) {
          cout << "Case #" << (current + 1) << ": " << s << " won" << endl;
          breakOut = true;
          break;
        } else {
          breakOut = false;
        }
      }
      if(breakOut) {
        break;
      }
    }
    if(breakOut) continue;

    for(i = 0; i < 4; ++i) {
      for(j = 0; j < 1; ++j) {
        char s = board[p(i, j)];
        if(charOrT(s, '.')) {
          continue;
        }
        for(k = 0; k < 4; ++k) {
          if(!charOrT(board[p(i,j + k)], s)) {
            breakOut = true;
            break;
          }
        }
        if(!breakOut) {
          cout << "Case #" << (current + 1) << ": " << s << " won" << endl;
          breakOut = true;
          break;
        } else {
          breakOut = false;
        }
      }
      if(breakOut) {
        break;
      }
    }
    if(breakOut) continue;

    char s = board[p(0, 0)];
    for(i = 0; i < 4; ++i) {
      if(charOrT(s, '.')) {
        breakOut = true;
        break;
      }
      if(!charOrT(board[p(i,i)], s)) {
        breakOut = true;
        break;
      }
    }
    if(!breakOut) {
      cout << "Case #" << (current + 1) << ": " << s << " won" << endl;
      continue;
    } else {
      breakOut = false;
    }
    s = board[p(3, 3)];
    for(i = 3; i >= 0; --i) {
      if(charOrT(s, '.')) {
        breakOut = true;
        break;
      }
      if(!charOrT(board[p(i,i)], s)) {
        breakOut = true;
        break;
      }
    }
    if(!breakOut) {
      cout << "Case #" << (current + 1) << ": " << s << " won" << endl;
      continue;
    } else {
      breakOut = false;
    }
    s = board[p(0, 3)];
    for(i = 0; i < 4; ++i) {
      if(charOrT(s, '.')) {
        breakOut = true;
        break;
      }
      if(!charOrT(board[p(3-i,i)], s)) {
        breakOut = true;
        break;
      }
    }
    if(!breakOut) {
      cout << "Case #" << (current + 1) << ": " << s << " won" << endl;
      continue;
    } else {
      breakOut = false;
    }
    s = board[p(3, 0)];
    for(i = 3; i >= 0; --i) {
      if(charOrT(s, '.')) {
        breakOut = true;
        break;
      }
      if(!charOrT(board[p(3-i,i)], s)) {
        breakOut = true;
        break;
      }
    }
    if(!breakOut) {
      cout << "Case #" << (current + 1) << ": " << s << " won" << endl;
      continue;
    } else {
      breakOut = false;
    }

    for(i = 0; i < 4; ++i) {
      for(j = 0; j < 4; ++j) {
        if(board[p(i, j)] == '.') {
          cout << "Case #" << (current + 1) << ": Game has not completed" << endl;
          breakOut = true;
          break;
        }
      }
      if(breakOut) break;
    }
    if(breakOut) continue;

    cout << "Case #" << (current + 1) << ": Draw" << endl;
          
  }
  return 0;
}
        
