#include <cstdio>
#include<cstring>

char s[]="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char a[]="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

char res[1000];
bool v[1000];
int main()
{
   int i;
   char b[10010];
   memset(res,'A',sizeof(res));
   memset(v,false,sizeof(v));
   for(i=0;s[i]!='\0';i++)
   {
       if(s[i]==' ') continue;
       res[s[i]]=a[i];
       v[a[i]]=true;
   }
 //  for(i='a';i<='z';i++) if(res[i]=='A') printf("%c\n",i);
//   for(i='a';i<='z';i++) if(!v[i]) printf("%c\n",i);
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   res['q']='z';
   res['z']='q';
   int n,j,k;
   scanf("%d",&n);
   getchar();
   for(j=1;j<=n;j++)
   {
       gets(b);
       for(k=0;b[k]!='\0';k++)
       {
           if(b[k]==' ') continue;
           b[k]=res[b[k]];
       }
       printf("Case #%d: %s\n",j,b);
   }
   return 0;
}


