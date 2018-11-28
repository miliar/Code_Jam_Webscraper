#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main () {
  string tmp;
  ifstream file("C-small-attempt0.in");
  ofstream file2("C-small-attempt0.out");
  if (file.is_open() && file2.is_open())
  {
    int T, R, K, N;
    file >> T;
    for (int i = 0; i < T; i++)
    {
      file >> R >> K >> N;
      int *group = new int[N];    

      int tmp;
      for (int h=0;h<N; h++)
      {
        file >> group[h];
      }
      
      int indStart = 0, indEnd = 1 < N ? 1 : 0;
      int sum = 0, curSum;
      for (int k = 0; k < R; k++)
      {        
        curSum = group[ indStart ];
        while (curSum + group[indEnd] <= K && indStart != indEnd)
        {
          curSum += group[indEnd];
          indEnd = (indEnd + 1 > N-1) ? 0 : indEnd + 1;
        }
        indStart = indEnd;
        indEnd = (indStart + 1 > N-1) ? 0 : indStart + 1;
        
        sum += curSum;
      }

      cout << "case" << i+1 << endl;
      file2 << "Case #" << i+1 << ": " << sum;
      if (i != T - 1)
        file2 << endl;

      delete[] group;
    }
    
    file2.close();
    file.close();
  }
  else cout << "Unable to open file"; 

  return 0;
}