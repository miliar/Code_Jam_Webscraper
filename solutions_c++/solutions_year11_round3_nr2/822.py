#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
  long long T, L, t, N, C, time, max, a, x, start;
  vector<int> stars;

  ifstream in;
  ofstream out;

  if (argc == 3)
  {
    in.open(argv[1]);
    if (!in.is_open())
    {
      cerr << "Error opening " << argv[1] << endl;
      return 0;
    }
    out.open(argv[2]);
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening " << argv[2] << endl;
      return 0;
    }
  }
  else
  {
    in.open("in.txt");
    if (!in.is_open())
    {
      cerr << "Error opening in.txt" << endl;
      return 0;
    }
    out.open("out.txt");
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening out.txt" << endl;
      return 0;
    }
  }

  in >> T;
  for (int i = 0; i < T; i++)
  {
    out << "Case #" << i + 1 << ": ";
    cout << "Case #" << i + 1 << ":" << endl;
    in >> L >> t >> N >> C;
    stars.resize(N, 0);
    for (int j = 0; j < C; j++)
    {
      in >> a;
      for (int k = 0; k < N; k++)
      {
        x = k * C + j;
        if (x >= N) break;
        stars[x] = a;
      }
    }

    start = -1;
    time = 0;
    for (int j = 0; j < N; j++)
    {
      x = stars[j] * 2;
      if (t >= time && t < time + x)
      {
        start = j;
        stars[j] -= (t - time) / 2;
        cout << "Start: " << start << " " << stars[j] << endl;
      }
      time += x;
    }

    for (int l = 0; l < L; l++)
    {
      max = start;
      for (int j = start + 1; j < N; j++)
        if (stars[j] > stars[max])
          max = j;
      if (!stars[max]) break;
      time -= stars[max];
      stars[max] = 0;
      cout << "Booster at " << max << endl;
    }

    out << time << endl;
  }

  return 0;
}

