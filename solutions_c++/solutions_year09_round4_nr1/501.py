#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

bool test(vector<char> &v)
  {
  for(int i=0;i<v.size();++i)
    if (v[i]>i) return false;
  return true;
  }

int main()
  {
  int T;

  scanf("%d ",&T);
  for(int t=0;t<T;++t)
    {
    int N;
    scanf("%d ",&N);

    vector<char> v;
    for(int i=0;i<N;++i)
      {
      char buf[256];
      gets(buf);
      string s(buf);
      int mx=0;
      for(int j=0;j<s.size();++j)
        if (s[j]=='1') mx=j;

      v.push_back(mx);
      }

    int ret=0;

    for(int i=0;i<N-1;++i)
      {
      if (v[i]<=i) continue;
      for(int j=i+1;j<N;++j) if(v[j]<=i)
        {
        ret+=j-i;
        int save=v[i];
        for(int k=j;k>i;--k) v[k]=v[k-1];
        v[i]=save;
        break;
        }
      }

    printf("Case #%d: %d\n",t+1,ret);
    }

  return 0;
  }