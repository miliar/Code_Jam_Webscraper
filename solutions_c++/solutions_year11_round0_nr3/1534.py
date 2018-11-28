#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;


int nums[1234];
int val[1234][1234];

int s(int a, int b)
{
  int c = a & b;
  return (a^c) | (b^c);
}

int main(void)
{
  int N;
  cin >> N;
  for(int c = 1; c <= N ;c++)
  {
    int n;
    cin >> n;
    for(int i = 0 ; i < n; i++) cin >> nums[i];
    sort(nums, nums+n);
    int sum = 0;
    for(int i = 0; i < n; i++) sum = s(sum,nums[i]);
    printf("Case #%d: ", c);

    if(sum != 0) printf("NO\n");
    else
    {
      sum=0;
      for(int i = 1; i < n; i++) sum+=nums[i];
      printf("%d\n",sum);
    }
  }
  return 0;
}
