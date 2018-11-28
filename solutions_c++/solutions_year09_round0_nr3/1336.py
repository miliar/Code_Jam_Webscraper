#include <stdio.h>
#include <string.h>

char str[600];
long cnt[600][2];

main()
{
  freopen("file.in","r",stdin);
  freopen("file.out","w",stdout);
  char jam[] = "welcome to code jam";
  long tc,t,i,j,ind,ind2,num,num2,l;
  scanf("%d\n",&t);
  for(tc=1;tc<=t;tc++)
  {
    gets(str); ind  = 0;
    l = strlen(str);
    if(str[0]=='w') cnt[0][0]=1; else cnt[0][0]=0;
    for(j=1;j<l;j++)
    {
      cnt[j][0] = cnt[j-1][0];
      if(str[j]=='w')cnt[j][0]++;
    }
      
    for(i=1;i<19;i++)
    {
      ind2 = ind^1;
      for(j=0;j<l;j++)
        cnt[j][ind2] = 0;
      for(j=0;j<l;j++)
      {
        if(j==0)
        { 
          num = 0;
          num2 = 0;
        }
        else
        {
          num = cnt[j-1][ind];
          num2 = cnt[j-1][ind2];
        }
        if(str[j]==jam[i]) cnt[j][ind2] = (num2+num)%10000;
        else               cnt[j][ind2] = num2;
      }
      ind^=1;
    }
    printf("Case #%d: %.04d\n",tc,cnt[l-1][ind2]);
    
  }
}
