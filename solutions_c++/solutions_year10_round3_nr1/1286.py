#include <fstream>
#include <iostream>

using namespace std;

int main()
{
  ifstream fin("A-small.in");
  ofstream fout("A-small.out");

  int T;
  fin >> T;
  for(int test = 1; test <= T; test++)
  {
    int N;
    fin >> N;
    int A[N];
    int B[N];
    for(size_t i = 0; i < N; i++)
    {
      fin >> A[i];
      fin >> B[i];
    }

    int result = 0;
    for(size_t i = 1; i < N; i++)
    {
      for(size_t j = 0; j < i; j++)
      {
        if((A[i] < A[j] && B[i] > B[j]) ||
           (A[i] > A[j] && B[i] < B[j]))
        {
          result++;
        }
      }
    }

    cout << "Case #" << test << ": "<< result << endl;
  }
}

