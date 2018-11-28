#include <iostream>
#include <vector>
using namespace std;

bool snappers(int k, int size, int lastsize, vector<bool>& snapps);
char* snap_mode(bool mode);

int main(void)
{
  int a, n, k, n_a, lastsize;
  vector<bool> result(0), snapps(0), test(0);
  cin >> a;
  n_a = a;
  result.resize(a, false);
  while(n_a > 0)
    {
      cin >> n >> k;
      snapps.resize(n, false);
      result[a - n_a--] = snappers(k, n, lastsize, snapps);
      lastsize = n;
    }

  for(int i = 0; i < a; ++i)
    cout << "Case #" << (i+1) << ": " << snap_mode(result[i]) << endl;

  return 0;
}

bool snappers(int k, int size, int lastsize, vector<bool>& snapps)
{
  bool last = true;
  int n = 0;

  for(int i = 0; i < size && i < lastsize; ++i)
    snapps[i] = false;

  while(k --> 0)
    {
      last = true;
      n = 0;
      while(last && n < size)
	{
	  last = snapps[n];
	  snapps[n] = !snapps[n];
	  n++;
	}
    }

  n = 0;
  while(n < size && snapps[n]) n++;
  return n == size;
}

char* snap_mode(bool mode)
{
  if(mode) return "ON";
  return "OFF";
}
