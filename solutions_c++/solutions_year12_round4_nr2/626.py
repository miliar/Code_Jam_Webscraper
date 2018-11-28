#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main()
{
  int t1;
  scanf("%d ",&t1);
  for(int i1=1; i1<=t1; i1++)
  {
    int n,w,h;
    scanf("%d %d %d ",&n,&w,&h);
    vector<int> A;
    for(int i=0; i<n; i++)
    {
      int x;
      scanf("%d ",&x);
      A.push_back(x);
    }
    //sort(A.begin(),A.end());
    vector<pair<int,int> > V;
    for(int i=0; i<n; i++) V.push_back(make_pair(-1,-1));
    bool t=false;
    for(int k=0; k<n; k++)
    {
      t=false;
      for(int i=0; i<=w; i++)
      {
	for(int j=0; j<=h; j++)
	{
	  t=true;
	  int posun=0;
	  for(int p=0; p<k; p++)
	  {
	    if(i-V[p].first<A[k]+A[p] && j-V[p].second<A[k]+A[p]) {t=false; posun=V[p].second+A[p]+A[k]-1;}
	  }
	  if(t) {V[k]=make_pair(i,j); break;}
	  else j=posun;
	}
	if(t) break;
      }
    }
    printf("Case #%d:",i1);
    for(int i=0; i<n; i++) printf(" %d %d",V[i].first,V[i].second); printf("\n");
  }
  return 0;
}