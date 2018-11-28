#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <string>

using namespace std;

int n;
vector<int> s, a, b;
bool found;

void search(int now,int sum1, int sum2)
{
  if (sum1==sum2 && sum1!=0)
  {
    found = true;
    for (int i=0;i<a.size();++i)
      printf("%d ", a[i]);
    printf("\n");
    for (int i=0;i<b.size();++i)
      printf("%d ", b[i]);
    printf("\n");
  };
  
  if (found)
    return;

  if (now == n)
    return;
  else 
  {
    search(now+1,sum1,sum2);
    a.push_back(s[now]);
    search(now+1,sum1+s[now],sum2);
    a.pop_back();

    b.push_back(s[now]);
    search(now+1,sum1,sum2+s[now]);
    b.pop_back();
  };
};


int main()
{
  int n1,i1;
  cin >> n1;
  for (i1=1;i1<=n1;++i1)
  {
    int i,j,k,l,m;
    cin >> n;

    s.clear();
    s.resize(n);
    a.clear();
    b.clear();
    found = false;
    for (i=0;i<n;++i)
      cin >> s[i];

    printf("Case #%d:\n",i1);
    search(0,0,0);
    if (not found)
      printf("Impossible\n");
  };

};
