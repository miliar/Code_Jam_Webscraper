#include <iostream>
#define N 1500

using namespace std;

int rd()
{
  int h,m,t;
  scanf("%d:%d",&h,&m);
  t=h*60+m; // printf("%d:%d => %d\n",h,m,t);
  return t;
}

int main()
{
int depa[N],depb[N],arra[N],arrb[N];
int n,na,nb,t;

scanf("%d",&n);

for(int loop=1;loop<=n;loop++)
{
  int t1,t2;

  for(int i=0;i<N;i++) depa[i]=depb[i]=arra[i]=arrb[i]=0;
  scanf("%d",&t);
  scanf("%d%d",&na,&nb);
  for(int i=0;i<na;i++)
  {
    t1=rd(); t2=rd()+t;
    depa[t1]++; arrb[t2]++;
  }
  for(int i=0;i<nb;i++)
  {
    t1=rd(); t2=rd()+t;
    depb[t1]++; arra[t2]++;
  }

  int ma=0,mb=0,na=0,nb=0;
  for(int i=0;i<1440;i++)
  {
    na+=depa[i]-arra[i];
    nb+=depb[i]-arrb[i];
    if (na>ma) ma=na;
    if (nb>mb) mb=nb;
  }

  printf("Case #%d: %d %d\n",loop,ma,mb);
}

}
