#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
int main()
{
  int T;
  cin >> T;
  int C = 1;
  while(T--)
    {
      int N, L, H;
      cin >> N >> L >> H;
      vector<int> nums;
      int n;
      for(int i = 0 ; i < N; i++)
	{
	  cin >> n; 
	  nums.push_back(n);
	}
      bool cool = false;
      int A = 0;
      for(int i = L; i <= H; i++)
	{
	  bool ok = true;
	  for(int j = 0 ; j < nums.size(); j++)
	    if( i % nums[j] != 0 && nums[j] % i != 0)
	      ok = false;
	  if( ok ){
	    cool = true;
	    A = i;
	    break;
	  }
	    
	}
      if( cool )
	printf("Case #%d: %d\n", C++, A);
      else
	printf("Case #%d: NO\n", C++);
    }
}
