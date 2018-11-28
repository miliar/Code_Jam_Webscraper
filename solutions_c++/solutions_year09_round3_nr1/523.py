#include <stdio.h>
#include <string.h>
#include <iostream>

char str[100];
long num[300];
bool fix[300];
main()
{
  freopen("file.in","r",stdin);
  freopen("file.out","w",stdout);
  long tc,t,i,j,cnt,l,cur;
  long long ans,p;
  scanf("%d\n",&t);
  for(tc=1;tc<=t;tc++)
  {
    for(i=0;i<260;i++)
    {
      fix[i]=false;
      num[i]=-1;
    }
    gets(str);
    cnt = 0;
    for(i=0;str[i]!=0;i++)
      if(!fix[str[i]])
      {
        cnt++;
        fix[str[i]]=true;
      }
    if(cnt<2)cnt=2;
    l = strlen(str);
    num[str[0]]=1;
    cur = 0;
    for(i=1;i<l;i++)
      if(num[str[i]]==-1)
      {
        num[str[i]]=cur;
        cur = (cur==0)? 2 : cur+1;
      }
    
    ans = 0; p = 1;
    for(i=l-1;i>=0;i--)
    {
      ans += (long long)num[str[i]]*(long long)p;
      p *= cnt;
    }
    
    printf("Case #%d: ",tc);
    std::cout << ans << "\n";
  }
}
