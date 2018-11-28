#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
  ifstream ff("input.txt");
  ofstream gg("output.txt");

  int T, N, xs, xc, min;
  vector<int> candy;

  ff >> T;
  for(int t = 0; t < T; ++t)
  {
    ff >> N; 
    xs = 0; xc = 0; min = 1000999;
    candy.resize(N);
    for(int n = 0; n < N; ++n)
    {
      ff >> candy[n];
      xs += candy[n];
      xc ^= candy[n];
      if(candy[n] < min)
	min = candy[n];
    }

    if(xc != 0)
      gg << "Case #" << t+1 << ": NO" << endl;
    else
      gg << "Case #" << t+1 << ": " << xs - min << endl;

  }

  return 0;
}
