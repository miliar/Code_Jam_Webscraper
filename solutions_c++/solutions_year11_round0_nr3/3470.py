#include <cstdio>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

long
GetSum2(vector<long>& values)
{
  long v = 0;
  for(size_t i = 0; i < values.size(); ++i)
  {
    v += values[i];
  }

  return v;
}

long
GetSum(vector<long>& values)
{
  long v = 0;
  for(size_t i = 0; i < values.size(); ++i)
  {
    v ^= values[i];
  }

  return v;
}

long
GetMin(vector<long>& values)
{
long min_ = 1e6;
for(size_t i = 0; i < values.size(); ++i) min_ = min(min_, values[i]);

return min_;
}

void main_(int iTest)
{

int count;
cin >> count;

vector<long> values(count);

for(int i = 0; i < count; ++i)
{
  cin >> values[i];
}

long max_ = 0;
if(0 == GetSum(values))
{
max_ = GetSum2(values) - GetMin(values);

}

if(max_ == 0)
{
printf("Case #%d: NO\n", iTest);
}
else
{
printf("Case #%d: %ld\n", iTest, max_);
}
}


int main()
{

int nTest = 0;
cin >> nTest;

for(int i = 0; i < nTest; ++i)
{
main_(i+1);
}


return 0;
}
