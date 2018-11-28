#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#define PB push_back
using namespace std;
int main()
{
   int T,cas=1;
   freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\data.in","r",stdin);
   freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\data.out","w",stdout);
   scanf("%d",&T);
   while(T--)
   {
      int n,k,i;
      string sta;
      scanf("%d%d",&n,&k);
      k%=(1<<n);
      printf("Case #%d: ",cas++);
      if(k==((1<<n)-1))puts("ON");
      else puts("OFF");
   }
}
