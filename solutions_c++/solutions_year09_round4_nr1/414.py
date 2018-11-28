#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std; typedef unsigned long ulong; typedef long long llong;
typedef unsigned long long ullong;

int main()
{
int cases;
int k[100];
char s[100];

cin >> cases; getchar();

for(int loop=1;loop<=cases;loop++)
{
  int n; cin >> n;
  for(int i=0;i<n;i++) {scanf("%s",s); char*t=strrchr(s,'1'); k[i]=t?t-s:0; }

  int t=0;
  for(int i=0;i<n;i++)
  {
    int j=i; for(; j<n && k[j]>i;j++)
    assert(j<n);

    t+=j-i; if(j>i) rotate(k+i,k+j,k+j+1);
  }

  printf("Case #%d: ",loop);
  printf("%d\n",t);

  fflush(stdout);
}

}
