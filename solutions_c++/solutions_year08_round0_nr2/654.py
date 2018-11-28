#include <cstdio>
#include <algorithm>
using namespace std;
int i,j,k,s,t,n,m,T,ans1,ans2,h1,m1,h2,m2;
struct node{
  int s,e;
  bool vi;
}a[101],b[101];

bool cmp(node x,node y)
{
  return x.s<y.s;
}

void do2(int);
void do1(int nu)
{
  int i;
  a[nu].vi=0;
  for (i=1;i<=m;++i)
    if (b[i].vi && b[i].s>=a[nu].e+t)
      {
	do2(i);
	return;
      }
}

void do2(int nu)
{
  int i;
  b[nu].vi=0;
  for (i=1;i<=n;++i)
    if (a[i].vi && a[i].s>=b[nu].e+t)
      {
	do1(i);
	return;
      }
}
main()
{
  scanf("%d",&T);
  for (int I=1;I<=T;++I)
    {
      scanf("%d",&t);
      scanf("%d%d",&n,&m);
      for (i=1;i<=n;++i)
	{
	  scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
	  a[i].s=h1*60+m1;
	  a[i].e=h2*60+m2;
	  a[i].vi=1;
	}
      for (i=1;i<=m;++i)
	{
	  scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
	  b[i].s=h1*60+m1;
	  b[i].e=h2*60+m2;
	  b[i].vi=1;
	}
      sort(a+1,a+n+1,cmp);
      sort(b+1,b+m+1,cmp);
      ans1=ans2=0;
      while (1){
	for (i=1;i<=n;++i)
	  if (a[i].vi) break;
	for (j=1;j<=m;++j)
	  if (b[j].vi) break;
	if (i<=n && j<=m)
	  {
	    if (a[i].s<=b[j].s) 
	      {
		do1(i);
		++ans1;
	      }
	    else 
	      {
		do2(j);
		++ans2;
	      }
	  }
	else if (i<=n)
	  {
	    ++ans1;
	    do1(i);
	  }
	else if (j<=m)
	  {
	    ++ans2;
	    do2(j);
	  }
	else break;
      }
      
      printf("Case #%d: %d %d\n",I,ans1,ans2);
    }
  return 0;
}


