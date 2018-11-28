#include <stdio.h>
#include <string.h>

char s[20];
int num[100];
int mention[100];
int pos(char c)
{
        if (c>='0' && c<='9') return c-'0';
        else return c-'a' + 10;
}
int pow(int a,int n)
{
        int i;
        int re=1;
        for (i=1;i<=n;i++) re*=a;
        return re;
}
int main()
{
freopen("a.in","r",stdin);
freopen("a.out","w",stdout);
        int css;
        scanf("%d",&css);
        int cs;
        for (cs=1;cs<=css;cs++)
        {
               scanf("%s",s);
               int i;
               memset(mention,0,sizeof(mention));
               for (i=0;s[i]!=0;i++) mention[pos(s[i])]++;
               int k=0;
               for (i=0;i<=99;i++) if (mention[i]) k++;
               if (k<2) k=2;
               for (i=0;i<=99;i++) num[i]=-1;
               
               num[pos(s[0])]=1;
               i=1;while (s[i]==s[0]) i++;
               if (s[i]!=0) num[pos(s[i])]=0;
               int p = 2;
               
               for (i=0;s[i]!=0;i++)
               {
                       if (num[pos(s[i])]==-1) {num[pos(s[i])] = p;p++;}
               }
               
               int len = strlen(s);
               long long re=0;
               for (i=0;s[i]!=0;i++) re += num[pos(s[i])] *pow(k,len-i-1);
               printf("Case #%d: %I64d\n",cs,re);
             //  printf("%s\n",s);
//               for (i=0;s[i]!=0;i++) printf("%d ",num[pos(s[i])]);
//               printf("\n"); 
        }
        return 0;
}
               
        
