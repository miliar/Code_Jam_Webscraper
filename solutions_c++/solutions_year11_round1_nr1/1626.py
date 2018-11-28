#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

#define BUF_SIZE 65536

int integer_len(char* p)
{
  int res = 0;
  while (true)
  {
    if (*p < '0' || *p > '9')
    {
      return res;
    }
    p++;
    res++;
  }
}

int main()
{
  int T; cin >> T;

  string dummy_s;
  std::getline(cin, dummy_s);

  for (int t = 0; t < T; t++)
  {
    bool possible = true;
    string s; 

    //
    // input N
    //
    std::getline(cin, s);

    //
    // check N
    //
    bool possible_n = false;
    int N, PD, PG;

    // if N >= 100?
    char* buf_n = (char*)s.c_str();
    if (integer_len(buf_n) >= 3)
    {
      possible_n = true;
      char dummy[BUF_SIZE];
      sscanf("%s %d %d", dummy, &PD, &PG);
    } else
    {
      sscanf(buf_n, "%d %d %d", &N, &PD, &PG);
      for (int D = 1; D <= N; D++)
      {
        int win_i = D * PD / 100;
        double win_f = (double )D * (double )PD / 100.0;
        if ((double )win_i == win_f)
        {
          possible_n = true; break;
        }
      }
    }
    if (!possible_n) possible = false;

    if (possible)
    {
      if (PG == 100)
      {
        if (PD != 100) possible = false;
      }
      if (PG == 0)
      {
        if (PD != 0) possible = false;
      }
    }

    cout << "Case #" << t + 1 << ": " << (possible ? "Possible" : "Broken") << endl;
  }
}