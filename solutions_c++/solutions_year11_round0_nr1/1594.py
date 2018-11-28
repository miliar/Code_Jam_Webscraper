#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
using namespace std;


int main()
{
    int cas;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &cas);
    int T=0;
    while(cas--)
    {
       int n;
       char ch;
       T++;
       int dis;
       int cur1=1, cur2=1;
       int res1=0, res2=0;
       scanf("%d", &n);
       int res = 0;
       for(int i=0; i<n; ++i)
       {
          scanf(" %c %d", &ch, &dis);
          int tmp = 0;
          if(ch=='O')
          {
             tmp = abs(dis-cur1)+1;
             res1 += tmp;
             cur1 = dis;
             if(res1 <= res2) 
               res1 = res2+1;
          }
          else
          {
              tmp = abs(dis-cur2)+1;
              cur2 = dis;
              res2 += tmp;
              if(res2 <= res1)
                res2 = res1+1;
          }
          //clog<< res1 <<"   "<<res2<<"  kirk\n";
       }
       res = max(res1, res2);
       printf("Case #%d: %d\n",T, res);
    }
    //system("pause");
    return 0;
} 

