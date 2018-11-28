#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

#define DBG(vari) cout<<#vari<<" = "<<(vari)<<endl;
#define dbg(...) fprintf(stderr, __VA_ARGS__)



using namespace std;

int main()
{   freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long int t;
    cin>>t;
    char a[4][4];
   
for(long long int cas=1 ;cas<=t ;cas++)
{  int isdot=0;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
       {cin>>a[i][j];
        if(a[i][j]=='.')
        isdot=1;
       }
        int wonflag=0;
        int sum=0;
        
        for(int i=0;i<4 ;i++)
        {   sum=0;
          sum=a[i][0]+a[i][1]+a[i][2]+a[i][3];
             if(sum==352||sum == 348)
                {
                cout<<"Case #"<<cas<<": X won\n";
                 wonflag=1;
                 break;
                }
             else if((sum ==316) || (sum== 321))
                {cout<<"Case #"<<cas<<": O won\n";
                wonflag=1;
                break;
                }
       }
       if(wonflag!=1)
       {
        for(int i=0;i<4;i++)
          {
           sum=0;
          sum=a[0][i]+a[1][i]+a[2][i]+a[3][i];
             if(sum==352||sum == 348)
                 {cout<<"Case #"<<cas<<": X won\n";
                  wonflag=1;
                  break;
                 }
             else if(sum ==316 || sum== 321)
               {
                   cout<<"Case #"<<cas<<": O won\n";
                   wonflag=1;
                   break;
               }
          }
       }
       if(wonflag!=1)
       {   sum=a[0][0]+a[1][1]+a[2][2]+a[3][3];
           if(sum==352||sum==348)
            {cout<<"Case #"<<cas<<": X won\n";
                  wonflag=1;
            }
           else if(sum ==316 || sum==321)
               {
                   cout<<"Case #"<<cas<<": O won\n";
                   wonflag=1;
               }
           if(wonflag!=1)
           {
            sum=a[0][3]+a[1][2]+a[2][1]+a[3][0];
            if(sum==352||sum==348)
            {cout<<"Case #"<<cas<<": X won\n";
                  wonflag=1;
            }
           else if(sum ==316 || sum== 321)
               {
                   cout<<"Case #"<<cas<<": O won\n";
                   wonflag=1;
               }
           }
        }
       if(wonflag!=1)
       {  /* int rowfound=0;
           for(int i=0;i<4;i++)
           {

            for(int j=0;j<4;j++)
            if(a[i][j]=='.')
            */
          if(isdot==1)
           {//Case #3: Game has not completed
               cout<<"Case #"<<cas<<": Game has not completed\n";
              //  rowfound=1;
                wonflag=1;
             //  break;
           }
          /* if(rowfound==1)
            break;
           }
           */
       }
       if(wonflag!=1)
        cout<<"Case #"<<cas<<": Draw\n";
}
    return 0;
}

