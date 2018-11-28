#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define REP(z,n) for(int (z)=0;(z)<(n);++(z))

int main()
{
 int t,n,tmp,p,c,minc;; scanf("%d", &t);
 bool is[105];
 int a[105];
 for(int q=0;q<t;++q)
 {
  scanf("%d", &p);
  scanf("%d", &n);
  for(int i=0;i<n;++i) { scanf("%d", &a[i]); a[i]--; }
  minc=1000000007;
  do
  {
   REP(i,100) is[i]=1;
   c=0;
   REP(i, n)
   {
    is[a[i]]=0;
    for(int k=a[i]-1;k>=0;--k)
    {
     if(!is[k]) break;
     c++;
    }
    for(int k=a[i]+1;k<p;++k)
    {
     if(!is[k]) break;
     c++;
    }
   }
   if(c<minc) minc=c;
  } while(next_permutation(a, a+n)!=0);
  printf("Case #%d: %d\n", q+1, minc);
 }





}
