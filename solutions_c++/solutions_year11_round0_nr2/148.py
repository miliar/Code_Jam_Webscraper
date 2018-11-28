#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

const int n = 26;
const int maxm(105);

bool combine[n][n] , dis[n][n];
int stack[maxm],num,became[n][n];
char ss[maxm];

int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int task;
   scanf("%d",&task);
   for (int cases(1);cases<=task;cases++)
   {
      memset(combine,0,sizeof(combine));
      memset(dis,0,sizeof(dis));
//      memset(list,0,sizeof(list));
      memset(stack,0,sizeof(stack));
      num = 0;
      int edge;
      scanf("%d",&edge);
      for (int i(1);i<=edge;i++)
      {
         char s[5];
         scanf("%s",s);
         combine[s[0] - 65][s[1] - 65] = true;
         combine[s[1] - 65][s[0] - 65] = true;
         became[s[0] - 65][s[1] - 65] = s[2] - 65;
         became[s[1] - 65][s[0] - 65] = s[2] - 65;
      }
      scanf("%d",&edge);
      for (int i(1);i<=edge;i++)
      {
         char s[5];
         scanf("%s",s);
         dis[s[0] - 65][s[1] - 65] = true;
         dis[s[1] - 65][s[0] - 65] = true;
      }
      int m;
      scanf("%d",&m);
      scanf("%s",ss);
      int tot = 0;
      for (int i(0);i<m;i++)
      {
//         ss[i] - 65;
         stack[++tot] = ss[i] - 65;
         if (tot > 1)
         {
            if (combine[stack[tot-1]][stack[tot]])
               {
                  stack[tot-1] = became[stack[tot-1]][stack[tot]];
                  tot--;
               } else
               {
                  for (int j(1);j<tot;j++)
                  if (dis[stack[tot]][stack[j]])
                  {
                     tot = 0;
                        break;
                  }
               }
         }
      }
      /*   while (tot > 0)
         {
            if (tot == 1) break;
            if (combine[stack[tot-1]][stack[tot]])
            {
               stack[tot-1] = became[stack[tot-1]][stack[tot]];
               tot--;
            } else
            {
               break;
            }
         }*/
//      }
      printf("Case #%d: [",cases);
      bool first(true);
      for (int i(1);i<=tot;i++)
      {
         if (i == 1)
            printf("%c",stack[i] + 65);
         else printf(", %c",stack[i] + 65);
      }
      printf("]\n");
   }
   return 0;
}
