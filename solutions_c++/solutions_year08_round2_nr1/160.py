#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <complex>

using namespace std;

int mod(int x) { long long ret = x % 3; while(ret < 0) ret += 3; return ret; }

int main()
{
  int tc;
  cin >> tc;
  for(int z = 0; z < tc; z++)
  {
      long long count[9];
      pair<int, int> modulo[9];
      for(int i = 0; i < 9; i++)
      {
	  modulo[i].first = i / 3;
	  modulo[i].second = i % 3;
      }

      memset(count, 0, sizeof count);
      long long n, A, B, C, D, X, Y, M;
      cin >> n >> A >> B >> C >> D >> X >> Y >> M;

      count[mod(X % 3) * 3 + mod(Y % 3)]++;
      for(int i = 1; i < n; i++) 
      {
	  X = (A * X + B) % M;
	  Y = (C * Y + D) % M;
	  count[mod(X % 3) * 3 + mod(Y % 3)]++;
      }

      long long retVal = 0;
      for(int i = 0; i < 9; i++)
	  for(int j = 0; j < 9; j++)
	      for(int k = 0; k < 9; k++)
	      {
		  int sumA = (modulo[i].first + modulo[j].first + modulo[k].first);
		  int sumB = (modulo[i].second + modulo[j].second + modulo[k].second);

		  if(sumA % 3 || sumB % 3) continue;

		  long long val1 = count[i];
		  long long val2 = (count[j] - (i == j ? 1 : 0));
		  long long val3 = (count[k] - (j == k ? 1 : 0) - (i == k ? 1 : 0));

		  if(val1 < 0 || val2 < 0 || val3 < 0) continue;
		  retVal += val1 * val2 * val3;
	      }

      cout << "Case #" << z + 1 << ": " << retVal/6 << endl;

  }
}
