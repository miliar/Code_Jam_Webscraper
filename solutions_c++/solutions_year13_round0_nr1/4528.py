#include <cstring>
#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define mp make_pair
#define ITER(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define mod 1000000007
#define MAXN 1000010
#define ff first
#define ss second
#define get getchar//_unlocked
inline int inp()
{
    int n=0,s=1;
    char p=get();
    if(p=='-')
    s=-1;
    while((p<'0'||p>'9')&&p!=EOF)
    p=get();
    while(p>='0'&&p<='9')
    {
    n = (n<< 3) + (n<< 1) + (p - '0');
    p=get();
    };
    return n*s;
}
char a[5][5];
int main()
{
    int i,n,j,k,l,m,t,c=0,ans,p,f,x,o;
    scanf("%d",&t);
    for(p=1;p<=t;p++)
    {
        f=0;l=0;
      for(i=0;i<4;i++)
      {
          scanf("%s",a[i]);
        // getchar();
      }
      /*for(i=0;i<4;i++)
      {
          printf("%s",a[i]);printf("\n");
      }*/
       for(i=0;i<4;i++)
       {
          for(j=0,x=0,o=0,m=0;j<4;j++)
          {
            if(a[i][j]=='X')
            x++;
            else if(a[i][j]=='O')
            o++;
            else if(a[i][j]=='T')
            m++;
            else if(a[i][j]=='.')
            l++;
          }
          if((x+m)==4)
          {
              printf("Case #%d: X won\n",p);f=1;break;
          }
          if((o+m)==4)
          {
              printf("Case #%d: O won\n",p);f=1;break;
          }
       }
       for(j=0;j<4&&!f;j++)
       {
          for(i=0,x=0,o=0,m=0;i<4;i++)
          {
            if(a[i][j]=='X')
            x++;
            else if(a[i][j]=='O')
            o++;
            else if(a[i][j]=='T')
            m++;
          }
         // printf("%d\n",o+m);
          if((x+m)==4)
          {
              printf("Case #%d: X won\n",p);f=1;break;
          }
          if((o+m)==4)
          {
              printf("Case #%d: O won\n",p);f=1;break;
          }
       }
          for(i=0,j=0,x=0,o=0,m=0;i<4&&!f;i++,j++)
          {
            if(a[i][j]=='X')
            x++;
            else if(a[i][j]=='O')
            o++;
            else if(a[i][j]=='T')
            m++;
              // printf("%d\n",o+m);
          if((x+m)==4)
          {
              printf("Case #%d: X won\n",p);f=1;break;
          }
          if((o+m)==4)
          {
              printf("Case #%d: O won\n",p);f=1;break;
          }
          }
          for(i=0,j=3,x=0,o=0,m=0;i<4&&!f;i++,j--)
          {
            if(a[i][j]=='X')
            x++;
            else if(a[i][j]=='O')
            o++;
            else if(a[i][j]=='T')
            m++;
          if((x+m)==4)
          {
              printf("Case #%d: X won\n",p);f=1;break;
          }
          if((o+m)==4)
          {
              printf("Case #%d: O won\n",p);f=1;break;
          }
          }

          if(f==0)
          {
              if(l>0)
              {
                  printf("Case #%d: Game has not completed\n",p);continue;
              }
              else printf("Case #%d: Draw\n",p);
          }
        //getchar();
    }
    return 0;
}
