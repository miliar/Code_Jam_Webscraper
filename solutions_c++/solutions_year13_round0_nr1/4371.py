/*
ID: prodigyaj
LANG: C++
TASK:
*/

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
#include <fstream>
#include <cstring>

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)
#define pb push_back
#define C(x) cout<<x<<" "
#define CE(x) cout<<#x<<" : "<<x<<endl

using namespace std;
using namespace __gnu_cxx;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
char b[4][4];
bool checkWin(char c)
{
     FOR(i,4) // row check
     {
        int cnt = 0;
        FOR(j,4)
        {
            //cout<<b[i][j]<<" "<<c<<endl;    
            if(b[i][j]==c || b[i][j]=='T')
               cnt++;
        }
        if(cnt==4)
            return true;
     }
     
     FOR(j,4) // column check
     {
        int cnt = 0;
        FOR(i,4)
            if(b[i][j]==c || b[i][j]=='T')
               cnt++;
        if(cnt==4)
            return true;
     }
     
     int cnt=0;
     for(int i=0,j=0;i<4;i++,j++)
     {    
         if(b[i][j]==c || b[i][j]=='T')
                   cnt++;          
     }
     if(cnt==4)
        return true;
        
     cnt=0;    
     for(int i=0,j=3;i<4;i++,j--)
     {           
         if(b[i][j]==c || b[i][j]=='T')
                   cnt++;
     }
     
     if(cnt==4)
        return true;
        
    return false;    
}
int main()
{
    int t;
    S(t);
    
    FORE(test,t)
    {
                bool dot=false;
                 FOR(i,4)
                     FOR(j,4)
                     {
                         cin>>b[i][j];
                         if(b[i][j]=='.')
                            dot = true;                         
                     }
                 printf("Case #%d: ",test);          
                 if(checkWin('X')==true)
                      printf("X won\n");
                 else
                 if(checkWin('O')==true)
                      printf("O won\n");
                 else
                 if(dot==true)
                     printf("Game has not completed\n");
                 else
                     printf("Draw\n");
                 
    }
return 0;
}
