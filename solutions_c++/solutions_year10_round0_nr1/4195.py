#include <iostream>
#include <fstream>
using namespace std;

int main () {
  string tmp;
  ifstream file("A-small-attempt2.in");
  ofstream file2("A-small-attempt2.out");
  if (file.is_open() && file2.is_open())
  {
    int T, N, K;
    file >> T;
    for (int i = 0; i < T; i++)
    {
      file >> N >> K;
      bool* power = new bool[N+1];
      bool* power_new = new bool[N+1];
      bool* onoff = new bool[N];
      for (int k = 0; k < N; k++)
      {
        power[k] = false;
        power_new[k] = false;
        onoff[k] = false;
      }
      power[0] = true;
      power_new[0] = true;
      power[N] = false;
      for (int j=0; j < K;j++)
      {
        for(int h=0;h<N;h++)
        {
          if (power[h])
            onoff[h] = !onoff[h];
          if (power_new[h] && onoff[h])
            power_new[h+1] = true;
          if (!onoff[h])
            power_new[h+1] = false;
        }

        for(int h=0;h<N;h++)
        {
          power[h] = power_new[h];
        }
      }      
      file2 << "Case #" << i+1 << ": " << (power[N-1] && onoff[N-1] ? "ON" : "OFF");
      if (i != T - 1)
        file2 << endl;

      delete[] power;
      delete[] power_new;
      delete[] onoff;
    }
    
    file2.close();
    file.close();
  }
  else cout << "Unable to open file"; 

  return 0;
}