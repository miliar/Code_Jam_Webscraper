#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <functional>
#include <stack>
#include <cmath>
#define MMset(a,b) memset(a,b,sizeof(a))
#define max(a,b)   ((a)>(b)?(a):(b))
#define min(a,b)   ((a)<(b)?(a):(b))
#define eps 1e-8
using namespace std;
int T,N;
char com[2]; 
int ab(int a){return a>0?a:-a;}
int main()
{
    
    //freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&N);
        char pre;
        int cnt = 0,ti=0;
        int end;
        int nowo = 1,nowb = 1,nexto,nextb;
        for (int i=0;i<N;i++)
        {
            scanf("%s%d",&com,&end);
            if (!i)
            {
               pre=com[0];
               if (com[0]=='O') ti=end-nowo+1,nowo=end;
               else             ti=end-nowb+1,nowb=end;
               continue;
            }
            if (com[0]=='O')
            {
               if (pre==com[0])
               {
                  ti+=(ab(end-nowo)+1);
               }
               else
               {
                   cnt+=ti;
                   if (ti>=ab(end-nowo)) ti=1;
                   else                ti=ab(end-nowo)-ti+1;
               }
               nowo=end;
               pre='O';
            }
            if (com[0]=='B')
            {
               if (pre==com[0])
               {
                  ti+=(ab(end-nowb)+1);
               }
               else
               {
                   cnt+=ti;
                   if (ti>=(ab(end-nowb))) ti=1;
                   else                ti=ab(end-nowb)-ti+1;
               }
               nowb=end;
               pre='B';
            }    
        }
        cnt+=ti;
        printf("Case #%d: %d\n",cas,cnt);
    }
}
