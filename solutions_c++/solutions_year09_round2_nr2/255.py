#include <stdio.h>
#include <algorithm>
using namespace std;
int ii,t,n,i;
char ch;
char s[1000];
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
scanf("%d\n",&t);
for(ii=1;ii<=t;ii++)
   {
   printf("Case #%d: ",ii);
   gets(s);
   n=0;
   while(s[++n]);
   if(!next_permutation(s,s+n))
      {
      sort(s,s+n);
      for(i=0;;i++)
         if(s[i]!='0')
            {
            ch=s[i];
            s[i]='0';
            break;
            }
      putchar(ch);
      puts(s);
      }
   else
      puts(s);
   }
return 0;
}
