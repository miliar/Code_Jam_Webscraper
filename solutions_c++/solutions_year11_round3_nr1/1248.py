#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include<string.h>

using namespace std;
double A[101],W[101],T[101],arr[101];
char S[1001],SS[101][101];
int k,c;
bool valid(int r,int cc)
{
    if(r>=k || cc>=c || r<=-1 || cc<=-1) return 0;
    return 1;
}
int main()
{
   freopen("a.txt","r",stdin);
   freopen("a.out","w",stdout);
    int t,i,j,cnt,w,l,cas=1;
    double RPI,WP,OWP,OOWP;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&k,&c);

        for(i=0;i<k;i++)
         scanf("%s",SS[i]);

         for(i=0;i<k;i++)
          for(j=0;j<c;j++)
          {
              if(SS[i][j]=='#')
              {
                  if(valid(i,j) && SS[i][j+1]=='#' && SS[i+1][j]=='#' && SS[i+1][j+1]=='#')
                  {
                      SS[i][j]='/';SS[i+1][j+1]='/';SS[i][j+1]='\\';SS[i+1][j]='\\';
                  }
              }
          }
          w=0;
          for(i=0;i<k;i++)
          for(j=0;j<c;j++)
          if(SS[i][j]=='#')
          {
              w=1; break;
          }

        printf("Case #%d:\n",cas++);
        if(w) printf("Impossible\n");
        else
        {
          for(i=0;i<k;i++){
          for(j=0;j<c;j++)
          {
              printf("%c",SS[i][j]);
          }
          printf("\n");}
        }


    }

    return 0;
}
