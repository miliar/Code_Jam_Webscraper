// Daremonai
// OS: Ubuntu
// Compiler version: g++ 4.5.2

#include <iostream>
#include <fstream>
#include <exception>
#include <vector>
#include <string>

using namespace std;

int N;

int main(int argc, const char *argv[])
try {
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " filename" << endl;
    return -1;
  }
  ifstream input(argv[1]);
  if(!input) {
    cerr << "Could not open file " << argv[1] << endl;
    return -2;
  }
  int T = 0;
  int R,C;
  int count = 0;
  input >> T;
  bool impossible = false;

  char tiles[51][51] = { '.' };
  string str = "";

  for (int t=0;t<T;++t) {
    input >> R >> C;
    impossible = false;
    count = 0;

    for (int i=0;i<R;++i) {
      input >> str;
      for(int j=0;j<C;++j) {
        tiles[i][j] = str[j];
        if(str[j] == '#')
          ++count;
      }
    }
    cout << "Case #" << t+1 << ":" << endl;

    if (count % 4 != 0)
      impossible = true;
    else {
      for (int i =0; i<R-1;++i) {
        for (int j=0;j<C-1;++j) {
          if(tiles[i][j] == '/' || tiles[i][j] =='\\' || tiles[i][j] == '.')
            continue;
          if(tiles[i][j]   == '#' && tiles[i][j+1]   == '#' &&
             tiles[i+1][j] == '#' && tiles[i+1][j+1] == '#') {
            tiles[i][j]='/';
            tiles[i][j+1]='\\';
            tiles[i+1][j]='\\';
            tiles[i+1][j+1]='/';
          }
          else {
            impossible = true;
            break;
          }
        }
        if(impossible)
          break;
      }
    }

    if(impossible)
      cout << "Impossible" << endl;
    else {
      for (int i=0;i<R;++i) {
        for(int j=0;j<C;++j)
          cout << tiles[i][j];
        cout << endl;
      }
    }
  }

  return 0;
}
catch (exception & e) {
  cerr << "Error: " << e.what() << endl;
  return -2;
}
catch(...) {
  cerr << "Unknown exception." << endl;
  return -3;
}
