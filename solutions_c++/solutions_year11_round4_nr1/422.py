#include"stdio.h"
#include"algorithm"
using namespace std;
struct str
{
  int length,speed;
  bool operator<(const str a)const
  {
    return speed<a.speed;
  }
};
int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
    int len,r,s,time;
    scanf("%d%d%d%d",&len,&s,&r,&time);
    r=r-s;
    double total=0;
    int n;
    scanf("%d",&n);
    str rec[n+1];
    for(int x=0;x<n;x++)
    {
      int a,b;
      scanf("%d%d%d",&a,&b,&rec[x].speed);
      rec[x].speed+=s;
      rec[x].length=b-a;
      len-=rec[x].length;
      total+=rec[x].length/(rec[x].speed+0.0);
    }
    rec[n].length=len;
    rec[n].speed=s;
    n++;
    total+=len/(s+0.0);
    sort(rec,rec+n);
    double money=time;
    int x=0;
    while(x<n && money>0)
    {
      double rate=r/(double)rec[x].speed,save=min(rate*money,r*rec[x].length/(0.0+rec[x].speed*(rec[x].speed+r)));
      total-=save;
      money-=save/rate;
      x++;
    }
    printf("Case #%d: %f\n",t,total);
  }
}