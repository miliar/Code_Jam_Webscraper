#include <cmath>
#include <map>
#include <cstring>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std; typedef unsigned long ulong; typedef long long llong;

int main()
{
int cases;

cin >> cases;

for(int loop=1;loop<=cases;loop++)
{
  int i,j,k,m=10000;
  char s[10000],s2[10000];

  cin >> k;
  scanf("%s",s2); int n=strlen(s2);
  char t[k];

  int p[k]; for(i=0;i<k;i++) p[i]=i;

  do
  {
    strcpy(s,s2);
    for(i=0;i<n/k;i++)
    {
      int off=i*k; for(j=0;j<k;j++) t[j]=s[off+p[j]];
      for(j=0;j<k;j++) s[off+j]=t[j];
    }
    
    int t=1;
    for(i=1;i<n;i++) if(s[i]!=s[i-1]) t++;
    m = min(m,t);
    
  } while (next_permutation(p,p+k));

  printf("Case #%d: %d\n",loop,m);
}

}
