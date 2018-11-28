#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<pair<int,int> > VPII;

void solve(int tc)
{
  int T,NA,NB;
  scanf("%d %d %d ",&T,&NA,&NB);

  VPII A, B;

  for(int i=0;i<NA;++i)
  {
    int ah,am,bh,bm;
    scanf("%d:%d %d:%d ",&ah,&am,&bh,&bm);
    A.push_back(make_pair(60*ah+am,1));
    B.push_back(make_pair(60*bh+bm+T,-1));
  }
  for(int i=0;i<NB;++i)
  {
    int bh,bm,ah,am;
    scanf("%d:%d %d:%d ",&bh,&bm,&ah,&am);
    B.push_back(make_pair(60*bh+bm,1));
    A.push_back(make_pair(60*ah+am+T,-1));
  }

  sort(A.begin(),A.end()); sort(B.begin(),B.end());

  int sa=0,sb=0;

  int n=0;
  for(VPII::iterator i=A.begin();i!=A.end();++i)
  {
    n+=i->second;
    if(n>sa)sa=n;
  }
  n=0;
  for(VPII::iterator i=B.begin();i!=B.end();++i)
  {
    n+=i->second;
    if(n>sb)sb=n;
  }

  printf("Case #%d: %d %d\n",tc,sa,sb);
}

int main()
{
  int T;
  scanf("%d ",&T);
  for(int i=0;i<T;i++)solve(i+1);
  return 0;
}
