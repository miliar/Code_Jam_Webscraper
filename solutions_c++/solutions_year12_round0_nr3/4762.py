#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

#define ll long long
using namespace std;


int a, b;

int size(int n)
{
  if(n / 1000000)
    return 6;
  if(n / 100000)
    return 5;
  if(n / 10000)
    return 4;
  if(n / 1000)
    return 3;
  if(n / 100)
    return 2;
  if(n / 10)
    return 1;
  return 0;
}

int power(int n)
{
  int base = 1;
  while(n--)
    base *= 10;
  return base;
}

int shift(int n, int len)
{
  int c = n / power(len);
  n -= c * power(len);
  return n*10 + c;
}

int go(int n, int len)
{
  int ans = 0;
  int next;

  for(int i=0; i<len; i++)
  {
    n = shift(n, len);

    if(n <= a)
      continue;
    if(n > b)
      continue;
    if(size(n) == len)
      ans++;
  }

  return ans;
}

int main(void)
{
  freopen("g:\\input.txt", "rt", stdin);
  freopen("g:\\output.txt", "wt", stdout);
  
  int c;
  scanf("%d ", &c);
    
  for(int i=0; i<c; i++)
  {
    cout<<"Case #"<<i+1<<": ";
    
    cin>>a>>b;
    int ans = 0;

    while(a <= b)
    {
      int len = size(a);

      ans += go(a, len);

      a++;
    }

    cout<<ans<<endl;
  }

  return 0;
}