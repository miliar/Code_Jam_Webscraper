#include<algorithm>
#include<cstdio>
using namespace std;
int main()
{
  int t;
  scanf("%d",&t);
  for(int i=1;i<=t;++i)
  {
    long long n;
    int pd,pg;
    scanf("%I64d%d%d",&n,&pd,&pg);
    printf("Case #%d: %s\n",i,(100/__gcd(pd,100)>n)||(pd<100&&pg==100)||(pd>0&pg==0)?"Broken":"Possible");
  }
  return 0;
}
