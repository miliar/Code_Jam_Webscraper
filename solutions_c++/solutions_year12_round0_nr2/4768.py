#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef map<int, int> mii;

typedef long long ll;

#define N 105

int t[N];
int p;

int max(int i, int surprise)
{
  if(i < 0)
    return 0;

  int mod= t[i]%3;
  int best_score = (t[i] / 3) + (mod>0); 

  // If it's already greater or equals. 
  if(best_score >= p)
    return max(i-1, surprise) + 1;

  if(surprise > 0 && mod != 1 && best_score + 1 >= p && t[i] > 1)
    return max(i-1, surprise - 1) + 1;

  return max(i-1, surprise);
}

int main()
{
  int test_cases;
  scanf("%d\n", &test_cases);
  for(int i=1; i <= test_cases; ++i)
  {
    printf("Case #%d: ", i);
    
    int n, s;
    scanf("%d%d%d", &n, &s, &p);
    for(int i=0; i < n; ++i)
      scanf("%d", &t[i]);    

    printf("%d\n", max(n-1, s));
  }
}
