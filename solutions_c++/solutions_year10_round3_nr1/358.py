#include <iostream>
using namespace std;

int solve()
{
  int N;
  int A[1010];
  int B[1010];
  cin >> N;
  
  for(int i = 0; i < N; i++)
  {
    cin >> A[i] >> B[i];
  }
  
  int ret = 0;
  for(int i = 0; i < N-1; i++)
  {
    for(int j = i+1; j < N; j++)
    {
      float a1 = A[i];
      float b1 = B[i] - A[i];
      float a2 = A[j];
      float b2 = B[j] - A[j];
      float x = (a2 - a1) / (b1 - b2);
      
      if(b1 == b2)
        continue;
      
      //cout << b1 << " " << b2 << endl;
      
      //cout << x << endl;
      
      if(x > 0 && x < 1)
        ret ++;
    }
  }
  return ret;
}

int main()
{
  int T;
  cin >> T;
  
  for(int i = 1; i < T+1; i++)
  {
    cout << "Case #" << i << ": " << solve() << endl;
  }
}
