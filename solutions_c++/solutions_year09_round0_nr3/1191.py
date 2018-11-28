#include <string>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int n;
  scanf("%d\n", &n);
  string pattern = "welcome to code jam";
  vector<int> p1(pattern.length(), 0);
  vector<int> p2(pattern.length(), 0);
  for (int test_case=0; test_case<n; test_case++)
  {
    string text;
    getline(cin, text);
    vector<int> &current = p2;
    vector<int> &prev = p1;
    fill(prev.begin(), prev.end(), 0);

    for (int i=0; i<text.length(); i++)
    {
      current[0] = prev[0];
      if (text[i]==pattern[0])
        current[0]++;
      for (int j=1; j<pattern.length(); j++)
      {
        current[j] = prev[j];
        if (text[i]==pattern[j])
          current[j] += prev[j-1];
        current[j] %=10000;
      }
      swap(prev, current);
    }
    printf("Case #%d: %04d\n", test_case+1, prev[pattern.length()-1]);
  }
  return 0;
}

