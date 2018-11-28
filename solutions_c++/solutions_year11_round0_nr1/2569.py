#include <cstdio>
#include <queue>
using namespace std;
int t,n,j,time,pos1,pos2;
queue <pair<char,int>> common;
queue <int> r1,r2;
int main()
{
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&t);
 for (int i=1;i<=t;++i)
 {
  printf("Case #%d: ",i);
  scanf("%d",&n);
  for (j=0;j<n;++j)
  {
   pair<char,int> cur;
   scanf(" %c %d",&cur.first,&cur.second);
   common.push(cur);
   if (cur.first=='O') r1.push(cur.second); else r2.push(cur.second);
  }
  time=0; pos1=pos2=1;
  while (!common.empty())
  {
   ++time;
   if (common.front().first=='O')
   {
    if (common.front().second==pos1)
    {
     common.pop();
     r1.pop();
    }
    else
     if (common.front().second>pos1) ++pos1; else --pos1;
    if (r2.empty()) continue;
    if (r2.front()>pos2) ++pos2; else 
     if (r2.front()<pos2) --pos2;
   }
   else
   {
    if (common.front().second==pos2)
    {
     common.pop();
     r2.pop();
    }
    else
     if (common.front().second>pos2) ++pos2; else --pos2;
    if (r1.empty()) continue;
    if (r1.front()>pos1) ++pos1; else 
     if (r1.front()<pos1) --pos1;
   }
  }
  printf("%d\n",time);
  getchar();
 }
}