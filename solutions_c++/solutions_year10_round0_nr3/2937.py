#include"cstdio"
#include"list"
using namespace std;
long long t,r,k,n;
list<long long> a;
int main()
{
  long long c1,c2,c3,t1,ans=0,sum=0;
  freopen("C-small-attempt0.in","r",stdin);
  freopen("themepark.out","w",stdout);
  scanf("%lld",&t);
  for(c1=0;t>c1;c1++,ans=0,a.clear())
  {
    scanf("%lld %lld %lld",&r,&k,&n);
    for(c2=0;n>c2;c2++)
    {
      scanf("%lld",&t1);
      a.push_back(t1);
    }
    for(c2=0,c3=0;r>c2;c2++,c3=0,sum=0)
      while(sum+a.front()<=k&&n>c3)
      {
        ans+=a.front();
        sum=sum+a.front();
        a.push_back(a.front());
        a.pop_front();
        c3++;
      }
    printf("Case #%lld: %lld\n",c1+1,ans);
  }
}
