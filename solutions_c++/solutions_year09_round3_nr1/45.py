#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

typedef __int64 lint;

int main()
  {
  int T;

  scanf("%d \n",&T);
  for(int t=0;t<T;++t)
    {
    char buf[256];
    gets(buf);
    string s(buf);

    string s2(s);
    sort(s2.begin(),s2.end());
    s2.erase(unique(s2.begin(),s2.end()),s2.end());
    int base=s2.size();
    if (base==1) base=2;

    map<char,int> D;
    int next=0;
    for(size_t i=0;i<s.size();++i)
      {
      if (i==0)
        {
        D[s[i]]=1;
        continue;
        }
      if (D.find(s[i])==D.end())
        {
        D[s[i]]=next;
        if (++next==1) ++next;
        }
      }

    lint ret=0,mul=1;
    for(int i=int(s.size())-1;i>=0;--i)
      {
      ret+=lint(D[s[i]])*mul;
      mul*=lint(base);
      }

    //if (s.size()==1) ret=0;
    cout << "Case #"<<t+1<<": "<<ret<<endl;
    }

  return 0;
  }