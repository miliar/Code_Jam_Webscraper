#include <iostream>
#include<ctype.h>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>
#include<queue>
#include<cassert>
#include<iterator>
#include<cmath>
using namespace std ;
int main()
{
   char a[100];

   a[0] = 'y';//a
   a[1] = 'h';//b
   a[2] = 'e';
   a[3] = 's';
   a[4] = 'o';//e
   a[5] = 'c';//f
   a[6] = 'v';//g
   a[7] = 'x';
   a[8] = 'd';
   a[9] = 'u';//j
   a[10] = 'i';//k
   a[11] = 'g';
   a[12] = 'l';
   a[13] = 'b';//n
   a[14] = 'k';//o
   a[15] = 'r';
   a[16] = 'z';
   a[17] = 't';//r
   a[18] = 'n';//s
   a[19] = 'w';
   a[20] = 'j';//u
   a[21] = 'p';//v
   a[22] = 'f';//w
   a[23] = 'm';//x------
   a[24] = 'a';//y
   a[25] = 'q';//z

   int test;
   int i,j;
   char dum;
   scanf("%d",&test);
   scanf("%c",&dum);
   char str[200];
   for(i=1;i<=test;i++)
   {
      scanf("%[^\n]",str);
      scanf("%c",&dum);
      printf("Case #%d: ",i);
      for(j=0;j<strlen(str);j++)
      {
         if(str[j]==' ')
            printf("%c",str[j]);
         else
         {
            int x = str[j] - 'a';
            printf("%c",a[x]);
         }
      }
      printf("\n");
   }


   



   return 0;
}
