#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#define MAX 1123
#define INF 99999999
using namespace std;

void apply(char *s2, char *s, const vector <int> &perm, int k)
{
  int j = 0;
  while(j < strlen(s))
    {
      for(int i = 0; i < k; i++)
	{
	  s2[perm[i%k] + j] = s[i + j];
	}
      j+=k;
    }
}

int size(char *s2)
{
  int g = 1;

  for(int i = 0; i < strlen(s2) - 1; i++)
    {
      if(s2[i] != s2[i+1]) g++;
    }

  return g;
}


int main(int argc, char *argv[]){

  int n, k, t = 1;
  char s[MAX], s2[MAX];
  scanf("%d",&n);

  while(n--)
    {
      scanf("%d",&k);
      scanf("%s",s);
      strcpy(s2, s);

      vector <int> perm;
      int m = INF;
      perm.resize(k);
      for(int i = 0; i < k; i++) perm[i] = i;

      do
	{
	  apply(s2, s, perm, k);
	  m = min(m, size(s2));
	  // printf("[%s][%d]\n",s2, size(s2));
	}
      while(next_permutation(perm.begin(), perm.end()));
	
      printf("Case #%d: %d\n",t++, m);
    }

  return 0;
}
