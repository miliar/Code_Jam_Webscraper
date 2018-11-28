#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int T, N;

int count(vector<int> id)
{
  int c = 0;
  for (int i = 0; i < N; i++)
    for (int j = i+1; j < N; j++)
      if (id[i] > id[j]) c++;
  return c;
}

int solve()
{
  cin >> N;

  vector<int> pos(N);
  for (int i = 0; i < N; i++)
    {
      string s;
      cin >> s;

      int k = -1;
      for (int j = 0; j < N; j++)
	if (s[j] == '1') k = j;

      pos[i] = k;
    }

  vector<int> id(N);
  for (int i = 0; i < N; i++) id[i] = i;
  
  int answer = (int)1e9;
  do
  {
    bool ok = true;
    for (int i = 0; i < N; i++) 
      if (pos[id[i]] > i) ok = false;
    if (ok)
      {
	int cur = count(id);
	if (cur < answer) answer = cur;
      }
  } while (next_permutation(id.begin(), id.end()));

  return answer;
}

int main()
{
  cin >> T;
  for (int i = 0; i < T; i++)
    cout << "Case #" << i+1 << ": " << solve() << endl;

  return 0;
}
