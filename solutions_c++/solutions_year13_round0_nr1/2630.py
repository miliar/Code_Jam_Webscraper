                  /* Original Author: Akash Sinha(sinaka) 
                       Problem Code:
                       Language: c++
                    */
using namespace std;
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include<conio.h>

//DEFINITIONS

#define LL  long long int
#define ULL  unsigned long long int
#define DB double
#define LDB long double
#define PB push_back
#define MP make_pair
#define SL(a) scanf("%lld",&a)
#define S(a) scanf("%d",&a)
#define SC(a) scanf("%c",&ch)
#define SD(a) scanf("%lf",&a)
#define PL(a) printf("%lld",a)
#define P(a) printf("%d",a)
#define PC(a) printf("%c",a)
#define PD(a) printf("%lf",a)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define NL printf("\n")
#define W(t) while(t--)
#define FOR(i,lo,hi) for(i=lo;i<hi;i++)
#define gc getchar_unlocked
#define MOD 1000000007
int main()
{
     freopen("C:\\Users\\suyash\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\suyash\\Desktop\\output.txt","w",stdout);
    char arr[10][10];
    int t,i,j,k,dots,x,y,tc;
    bool flagx,flagy;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        for(i=0;i<4;i++)
        scanf("%s",arr[i]);
        dots=0;x=0;y=0;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        if(arr[i][j]=='.')
        dots++;
        flagx=false;flagy=false;
        //check horizontal...
        for(i=0;i<4;i++)
        {
           x=0;y=0;
           for(j=0;j<4;j++)
           {
               if((arr[i][j]=='X')||(arr[i][j]=='T'))
               x++;
               if((arr[i][j]=='O')||(arr[i][j]=='T'))
               y++;
           }
           if(x==4)
           {
              flagx=true;
              break;
           }
           if(y==4)
           {
              flagy=true;
              break;
           }
        }
        //check vertical...
        if((!flagx)&&(!flagy))
        for(i=0;i<4;i++)
        {
           x=0;y=0;
           for(j=0;j<4;j++)
           {
               if((arr[j][i]=='X')||(arr[j][i]=='T'))
               x++;
               if((arr[j][i]=='O')||(arr[j][i]=='T'))
               y++;
           }
           if(x==4)
           {
              flagx=true;
              break;
           }
           if(y==4)
           {
              flagy=true;
              break;
           }
        }
        //check left diagonal...
        if((!flagx)&&(!flagy))
        {
            x=0;y=0;
            if((arr[0][0]=='X')||(arr[0][0]=='T'))
            x++;
            if((arr[0][0]=='O')||(arr[0][0]=='T'))
            y++;
            if((arr[1][1]=='X')||(arr[1][1]=='T'))
            x++;
            if((arr[1][1]=='O')||(arr[1][1]=='T'))
            y++;
            if((arr[2][2]=='X')||(arr[2][2]=='T'))
            x++;
            if((arr[2][2]=='O')||(arr[2][2]=='T'))
            y++;
            if((arr[3][3]=='X')||(arr[3][3]=='T'))
            x++;
            if((arr[3][3]=='O')||(arr[3][3]=='T'))
            y++;
            if(x==4)
            flagx=true;
            if(y==4)
            flagy=true;
        }
        //check roght diagonal...
        if((!flagx)&&(!flagy))
        {
            x=0;y=0;
            if((arr[0][3]=='X')||(arr[0][3]=='T'))
            x++;
            if((arr[0][3]=='O')||(arr[0][3]=='T'))
            y++;
            if((arr[1][2]=='X')||(arr[1][2]=='T'))
            x++;
            if((arr[1][2]=='O')||(arr[1][2]=='T'))
            y++;
            if((arr[2][1]=='X')||(arr[2][1]=='T'))
            x++;
            if((arr[2][1]=='O')||(arr[2][1]=='T'))
            y++;
            if((arr[3][0]=='X')||(arr[3][0]=='T'))
            x++;
            if((arr[3][0]=='O')||(arr[3][0]=='T'))
            y++;
            if(x==4)
            flagx=true;
            if(y==4)
            flagy=true;
        }
        if(flagx)
        printf("Case #%d: X won\n",tc);
        else if(flagy)
        printf("Case #%d: O won\n",tc);
        else if(dots!=0)
        printf("Case #%d: Game has not completed\n",tc);
        else
        printf("Case #%d: Draw\n",tc);
    }
    getch();
    return 0;
}
