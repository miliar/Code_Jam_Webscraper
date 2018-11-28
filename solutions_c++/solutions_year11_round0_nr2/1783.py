#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int combine[26][26];
bool opposed[26][26];
int main()
{
  freopen("B.in","r",stdin);
   freopen("B.out","w",stdout);
   int cas,cnt,c,d,n,i,j,index;
   char str[10],invoke[105],final[205];
   scanf("%d",&cas);
   for(cnt=1;cnt<=cas;cnt++)
   {
       memset(combine,-1,sizeof(combine));
       memset(opposed,0,sizeof(opposed));
       scanf("%d",&c);
       while(c--)
       {
           scanf("%s",str);
           combine[str[0]-'A'][str[1]-'A']=(int)str[2];
           combine[str[1]-'A'][str[0]-'A']=(int)str[2];
       }
       scanf("%d",&d);
       while(d--)
       {
           scanf("%s",str);
           opposed[str[0]-'A'][str[1]-'A']=true;
           opposed[str[1]-'A'][str[0]-'A']=true;
       }
       scanf("%d",&n);
       scanf("%s",invoke);
       index=-1;
       for(i=0;invoke[i]!='\0';i++)
       {
          final[++index]=invoke[i];
          while(index>=1&&combine[final[index]-'A'][final[index-1]-'A']!=-1)
          {
              final[index-1]=(char)combine[final[index]-'A'][final[index-1]-'A'];
              index--;
          }
          for(j=0;j<index;j++)
            {
                if(opposed[final[j]-'A'][final[index]-'A'])
                    break;
            }
          if(j<index) index=-1;
        }
       printf("Case #%d: [",cnt);
       for(i=0;i<index;i++)
        printf("%c, ",final[i]);
       if(index>=0)
       printf("%c",final[i]);
       printf("]\n");
   }
}
