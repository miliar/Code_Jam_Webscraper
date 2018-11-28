#include <stdio.h>
int i,j,i1,ia,l,d,n,rd;
char s[6000][100];
char st[6000];
bool ind,ind1;
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
scanf("%d %d %d\n",&l,&d,&n);
for(i=0;i<d;i++)
   gets(s[i]);
for(i=0;i<n;i++)
   {
   printf("Case #%d: ",i+1);
   gets(st);
   rd=0;
   for(j=0;j<d;j++)
      {
      i1=ia=0;
      ind=0;
      while(st[i1])
         {
         if(st[i1]!='(')
            {
            if(st[i1]==s[j][ia])
               {
               i1++;
               ia++;
               continue;
               }
            else
               {
               ind=1;
               break;
               }
            }
         else
            {
            for(ind1=0,i1++;st[i1]!=')';i1++)
               if(st[i1]==s[j][ia])
                  ind1=1;
            if(!ind1)
               {
               ind=1;
               break;
               }
            i1++;
            }
         ia++;
         }
      if(!ind) rd++;
      }
   printf("%d\n",rd);
   }
return 0;
}
