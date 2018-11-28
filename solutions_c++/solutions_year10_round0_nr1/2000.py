#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  ifstream fin("A-small.in");
  ofstream fout("A-small.out");

  int T;
  fin >> T;
  for(int test = 1; test < T + 1; test++)
  {
    int N, K;
    fin >> N;
    fin >> K;
    cout << "Case #" << test << ": ";
    int L = (1 << N);
    if(K % L == L - 1)
    {
      cout << "ON" << endl;
    }
    else
    {
      cout << "OFF" << endl;
    }
  }
}

