#include <map>
#include <utility>
#include <iostream>
#include <vector>
using namespace std;

const int NN = 100003;
map<pair<int, int>, int> cache;

int
bin(int n, int k)
{
  if (n < k || k < 0)
    return 0;
  map<pair<int, int>, int>::iterator xx = cache.find(make_pair(n, k));
  if (xx != cache.end()) return xx->second;
  int s = 1;
  vector<int> to_divide;
  for (int i = 2; i <= n-k; i++)
    {
      int tmp = i;
      for (int j = 2; tmp > 1; j++)
        {
          while (tmp % j == 0)
            {
              to_divide.push_back(j);
              tmp /= j;
            }
        }
    }
  int fin = 0;
  int ss = to_divide.size();
  for (int i = k+1; i <= n; i++)
    {
      int tmp = i;
      if (fin < ss)
        {
          for (int j = 0; j < to_divide.size(); j++)
            {
              if (tmp == 1)
                break;
              if (to_divide[j] != 0 && tmp % to_divide[j] == 0)
                {
                  tmp /= to_divide[j];
                  to_divide[j] = 0;
                  fin ++;
                }
            }
        }
      s = (tmp*s) % NN;
    }
  cache[make_pair(n, k)] = s % NN;
  return s % NN;
}

int
calcola(int N [501][501], int n, int k)
{
  if (k == 1) return 1;
  if (k == 2) return 1;
  if (k == 3) return n-3;
  if (N[n][k] != -1) return N[n][k];
  long long int s = 0;
  for (int t = 1; t < k; t++)
    s = (s + ((long long int)bin(n-k-1, k-t-1)) * calcola(N, k, t)) % NN;
  N[n][k] = s;
  return s;
}

int
main(void)
{
  int C, n;
  cin >> C;
  for (int c = 0; c < C; c++)
  {
    cin >> n;
    int N[501][501];
    for (int i = 0; i < 501; i++)
      for (int j = 0; j < 501; j++)
        N[i][j] = -1;
    int s = 1;
    for (int i = 2; i < n; i++)
      s = (s + calcola(N, n, i)) % NN;
    cout << "Case #" << (c+1) << ": " << s << endl;
  }
}
