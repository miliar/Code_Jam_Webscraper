#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
int i,j,t,c,ii,i1,rd;
char mas[500][500];
int pas[2000],raod[2000];
string st;
string ara[2000];
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
cin>>t;
for(ii=1;ii<=t;ii++)
   {
   for(i='A';i<='Z';i++)
      for(j='A';j<='Z';j++)
         mas[i][j] = mas[j][i] = 0;
   for(i=0;i<1000;i++)
      pas[i] = raod[i] = 0;
   printf("Case #%d: ",ii);
   cin>>c;
   for(i=0;i<c;i++)
      {
      cin>>st;
      mas[st[0]][st[1]] = mas[st[1]][st[0]] = st[2];
      }
   cin>>c;
   for(i=0;i<c;i++)
      cin>>ara[i];
   int k;
   cin>>k;
   cin>>st;
   rd = 0;
   for(i=0;i<st.size();i++)
      {
      pas[rd++] = st[i];
      raod[st[i]]++;
      while(rd > 1 && mas[ pas[rd-1] ] [ pas[rd-2] ])
         {
         raod[ pas[rd-1] ]--;
         raod[ pas[rd-2] ]--;
         rd--;
         pas[rd-1] = mas[ pas[rd] ] [ pas[rd-1] ];
         raod[ pas[rd-1] ]++;
         }
      for(j=0;j<c;j++)
         if(raod[ ara[j][0] ] && raod[ ara[j][1] ] )
            {
            rd = 0;
            for(i1='A';i1<='Z';i1++)
               raod[i1] = 0;
            break;
            }
      }
   printf("[");
   if(rd)
      {
      printf("%c",pas[0]);
      for(i=1;i<rd;i++)
         printf(", %c",pas[i]);
      }
   printf("]\n");
   }
return 0;
}
