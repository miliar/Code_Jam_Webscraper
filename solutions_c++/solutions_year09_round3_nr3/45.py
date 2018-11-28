#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

int P,Q;
vector<int> pris;

map<pair<int,int>,int> A;

int Rec(int l, int r)
  {
  if (l>=r) return 0;

  if (A.find(make_pair(l,r))!=A.end())
    return A[make_pair(l,r)];

  int ret=-1;

  for(int i=0;i<pris.size();++i) if (pris[i]>=l && pris[i]<=r)
    {
    int tmp=r-l;
    tmp+=Rec(l,pris[i]-1)+Rec(pris[i]+1,r);
    if (ret==-1 || tmp<ret) ret=tmp;
    }

  if (ret==-1) ret=0;
  return A[make_pair(l,r)]=ret;
  }

int main()
  {
  int T;

  scanf("%d ",&T);
  for(int t=0;t<T;++t)
    {
    scanf("%d %d ",&P,&Q);

    pris.clear();
    for(int i=0;i<Q;++i)
      {
      int pos;
      scanf("%d ",&pos);
      pris.push_back(pos);
      }

    A.clear();
    int ret=Rec(1,P);

    printf("Case #%d: %d\n",t+1,ret);
    }

  return 0;
  }