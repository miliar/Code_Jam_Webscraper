#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int i,j,z,nmb,l,n,c,a[1000000];
__int64 t,time;
bool used[1000000];
vector<pair<int,int>> dist;
vector<int> dist_;
int main()
{
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&nmb);
 for (int i=1;i<=nmb;++i)
 {
  printf("Case #%d: ",i);
  memset(used,false,n);
  scanf("%d %I64d %d %d",&l,&t,&n,&c);
  for (j=0;j<c;++j) scanf("%d",&a[j]);
  dist.clear(); dist_.clear(); int cur=0,last=-1;
  while (dist.size()<n)
  {
   dist.push_back(make_pair(a[cur],dist.size()));
   dist_.push_back(a[cur]);
   ++cur;
   if (cur==c) cur=0;
  }
  time=0;
  for (j=0;j<n;++j)
   if (time+2*dist[j].first<=t)
   {
    time+=2*dist[j].first;
    dist[j].first=0;
   }
   else
   {
    dist[j].first-=(t-time)/2;
    dist_[j]=dist[j].first;
    time=t; last=j;
    break;
   }
  sort(dist.begin(),dist.end());
  for (j=n-1;j>=n-l;--j) used[dist[j].second]=true;
  if (last>=0)
   for (j=last;j<n;++j)
    if (used[j]) time+=dist_[j]; else time+=2*dist_[j];
  printf("%I64d\n",time);
 }
}