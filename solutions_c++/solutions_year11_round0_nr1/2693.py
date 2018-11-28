#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
  freopen("robot.in","r",stdin);
  freopen("robot.out","w",stdout);
  int t,to=0;
  scanf("%d",&t);
  while(t--)
  {
    to++;
    printf("Case #%d: ",to);
    int b,n,i;
    int bc[101]={0},oc[101]={0},t[2]={0};
    char c,s[101];
    scanf("%d ",&n);
    for(i=0;i<n;i++)
    {
      scanf("%c %d ",&c,&b);
      s[i]=c;
      if(c=='B')
      {
        t[1]++;
        bc[t[1]]=b;
      }
      else if(c=='O')
      {
        t[0]++;
        oc[t[0]]=b;
      }
      //printf("%c\n",s[i]);
    }
    i=0;
    int time=0,j1=1,j2=1,posb=1,poso=1;
    while(1)
    {
        if(s[i]=='B')
        {
          time+=(fabs(bc[j1]-posb)+1);
          if((fabs(bc[j1]-posb)+1)>=fabs(oc[j2]-poso)) poso=oc[j2];
          else 
          {
            if (poso<oc[j2]) poso+=(fabs(bc[j1]-posb)+1);
            else poso=fabs(poso-(fabs(bc[j1]-posb)+1));
          }
          posb=bc[j1];
          j1++;
          //printf("%c=%d %d %d\n",s[i],time,poso,posb);
        }
        else if(s[i]=='O')
        {
          time+=(fabs(oc[j2]-poso)+1);
          if((fabs(oc[j2]-poso)+1)>=fabs(bc[j1]-posb)) posb=bc[j1];
          else 
          {
            if (posb<bc[j1]) posb+=(fabs(oc[j2]-poso)+1);
            else posb=fabs(posb-(fabs(oc[j2]-poso)+1));
          }
          poso=oc[j2];
          j2++;
          //printf("%c=%d %d %d\n",s[i],time,posb,poso);
        }
      i++;
      if(i>=n) break;
    }
    printf("%d\n",time);
  }
  return 0;
}
