#include<algorithm>
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<string.h>
#include<set>
#include<map>
#define taskname ""
#define sqr(a) (a)*(a)
#define pi pair<int,int>
#define forn(i,n) for(int i=0;i<(int)n;i++)
using namespace std;
int c[200],m;
map <pi,int> x;
int f(int i,int j)
{
  if(x[pi(i,j)]!=0)
    return x[pi(i,j)];
  int mn=1<<30;
  for(int q=0;q<m;q++)
    if(c[q]>=i&&c[q]<=j)
      mn<?=f(i,c[q]-1)+f(c[q]+1,j)+j-i;
  if(mn!=1<<30)
    return x[pi(i,j)]=mn;
  return 0;
}
int main()
{
  int p,t;
  freopen(taskname"in","r",stdin);
  freopen(taskname"out","w",stdout);
  scanf("%d",&t);
  for(int j=1;j<=t;j++)
  {
    scanf("%d %d",&p,&m);
	x.clear();
    forn(i,m)
      scanf("%d",&c[i]);
	//x.remove(x.begin(),x.end())
	printf("Case #%d: %d\n",j,f(1,p));
  }
  return 0;
}