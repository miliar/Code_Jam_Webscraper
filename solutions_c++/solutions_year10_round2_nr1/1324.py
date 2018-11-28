// Daremonai
// OS: Gentoo
// Compiler version: g++ 4.3.4

#include <iostream>
#include <fstream>
#include <exception>
#include <vector>
#include <string>

using namespace std;

int T, N, M;

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

  input >> T;

  int result = 0;
  int t;
  for (t = 0; t < T; ++t) {
    input >> N >> M;

    vector<string> existing;
    existing.clear();
    result = 0;
    if (N != 0)
    {
      int n;
      for (n = 0; n < N; ++n) {
        string str;
        input >> str;
        existing.push_back(str);
      }

      int m;
      vector<string> to_compute;
      for (m = 0; m < M; ++m) {
        string str;
        input >> str;

        while (str.find_last_of("/") != string::npos)
        {
          bool found = false;
          for (int i = 0; i < existing.size(); ++i)
          {
            if (existing[i] == str)
            {
              found = true;
              break;
            }
          }

          if (found)
            break;
          else
          {
            ++result;
            existing.push_back(str);
          }
          str = str.substr(0, str.find_last_of("/"));
        }
      }
    }
    else
    {
      int m;
      for (m = 0; m < M; ++m) {
        string str;
        input >> str;
        if (m == 0)
        {
          ++result;
          while (1)
          {
            int pos = str.find_last_of('/');
            if (pos == 0)
              break;
            str = str.substr(0, pos);
            existing.push_back(str.substr(0, pos));
            ++result;
          }
          continue;
        }

        while (str.find_last_of("/") != string::npos)
        {
          bool found = false;
          for (int i = 0; i < existing.size(); ++i)
          {
            if (existing[i] == str)
            {
              found = true;
              break;
            }
          }

          if (found)
            break;
          else
          {
            ++result;
            existing.push_back(str);
          }
          str = str.substr(0, str.find_last_of("/"));
        }
      }
    }
    cout << "Case #" << t + 1 << ": " << result << "\n";
  }

  cout.flush();
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
