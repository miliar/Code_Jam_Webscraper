#include <iostream>
#include <vector>
#include <numeric>
#include <list>

using namespace std;

int main()
{
  int N;
  cin >> N;
  
  for (int i = 0; i < N; ++i)
    {
      int P, K, L;
      cin >> P >> K >> L;
      
      vector<long long> v;

      for (int j = 0; j < L; ++j)
	{
	  long long x; cin >> x;
	  v.push_back(x);
	}

      sort(v.begin(), v.end(), greater<long long>());
      long long pressed = 0;
      for (int j = 0; j < v.size(); ++j)
	{
	  pressed += ((j / K) + 1) * v[j];
	}

      cout << "Case #" << i + 1 << ": " << pressed << endl;
    }

  return 0;
}
