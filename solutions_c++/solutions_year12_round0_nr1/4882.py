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

#define N 26

char t[N] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
  int test_cases;
  scanf("%d\n", &test_cases);
  for(int i=1; i <= test_cases; ++i)
  {
    printf("Case #%d: ", i);
    char c;
    while((c=getchar()) != '\n' && c != EOF) 
      printf("%c", (c == ' ') ? c: t[c-'a']);
    printf("\n"); 
  }

}
